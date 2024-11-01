# Candidate Datasets & Methods

## Datasets

### Biological Datasets

#### Used in Shen et al.:
- Dissecting incongruence between concatenation- and quartet-based approaches in phylogenomic data

#### Used in Improved Robustness paper:
- Plant dataset from Morel et al. (2019)
- Avian dataset (Neognathae + Palaeognathae) from Wu et al. (2018)
- Avian dataset (Palaeognathae) from Cloutier et al. (2019)

#### Available in ASTRAL GitHub repository:
- 1KP (1000 plant transcriptome dataset)
- Song_mammals (37 mammalian species, 442 genes)
- Song_primates (subset of Song_mammals with 9 primates, tree shrews, and 4 other mammalian taxa)

#### Used in ASTRAL-Pro paper:
- [A-pro_data](https://github.com/chaoszhang/A-pro_data) (datasets for gene tree estimation with paralogs)

#### Used in ASTRAL-constraint paper:
- Avian phylogenomic dataset (Jarvis et al. 2014, 48 species, 14,446 loci)

#### Used in DIscoVista paper:
- Dataset from Rouse et al. (2016): "New deep-sea species of Xenoturbella and the position of Xenacoelomorpha"
- Dataset from Cannon et al. (2016): "Xenacoelomorpha is the sister group to Nephrozoa"
- Dataset from Wickett et al. (2014): "Phylotranscriptomic analysis of the origin and early diversification of land plants"

#### Used in TreeShrink paper:
Six multi-gene datasets and a single gene HIV dataset:
- Plants (103 species, 424 genes)
- Insects (144 species, 1,478 genes)
- Metazoa-Cannon and Rouse (77 species, 212 genes)
- Mammals (37 species, 442 genes)
- Frogs (156 species, 95 genes)
- HIV (648 sequences)

## Methods

### Mentioned in Improved Robustness paper:
- NJST (Neighbor Joining Species Tree)
- ASTRID (Accurate Species TRee from Internode Distances)
- Weighted TREE-QMC (Weighted Tree Quartet MaxCut)
- Weighted ASTRAL/ASTER

### Other Notable Methods:
- **ASTRAL** (Accurate Species TRee ALgorithm): Estimates species trees from gene trees by maximizing the number of shared quartets.
- **ASTER** (Accurate Species Tree EstimatoR): Utilizes rank statistics from gene trees to estimate the species tree.
- **ASTRID** (Accurate Species TRees from Internode Distances): Constructs species trees using internode distances computed from gene trees.
- **BEAST** (Bayesian Evolutionary Analysis Sampling Trees): A Bayesian framework for estimating species trees and divergence times using multilocus sequence data.
- **MP-EST** (Maximum Pseudo-likelihood Estimation of Species Trees): Estimates species trees by maximizing a pseudo-likelihood function based on gene tree topologies.
- **SVDquartets**: Uses singular value decomposition to estimate species relationships from sequence data without first estimating gene trees.
- **STAR** (Species Tree estimation using Average Ranks): Estimates species trees by averaging the ranks of coalescence events across gene trees.
- **STEAC** (Species Tree Estimation using Average Coalescence times): Uses average coalescence times from gene trees to infer the species tree.
- **NJst** (Neighbor Joining for Species Trees): Applies neighbor-joining techniques to a distance matrix derived from gene trees.
- **SNAPP** (SNP and AFLP Phylogenies): A Bayesian method for inferring species trees directly from bi-allelic markers like SNPs.
- **BEST** (Bayesian Estimation of Species Trees): Estimates species trees using a Bayesian approach that accounts for gene tree heterogeneity.
- **GLASS** (Gene-tree/Species-tree Reconciliation Analysis): Infers species trees by reconciling gene tree differences due to duplication and loss events.
