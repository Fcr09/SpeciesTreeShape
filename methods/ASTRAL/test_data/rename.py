import re

def extract_names(tree_str):
    # Regular expression to find species names in Newick format
    pattern = r'([A-Za-z_]+[A-Za-z0-9_*]*?)(?=:|,|\))'
    return set(re.findall(pattern, tree_str))

def process_tree(tree_str, name_to_id):
    # Regular expression to find species names in Newick format
    pattern = r'([A-Za-z_]+[A-Za-z0-9_*]*?)(?=:|,|\))'
    
    def replace_name(match):
        return str(name_to_id[match.group(1)])
    
    # Replace each species name with its ID
    return re.sub(pattern, replace_name, tree_str)

def main():
    input_file = "Lepidoptera.tre"
    output_file = "Lepidoptera_numbered.tre"
    mapping_file = "species_id_mapping.txt"
    
    # First pass: collect all unique species names
    all_names = set()
    with open(input_file, 'r') as infile:
        for line in infile:
            names = extract_names(line.strip())
            all_names.update(names)
    
    # Create mapping from names to integers
    name_to_id = {name: i+1 for i, name in enumerate(sorted(all_names))}
    
    # Save the mapping to a file
    with open(mapping_file, 'w') as mapfile:
        mapfile.write("Original_Name\tID\n")
        for name, id_num in sorted(name_to_id.items()):
            mapfile.write(f"{name}\t{id_num}\n")
    
    # Second pass: replace names with IDs
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Process each tree (line) and write to output file
            numbered_tree = process_tree(line.strip(), name_to_id)
            outfile.write(numbered_tree + '\n')

if __name__ == "__main__":
    main()
