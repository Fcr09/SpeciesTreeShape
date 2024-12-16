#!/usr/bin/env python3

from Bio import Phylo
from io import StringIO
import os

def check_basic_format(tree_str):
    """Check basic Newick format requirements"""
    issues = []
    
    # Check if string is empty
    if not tree_str.strip():
        issues.append("Empty tree string")
        return issues
    
    # Check for balanced parentheses
    open_count = tree_str.count('(')
    close_count = tree_str.count(')')
    if open_count != close_count:
        issues.append(f"Unbalanced parentheses: {open_count} opening vs {close_count} closing")
    
    # Check if ends with semicolon
    if not tree_str.strip().endswith(';'):
        issues.append("Tree string doesn't end with semicolon")
    
    # Check for unmatched quotes
    quote_count = tree_str.count('"')
    if quote_count % 2 != 0:
        issues.append("Unmatched quotes")
    
    return issues

def validate_tree_string(tree_str, tree_number):
    """Validate a single tree string"""
    has_issues = False
    
    # Basic format checks
    issues = check_basic_format(tree_str)
    if issues:
        has_issues = True
        print(f"\nTree #{tree_number} - Basic format issues:")
        for issue in issues:
            print(f"- {issue}")
    
    # Try parsing with Bio.Phylo
    try:
        tree = Phylo.read(StringIO(tree_str), 'newick')
    except Exception as e:
        has_issues = True
        if not issues:  # Only print tree number if not already printed
            print(f"\nTree #{tree_number} - Parsing error:")
        print(f"- {str(e)}")
        print(f"- First 100 chars: {tree_str[:100]}...")
    
    return has_issues

def validate_tree_file(filepath):
    """Validate all trees in the file"""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        issues_found = False
        for i, line in enumerate(lines, 1):
            tree_str = line.strip()
            if tree_str:  # Skip empty lines
                if validate_tree_string(tree_str, i):
                    issues_found = True
        
        if not issues_found:
            print("No issues found in any trees.")
            
    except Exception as e:
        print(f"Error reading file: {str(e)}")

def main():
    # Hardcoded file path
    filepath = "Lepidoptera_Micropterigoidea_Micropterigidae_Micropterix_calthella_Mica__N.tre"
    
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return
        
    validate_tree_file(filepath)

if __name__ == "__main__":
    main()
