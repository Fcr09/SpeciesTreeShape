#!/usr/bin/env Rscript

library('ape')
library('treebalance')
library('readr')

get_root_from_filename <- function(method, dataset) {
  # Get list of files in the method directory
  files <- list.files(path = file.path("../results", method), pattern = "\\.tre$", full.names = FALSE)
  
  # Find the file that matches the pattern: dataset_*.tre
  pattern <- paste0("^", dataset, "_.*\\.tre$")
  matching_file <- files[grep(pattern, files)]
  
  if (length(matching_file) == 0) {
    stop("No matching file found")
  }
  
  # Extract the root (text between first underscore and .tre)
  root <- sub(paste0("^", dataset, "_(.+)\\.tre$"), "\\1", matching_file)
  
  return(list(
    filename = matching_file,
    root = root
  ))
}

get_statistics <- function(method, dataset) {
  result <- get_root_from_filename(method, dataset)
  file_name <- result$filename
  file_path <- file.path("../results", method, file_name)
  root <- result$root

  text <- read_file(file_path)
  tree <- ape::read.tree(text=text)

  rooted_tree <- ape::root(tree, root, resolve.root=TRUE)

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
  # Create directory if it doesn't exist
  dir.create(file.path("../metrics", dataset), recursive = TRUE, showWarnings = FALSE)

  # Write JSON file
  jsonlite::write_json(balance_indices, sprintf("../metrics/%s/%s.json", dataset, method), pretty=TRUE)
  cat("----------------------------------------\n")
}

# Move these outside the function
datasets <- c("Avianuce", "Cetacean", "Lepidoptera", "Papilionidae", "Pseudapis", "Seedplantbackbone", "Shenanimal", "Shenfungi", "Shenplant", "Songmammals", "UCEminus105")

# Calculate and save tree balance statistics for each dataset and method
methods <- c("ASTER", "TreeQMC", "ASTRAL-III", "ASTRID")

# Create error log file
error_log <- file("error_log.txt", "w")

for (dataset in datasets) {
  for (method in methods) {
    tryCatch({
      get_statistics(method, dataset)
    }, error = function(e) {
      error_msg <- sprintf("Error processing dataset: %s, method: %s\n", dataset, method)
      cat(error_msg)
      # Write error to log file
      writeLines(error_msg, error_log)
    })
  }
}

# Close error log file
close(error_log)

