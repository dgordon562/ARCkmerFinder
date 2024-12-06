# ARCkmerFinder

To run the pipeline:
mkdir (empty new directory)
cd (that directory)
git clone git@github.com:dgordon562/ARCkmerFinder.git .
edit config.yaml
run_snakemake.sh
edit datasets_to_add.fof
edit datasets_to_subtract.fof

     

summary of this pipeline:

There are 2 ways of running the pipeline:
1) when the meryl databases already exist
2) when the meryl databases do not already exist

In the latter case it will take a set of reads (such as for an
archaic) and make a meryl database (B) of the kmers of each archaic.  (It
does have the possibility of having several archaics at once.)  It
makes meryl databases of several african read sets (C).  Then it makes a
meryl database of the union of the archaics and, one at a time (D),
subtracts the meryl databases from each african.  So if a kmer exists
in both the archaic and in one of the africans, it is not in the final
meryl database (E).  If it just exists in the africans, it is not in the
final.  It is only in the final database if it is in the archaic and
not in the african.  Thus it probably includes no kmers found in
repeats because those repeats will be in one of the africans (or both
of them).

Then it will be go through this meryl database and remove any kmer
that has a count of 5 (default) or less (F).  The rationale is that these are errors
in the reads.  With a depth of coverage of, say 100, kmers should be
found roughly 100 times--not 5 times.  This is the final filtered
meryl database and it is used for the rest of the pipeline.

If this database already exists, it is specified in the config.yaml
file.  (There are a number of other flags that must be set as well to
prevent the pipeline from trying to recreated this meryl database.
This is currently under development.)

Enter an assembly (G):  for each kmer in the assembly, check if it is in
the filtered database.  Meryl-lookup gives a wig file (I) which I convert
to a bed file (J) in which each kmer is a single line (obviously this is a
huge bed file).  There are several other columns in the bed file which
are not used.

An fai file is made for the assembly and from this a set of windows
(nonoverlapping) spans the genome(H).  Each window is 2kb (default)
except, of course, for the final window in each contig.  Some fancy
bedtools assigns each line in J (above) to a 2k window here giving an
enormouse (300M) file (N) in which each kmer in the assembly has its
location and also which 2k window it is in, and then I count how many
such lines there are in each 2k window.

The # of distinct kmers (AAAA is counted once no matter how many AAAA
are in the reads) is counted for each meryl dataset.  (K) This takes a
very long time.  It is used for the curve which I use for deciding how
small a kmer frequency should be considered an error. (L)

makeHistogramPrerequisites.py combines the # of kmers in each 2kb
window, the list of windows across the genome, and a bed file of
putative introgressed regions, and gives:

szWindowsAcrossGenomeWithZeroAndNonZeroMatchingKmersAndIncludingIntrogressedAndNoIntrogressedRegions = "windows_across_genome_with_zero_and_nonzero_matching_kmers_and_including_introgressed_and_no_introgressed_regions.bed"

This file is used to make 3 histograms (M)




Files in the above description:
B:  these are listed in datasets_to_add.fof such as /panfs/jay/groups/7/hsiehph/shared/hsiehph_shared/short_read/ARC/meryl_databases/Chagyrskaya.meryl
C:  these are listed in datasets_to_subtract.fof
for example:
/panfs/jay/groups/7/hsiehph/shared/hsiehph_shared/short_read/BAM_HPRCandMEL/HG03516.final2.fq.gz /panfs/jay/groups/7/hsiehph/shared/hsiehph_shared/short_read/BAM_HPRCandMEL/meryl_databases/HG03516.meryl
/panfs/jay/groups/7/hsiehph/shared/hsiehph_shared/short_read/BAM_HPRCandMEL/HG02818.final.fq.gz /panfs/jay/groups/7/hsiehph/shared/hsiehph_shared/short_read/BAM_HPRCandMEL/meryl_databases/HG02818.meryl
D:  these are called intermediate1.meryl intermediate2.meryl etc
E:  to_find_minus_to_remove.meryl
F:  to_find_minus_to_remove.meryl_no_5_low_freq_kmers.meryl
G:  specified in config["assembly"]
H:  assembly.haplotype1.bed is just a bed file of the contigs, 1 line per contig
    assembly.haplotype1_2000_windows.bed is a bed file of 2kb
    (nonoverlapping) windows spanning the contigs
I:  assembly.haplotype1_to_find_minus_to_remove.meryl_no_5_low_freq_kmers.wig    
J:  szKmerCountBed or assembly.haplotype1_to_find_minus_to_remove.meryl_no_5_low_freq_kmers.bed
K: HG02818.counts HG02818.counts.txt Altai.counts Altai.counts.txt
   where the *.counts gives (I believe) the # of kmers (such as AAAA)
   which occur 1 time, 2 times, 3 times, ... and *.counts.txt gives the
   number of distinct kmers (such as AAAA) in the database.
L: count_of_frequencies_all.txt count_of_frequencies_all.png
kmers_not_counting_repeats_before_removing_low_occurrence_kmers.txt counts each kmer in the subtractred meryl database.  
N:  szKmerCountBedWithWindow or assembly.haplotype1_to_find_minus_to_remove.m\
eryl_no_5_low_freq_kmers.bed_with_window

what is the relation of szKmerCountInWindows and szWindowsAcrossGenomeWithZeroAndNonZeroMatchingKmersAndIncludingIntrogressedAndNoIntrogressedRegions

assembly.haplotype1_to_find_minus_to_remove.meryl_no_5_low_freq_kmers_in_2000_windows.bed
has no windows with no kmers


This is the most important output:

szWindowsAcrossGenomeWithZeroAndNonZeroMatchingKmersAndIncludingIntrogressedAndNoIntrogressedRegions = "windows_across_genome_with_zero_and_nonzero_matching_kmers_and_including_introgressed_and_no_introgressed_regions.bed"

windows_across_genome_with_zero_and_nonzero_matching_kmers_and_including_introgressed_and_no_introgressed_regions.bed


M:
Altai_minus_HG03516_HG02818_logx_histogram.png
Altai_minus_HG03516_HG02818_histogram.png
Altai_minus_HG03516_HG02818_with_limit_histogram.png



meryl print looks like this:
```
AAAAAAAAAAAAAAAAAAAAA   1564811
AAAAAAAAAAAAAAAAAAAAC   65845
.
.
.
```
where the number is the # of times the given kmer is found in the
read dataset.
The number of lines is the number of distinct kmers.  The 2nd column 
is irrelevant.
But if awk '{print $2}' | sort -n | uniq -c
then it will look like this:
```
2073056792 1
89240217 2
19355034 3
8221172 4
which means 
2073056792 kmers that occur 1 time in the read dataset
89240217 kmers that occur 2 times in the read dataset
etc.
```
so the sum of the 1st column gives the number of distinct kmers.
(the sum of the product of the 1st and 2nd columns gives the number
of (nondistinct) kmers in the read dataset, but we aren't using that
number for anything)

szKmerCountInWindows has a number, for each 20kb window, of kmers from
PNG16_vs_Chagyrskaya_minus_HG03516_greater_than_5.  If a kmer is found
more than once in the 20kb window, it is counted more than once?  Yes.
meryl-lookup notes for each kmer, how many times it is found in the
reads (by the meryl database).  But that count is ignored by this
pipeline.  Each kmer found is assigned to a 20kb window.  bedtools
groupby then counts how many kmers for each 20kb are found in the
meryl database.  Some of these kmers may be the same.  We don't know
and don't care.  Just how many kmers in each 20kb region are found in
the meryl database.



