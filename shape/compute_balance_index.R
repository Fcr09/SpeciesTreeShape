#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)

library('ape')
library('treebalance')
library('readr')

text <- read_file(args)
tree <- ape::read.tree(text=text)
rooted_tree <- ape::root(tree, "0", resolve.root=TRUE)
#write.tree(rooted_tree)
#plot(rooted_tree)
x <- rQuartetI(rooted_tree)
y <- avgLeafDepI(rooted_tree)
print(paste(x, " ", y, sep=""))
