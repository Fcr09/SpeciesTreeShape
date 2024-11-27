library(ggtree)
library(ggplot2)

# Define common plot style
tree_style <- list(
  geom_tiplab(size=3),
  theme_tree2(),
  theme(
    plot.margin = margin(20, 20, 20, 20),
    text = element_text(size=14),
    legend.position = "none"
  )
)

# Create plots for both ASTRAL and ASTRID trees
methods <- c("ASTRAL", "ASTRID")
plots <- list()

for (method in methods) {
  # Read tree file
  tree_file <- sprintf("../results/%s/1KP-speciestrees.tre", method)
  tree <- read.tree(tree_file)
  
  # Create plot with common style, setting edge.length to NULL to avoid NA warnings
  p <- ggtree(tree, branch.length='none') + tree_style
  
  # Save plot
  output_file <- sprintf("1KP_species_tree_%s.pdf", tolower(method))
  ggsave(output_file, p, width=24, height=16)
  
  plots[[method]] <- p
}
