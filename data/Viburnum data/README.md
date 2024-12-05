These files are needed to run the RevBayes scripts located in `../code/`. The file `../code/run_quick.Rev` controls exactly which input files are used and how they're used. The Supplementary Information document hosted on Dryad contains rich descriptions of how each dataset was generated. A brief description of the data files:

- `viburnum.range.n6.nex` contains the 6-region range data. Note that these are integer-coded states, because we wanted to allow for ambiguous ranges for some fossil taxa; see RevBayes tutorials on biogeography to use presence-absence ranges. (Supplements 1 & 5)
- `viburnum.biome.n4.nex` contains the 4-biome state data. (Supplements 1 & 5)
- `viburnum.backbone.tre` contains the Stage 1 RAD-seq topology constraint and the morphological constraints for the 10 unsequenced, extant taxa (Supplement 2)
- `viburnum.mol.nex` contains the cpDNA + ITS sequence alignment (Supplement 3)
- `viburnum.init.tre` contains a reasonable starting tree to speed up mixing
- `viburnum.fossil_intervals.tsv` contains the age ranges for fossil taxa (Supplement 5)
- `viburnum.taxa.tsv` contains all taxon labels and fossil taxon ages (Supplement 5)
- `viburnum.area_graph.n6.*.csv` contains the adjacencies among areas over time (Supplement 6)
- `viburnum.bg.times.txt` contains the times for applying each area-graph (Supplement 6)
