#!/bin/bash
#SBATCH --job-name=matrixeqtl
#SBATCH --time=1:0:0
#SBATCH --output=slurm_output/qtl.out
#SBATCH --error=slurm_output/qtl.err
#SBATCH --mail-user=jpopp4@jhu.edu
#SBATCH --partition=shared
#SBATCH --mem=50G

module load R

Rscript ../code/transeqtl.R
