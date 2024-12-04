#!/usr/bin/env Rscript

library('ape')
library('treebalance')
library('readr')

method <- "ASTRID"
dataset <- "Shenanimal_Murine_Ref_Mus_20161116"

# Read tree from file
tree_file <- sprintf("../results/%s/%s.tre", method, dataset)
text <- read_file(tree_file)
tree <- ape::read.tree(text=text)

# # Print tree labels to check available nodes
# print("Available tree labels:")
# print(tree$tip.label)

# Root the tree at the first tip label instead of "0"
rooted_tree <- ape::root(tree, 'Murine_Ref_Mus_20161116', resolve.root=TRUE)
# rooted_tree <- tree
# Make tree binary (resolve polytomies randomly)
# rooted_tree <- ape::multi2di(rooted_tree)

# Calculate balance indices

rquartet <- rQuartetI(rooted_tree)        # Rooted quartet index
sackin <- sackinI(rooted_tree)            # Sackin index
colless <- collessI(rooted_tree)          # Colless index
b1 <- B1I(rooted_tree)                    # B1 index
b2 <- B2I(rooted_tree)                    # B2 index
avgdepth <- avgLeafDepI(rooted_tree)      # Average leaf depth
avgvertdepth <- avgVertDep(rooted_tree)   # Average vertex depth
maxdepth <- maxDepth(rooted_tree)         # Maximum depth of the tree
maxwidth <- maxWidth(rooted_tree)         # Maximum width of the tree
stairs1 <- stairs1(rooted_tree)           # Stairs1 index
stairs2 <- stairs2(rooted_tree)           # Stairs2 index
symnodes <- symNodesI(rooted_tree)        # Symmetry nodes index
totcoph <- totCophI(rooted_tree)          # Total cophenetic index

# Print results
cat(sprintf("Rooted quartet index: %f\n", rquartet))
cat(sprintf("Sackin index: %f\n", sackin)) 
cat(sprintf("Colless index: %f\n", colless))
cat(sprintf("B1 index: %f\n", b1))
cat(sprintf("B2 index: %f\n", b2))
cat(sprintf("Average leaf depth: %f\n", avgdepth))
cat(sprintf("Average vertex depth: %f\n", avgvertdepth))
cat(sprintf("Maximum depth: %f\n", maxdepth))
cat(sprintf("Maximum width: %f\n", maxwidth))
cat(sprintf("Stairs1 index: %f\n", stairs1))
cat(sprintf("Stairs2 index: %f\n", stairs2))
cat(sprintf("Symmetry nodes index: %f\n", symnodes))
cat(sprintf("Total cophenetic index: %f\n", totcoph))

# Create a list of balance indices
balance_indices <- list(
  rooted_quartet = rquartet,
  sackin = sackin,
  colless = colless,
  b1 = b1,
  b2 = b2,
  avg_leaf_depth = avgdepth,
  avg_vertex_depth = avgvertdepth,
  max_depth = maxdepth,
  max_width = maxwidth,
  stairs1 = stairs1,
  stairs2 = stairs2,
  symmetry_nodes = symnodes,
  total_cophenetic = totcoph
)

# Convert to JSON and write to file
dataset <- "Shen_animal"
jsonlite::write_json(balance_indices, sprintf("../metrics/%s/%s.json", dataset, method), pretty=TRUE)
