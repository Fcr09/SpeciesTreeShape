# Candidate Datasets & Methods

## Datasets

### Biological Datasets

#### Used in Improved Robustness paper:
- Plant data set from Morel et al.
- Avian (Neognathae + Palaeognathae) from Wu et al.
- Avian (Palaeognathae) from Cloutier et al.

#### In the GitHub of ASTRAL:
- 1KP (1000 plant)
- Song_mammals
- Song_primates

#### Used in ASTRAL-Pro paper:
- [A-pro_data](https://github.com/chaoszhang/A-pro_data)

#### Used in ASTRAL-constraint paper:
- Avian phylogenomic dataset

#### Used in DIscoVista paper:
- Dataset from "New deep-sea species of Xenoturbella and the position of Xenacoelomorpha"
- Dataset from "Xenacoelomorpha is the sister group to Nephrozoa"
- Dataset from "Phylotranscriptomic analysis of the origin and early diversification of land plants"

#### Used in TreeShrink paper:
6 multi-gene datasets and a single gene HIV dataset:
- Plants
- Insects
- Metazoa-Cannon and Rouse
- Mammals
- Frogs
- HIV

## Methods

### Mentioned in Improved Robustness paper:
- NJST
- ASTRID
- Weighted TREE-QMC
- Weighted ASTRAL/ASTER

### Other Notable Methods:
- **ASTRAL** (Accurate Species TRee ALgorithm): Estimates species trees from a set of gene trees by finding the tree that maximizes the number of shared quartets.
- **ASTER** (Species TRee estimation using Average Ranks of coalescences): Utilizes rank statistics from gene trees to estimate the species tree.
- **ASTRID** (Accurate Species TRees from Internode Distances): Constructs species trees using internode distances computed from gene trees.
- **BEAST**: A Bayesian framework for estimating species trees and divergence times using multilocus sequence data.
- **MP-EST** (Maximum Pseudo-likelihood Estimation of Species Trees): Estimates species trees by maximizing a pseudo-likelihood function based on gene tree topologies.
- **SVDquartets**: A method that uses singular value decomposition to estimate species relationships from sequence data without first estimating gene trees.
- **STAR** (Species Tree Analysis using Average Ranks): Estimates species trees by averaging the ranks of coalescence events across gene trees.
- **STEAC** (Species Tree Estimation using Average Coalescence times): Uses average coalescence times from gene trees to infer the species tree.
- **NJst** (Neighbor Joining for Species Trees): Applies neighbor-joining techniques to a distance matrix derived from gene trees.
- **SNAPP** (SNP and AFLP Phylogenies): A Bayesian method for inferring species trees directly from bi-allelic markers like SNPs.
- **BEST** (Bayesian Estimation of Species Trees): Estimates species trees using a Bayesian approach that accounts for gene tree heterogeneity.
- **GLASS** (Gene-tree/Species-tree Reconciliation Analysis): Infers species trees by reconciling gene tree differences due to duplication and loss events.
