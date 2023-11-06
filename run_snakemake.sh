#!/usr/bin/bash -l

conda activate snakemake


snakemake -s ideogram_of_kmers_found.snake --jobname "{rulename}.{jobid}" --profile profile -w 60 --jobs 50 -p -k
