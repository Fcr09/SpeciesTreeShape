import re

from Bio import Phylo
import sys

def newick_to_nexus(newick_file, nexus_file):
    # Read the Newick file
    with open(newick_file, 'r') as infile:
        trees = list(Phylo.parse(infile, 'newick'))
    
    taxa = [terminal.name for terminal in trees[0].get_terminals()]
    outgroup = taxa[-1]  # Assuming the last taxon is the outgroup
    ntaxa = len(taxa)
    ngene = len(trees)
    
    # Write the Nexus file
    with open(nexus_file, 'w') as outfile:
        # Write the data block
        outfile.write("Begin data;\n")
        outfile.write(f"    dimension ngene={ngene} ntaxa={ntaxa};\n")
        outfile.write(f"    Format tree=rooted outgroup={outgroup};\n")
        outfile.write("    matrix\n")
        for taxon in taxa:
            outfile.write(f"    {taxon} 1 {taxon}\n")
        outfile.write("    ;\n")
        outfile.write("End;\n\n")
        
        # Write the trees block
        outfile.write("Begin trees;\n")
        for tree in trees:
            outfile.write(tree.format('newick'))
        outfile.write("End;\n")

# Usage
input_file = '1KP-genetrees.tre'
output_file = 'nexus/1KP-genetrees.nexus'

newick_to_nexus(input_file, output_file)
