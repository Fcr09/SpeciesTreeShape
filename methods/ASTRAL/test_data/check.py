import sys
from Bio import Phylo

def check_newick(file_path):
    try:
        with open(file_path, 'r') as f:
            # Just reading the file to ensure it's accessible
            tree_str = f.read().strip()
        # Attempt to parse the Newick string
        trees = list(Phylo.read(file_path, 'newick'))
        print("The file contains a valid Newick tree.")
    except Exception as e:
        print("The file does not contain a valid Newick tree.")
        print("Error message:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_newick.py <newick_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    check_newick(file_path)
