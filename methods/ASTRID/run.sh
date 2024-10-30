cd ../..
root_dir=$(pwd)
cd methods/ASTRID
bazel-bin/src/ASTRID -i $root_dir/data/avian_uce_trees_3679.tre -o $root_dir/results/ASTRID/avian_uce_trees_3679.tre