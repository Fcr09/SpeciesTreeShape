import re
import os

def load_mapping(mapping_file):
    # Create both forward and reverse mappings
    id_to_name = {}
    with open(mapping_file, 'r') as f:
        # Skip header line
        next(f)
        for line in f:
            name, id_num = line.strip().split('\t')
            id_to_name[id_num] = name
    return id_to_name

def process_tree(tree_str, id_to_name):
    # Regular expression to find species IDs:
    # - Must be a whole number (no decimal point)
    # - Must be followed by : or ) or ,
    # - Must not be preceded by ) or ] (support values)
    # - Must not be followed by numbers (branch lengths)
    pattern = r'(?<![\)\]])(\d+)(?=(?:\.|:|\)|,))'
    
    def replace_id(match):
        id_num = match.group(1)
        # Only replace if it's in our mapping (i.e., it's a species ID)
        return id_to_name[id_num] if id_num in id_to_name else id_num
    
    # Replace each ID with its original species name
    return re.sub(pattern, replace_id, tree_str)

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths relative to script location
    input_file = os.path.join(script_dir, "Lepidoptera_output.tre")
    output_file = os.path.join(script_dir, "Lepidoptera_remapped.tre")
    mapping_file = os.path.join(script_dir, "species_id_mapping.txt")
    
    # Load the ID to name mapping
    id_to_name = load_mapping(mapping_file)
    
    # Process the tree file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Process each tree (line) and write to output file
            remapped_tree = process_tree(line.strip(), id_to_name)
            outfile.write(remapped_tree + '\n')

if __name__ == "__main__":
    main()
