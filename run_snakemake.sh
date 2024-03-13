#!/usr/bin/bash -l


#SBATCH --time=48:00:00
#SBATCH --mem=30g
#SBATCH --cpus-per-task=1

source /panfs/jay/groups/7/hsiehph/shared/bin/initialize_conda.sh
conda activate snakemake


snakemake -s ARCkmerFinder.snake --jobname "{rulename}.{jobid}" --profile profile -w 60 --jobs 50 -p -k
