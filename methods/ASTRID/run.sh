cd ../..
root_dir=$(pwd)
cd methods/ASTRID


# bazel-bin/src/ASTRID -i $root_dir/data/shen_animal.tre -o $root_dir/results/ASTRID/Shenanimal_Murine_Ref_Mus_20161116.tre

# bazel-bin/src/ASTRID -i $root_dir/data/shen_plant.tre -o $root_dir/results/ASTRID/Shenplant_Paulownia_tomentosa.tre

# bazel-bin/src/ASTRID -i $root_dir/data/shen_fungi.tre -o $root_dir/results/ASTRID/Shenfungi_Scer.tre

# bazel-bin/src/ASTRID -i $root_dir/data/song_mammals.424.gene.tre -o $root_dir/results/ASTRID/Songmammals_Platypus.tre

# bazel-bin/src/ASTRID -i $root_dir/data/zhang_pseudapis.tre -o $root_dir/results/ASTRID/Pseudapis_Lasioglossum_albipes.tre

bazel-bin/src/ASTRID -i $root_dir/data/zhang_papilionidae.tre -o $root_dir/results/ASTRID/Papilionidae_Choristoneura_fumiferana.tre

# bazel-bin/src/ASTRID -i $root_dir/data/zhang_cetacean.tre -o $root_dir/results/ASTRID/Cetacean_Bacu.tre

# bazel-bin/src/ASTRID -i $root_dir/data/avian_uce_trees_3679.tre -o $root_dir/results/ASTRID/Avianuce_TINMA.tre

