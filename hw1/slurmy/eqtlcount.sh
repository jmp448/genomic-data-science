#!/bin/bash
#SBATCH --job-name=countQTL1
#SBATCH --time=0:10:0
#SBATCH --output=slurm_output/QTLcount1.out
#SBATCH --error=slurm_output/QTLcount1.err
#SBATCH --mem=5G
#SBATCH --mail-user=jpopp4@jhu.edu

module load python/3.7-anaconda

python eqtlcounter.py
