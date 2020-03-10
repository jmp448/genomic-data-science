#!/bin/bash
#SBATCH --job-name=q4
#SBATCH --time=0:30:0
#SBATCH --output=slurm_output/q4.out
#SBATCH --error=slurm_output/q4.err
#SBATCH --mail-user=jpopp4@jhu.edu
#SBATCH --partition=shared
#SBATCH --mem=5G

module load R

srun Rscript eqtl_cov_input.R "cov1" 0
srun Rscript eqtl_cov_input.R "cov2" 1
srun Rscript eqtl_cov_input.R "cov3" 2
srun Rscript eqtl_cov_input.R "cov4" 3
srun Rscript eqtl_cov_input.R "cov5" 4
wait
