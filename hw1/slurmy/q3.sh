#!/bin/bash
#SBATCH --job-name=q3
#SBATCH --time=0:20:0
#SBATCH --output=slurm_output/q3.out
#SBATCH --error=slurm_output/q3.err
#SBATCH --mem=25G
#SBATCH --partition=shared
#SBATCH --mail-user=jpopp4@jhu.edu

module load R

Rscript eqtl.R
