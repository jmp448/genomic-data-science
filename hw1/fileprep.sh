expfile=/work-zfs/abattle4/lab_data/GTEx_v8_eqtl_practice/matrix_eqtl/Whole_Blood.v8.normalized_expression.txt

# get a file with just the gtex ids
head -n1 < $expfile | tr -s '\t'  '\n' | awk '{if (NR != 1) print}' > data/gtex.ids.txt

# get a file with just the gene ids
awk '{if (NR != 1) print $1}' < $expfile > data/gene.ids.txt

# get a file with just the expression data
cut -f1 --complement $expfile | awk '{if (NR != 1) print}' > data/exp.data.txt
