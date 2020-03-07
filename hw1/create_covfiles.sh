covfile=/work-zfs/abattle4/lab_data/GTEx_v8_eqtl_practice/matrix_eqtl/Whole_Blood.v8.covariates.txt

# Covariate file 1: genotype PCs and sex only
cat $covfile | head -n 6 > cov1.txt
cat $covfile | tail -n 1 >> cov1.txt

# Covariate file 2: genotype PCs, sex, and 5 expression PCs
