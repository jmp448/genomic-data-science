#!/bin/bash
#SBATCH --job-name=countSNPcands
#SBATCH --time=0:20:0
#SBATCH --output=slurm_output/SNPcount.out
#SBATCH --error=slurm_output/SNPcount.err
#SBATCH --mem=5G
#SBATCH --mail-user=jpopp4@jhu.edu

module load python/3.7-anaconda

python eqtlcounter.py
