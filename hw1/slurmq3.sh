#SBATCH --job-name=q3
#SBATCH --time=0:20:0
#SBATCH --output=q3.out
#SBATCH --error=q3.err

module load R

Rsource eqtl.R
