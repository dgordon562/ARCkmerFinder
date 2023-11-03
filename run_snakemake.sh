#!/usr/bin/bash -l

conda activate snakemake


snakemake -s ideogram_of_kmers_found.snake -j 2
