#!/bin/bash
#SBATCH --job-name=q4
#SBATCH -N 5
#SBATCH -n 5
#SBATCH -c 1
#SBATCH --time=0:20:0
#SBATCH --output=slurm_output/q4.out
#SBATCH --error=slurm_output/q4.err
#SBATCH --mem-per-node=5G
#SBATCH --mail-user=jpopp4@jhu.edu

module load R

srun -N 1 -n 1 Rscript eqtl_cov_input.R "cov1" 0 &
srun -N 1 -n 1 Rscript eqtl_cov_input.R "cov2" 1 &
srun -N 1 -n 1 Rscript eqtl_cov_input.R "cov3" 2 &
srun -N 1 -n 1 Rscript eqtl_cov_input.R "cov4" 3 &
srun -N 1 -n 1 Rscript eqtl_cov_input.R "cov5" 4 &
wait
