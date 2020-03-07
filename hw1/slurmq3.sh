#!/bin/bash
#SBATCH --job-name=q3
#SBATCH --time=0:20:0
#SBATCH --output=q3.out
#SBATCH --error=q3.err
#SBATCH --mail-user=jpopp4@jhu.edu

module load R

Rscript eqtl.R
