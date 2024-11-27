#!/bin/bash

NTAX=$1
HGHT=$2
RATE=$3
REPL=$4
SUPP=$5
NGEN=$6

MODL="model.$NTAX.$HGHT.$RATE"
MYMODL="$NTAX,$HGHT,$RATE,$REPL,$SUPP,$NGEN"

# Define directories
GROUPDIR="/fs/cbcb-lab/ekmolloy"
PROJDIR="$GROUPDIR/ekmolloy/tree-qmc-study/han2024wtreeqmc"

# Define software
GETSHAPE="$PROJDIR/tools/compare_branch_support.py"
GETSHAPE="../../../../tools/compute_balance_index.R"

# Define input files
DATADIR="$PROJDIR/data/mirarab2015astral2-extsim/$MODL/$REPL"
DATADIR="../../data/mirarab2015astral2-extsim/$MODL/$REPL"

cd $DATADIR

MYSTRE="s_tree.trees"
if [ ! -e true_stree_shape.csv ]; then
    TSHAPE=$(Rscript $GETSHAPE $MYSTRE)
    TSHAPE=$(echo ${TSHAPE[@]} | awk '{print $2","$3}' | tr -d '"')
    echo "$NTAX,$HGHT,$RATE,$REPL,NA,NA,true_stree,$TSHAPE" > true_stree_shape.csv
fi

MYSTRE="caml_sh_${NGEN}gen"
if [ ! -e ${MYSTRE}_shape.csv ]; then
    TSHAPE=$(Rscript $GETSHAPE $MYSTRE.tre)
    TSHAPE=$(echo ${TSHAPE[@]} | awk '{print $2","$3}' | tr -d '"')
    echo "$NTAX,$HGHT,$RATE,$REPL,NA,$NGEN,caml,$TSHAPE" > ${MYSTRE}_shape.csv
fi

MTHDS=( "aster_h_t16" \
        "wastrid_s" \
        "wtreeqmc_wh_n2" )

for MYMTHD in ${MTHDS[@]}; do
    MYSTRE="${MYMTHD}_${SUPP}_${NGEN}gen"
    if [ ! -e ${MYSTRE}_shape.csv ]; then
        TSHAPE=$(Rscript $GETSHAPE $MYSTRE.tre)
        TSHAPE=$(echo ${TSHAPE[@]} | awk '{print $2","$3}' | tr -d '"')
        echo "$MYMODL,$MYMTHD,$TSHAPE" > ${MYSTRE}_shape.csv
    fi
done
