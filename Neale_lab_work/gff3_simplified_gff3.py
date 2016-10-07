#!/usr/bin/python

from __future__ import print_function, division

gff3_file = '/home/andy/DOC/neale_lab/Arabidopsis_thaliana/TAIR10_GFF3_genes.gff'

# We'll only worry about gene, mRNA, CDS, 5'UTR and 3'UTR

genes = dict()
gene_lines = dict()
cds_count = dict()
orientation = dict()

for gline in open(gff3_file):
    
    gline = gline.rstrip('\n')
    split_line = gline.strip().split('\t')
    if split_line[2] not in ('gene', 'mRNA', 'CDS', 'five_prime_UTR', 'three_prime_UTR'): continue
    
    if split_line[2] == 'gene':
        gene_id = split_line[8].split(';')[0].split('=')[-1]
        assert gene_id not in genes
        genes[gene_id] = dict()
        gene_lines[gene_id] = gline
        orientation[gene_id] = split_line[6]

    elif split_line[2] == 'mRNA':
        # ID=AT1G01020.1;Parent=AT1G01020;Name=AT1G01020.1;Index=1
        mrna_id = split_line[8].split(';')[0].split('=')[-1]
        parent_id = split_line[8].split(';')[1].split('=')[-1]
        assert parent_id in genes
        assert mrna_id not in genes[gene_id]
        genes[gene_id][mrna_id] = list()
        genes[gene_id][mrna_id].append(gline)
        
    else:
        
        mrna_id = split_line[8].split(',')[0].split('=')[-1]
        gene_id = mrna_id.split('.')[0]
        assert gene_id in genes
        assert mrna_id in genes[gene_id]
        genes[gene_id][mrna_id].append(gline)
        
        if split_line[2] == 'CDS':
            if mrna_id not in cds_count: cds_count[mrna_id] = 0
            cds_count[mrna_id] += 1

for gene_id in sorted(genes):
    
    # Skip genes with multiple isoforms as well as features like rRNAs, tRNAs, etc., where we
    # did not capture their data so len(genes[gene_id]) == 0
    if len(genes[gene_id]) != 1: continue

    # Skip genes with '-' orientation
    if orientation[gene_id] == '-': continue

    rna_id = genes[gene_id].keys()[0]
    
    # Skip genes with multiple CDS regions
    if cds_count[rna_id] != 1: continue

    # Skip organellar proteins
    if genes[gene_id][rna_id][0].split('\t')[0] not in ('Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5'): continue
    
    print(gene_lines[gene_id])
    print('\n'.join(genes[gene_id][rna_id]))
    
