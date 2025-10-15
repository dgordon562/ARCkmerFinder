# Check if the number of arguments ($#) is not equal to 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <jellyfish .tvf file>" >&2
    exit 1
fi

# If the script reaches this point, the argument is present.
JELLYFISH_HISTOGRAM_FILE="$1"

module load R/4.4.0-openblas-rocky8
Rscript genomescope.R $JELLYFISH_HISTOGRAM_FILE 21 150 plots_dir

module load python/3.6.3
./where_do_curves_cross.py
