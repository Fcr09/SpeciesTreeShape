import re

def count_species(tree_file):
    # Read the file content
    with open(tree_file, 'r') as f:
        content = f.read()
    
    # Regular expression to match species names (Format: Name_name_Family)
    species_pattern = r'([A-Z][a-z]+_[a-z]+_[A-Z][a-z]+)'
    
    # Find all matches
    species = set(re.findall(species_pattern, content))
    
    # Print results
    print(f"Total unique species found: {len(species)}")
    # print("\nList of species:")
    # for s in sorted(species):
    #     print(s)
    
    return species

# Use the function
species = count_species('Feng_frog_bootstrap.tre')
