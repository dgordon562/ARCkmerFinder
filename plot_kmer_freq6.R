options( echo = TRUE )

library( ggplot2 )
library("RColorBrewer") 

args <- commandArgs(trailingOnly = TRUE)
szTitle <- args[1]
szInputFile <- args[2]
szOutputFile <- args[3]


png( szOutputFile, height = 600, width = 1000 )


df <- read.table( szInputFile, header = FALSE )

# looks like:
# 2073056792 1
# 89240217 2
# 19355034 3
# which means there are 2073056792 that occur once



bp <- ggplot(data=df, aes(x=V2, y=V1, col = V3 ) )

bp <- bp + geom_point(alpha = 0.8, shape = 1 )
x_breaks = c(1, 10, 100, 1000, 10^4, 10^5, 10^6, 10^7, 10^8 )                                                               
y_breaks = c(1, 10, 100, 1000, 10^4, 10^5, 10^6, 10^7, 10^8, 10^9 )

bp <- bp + scale_y_log10( breaks = y_breaks ) + scale_x_log10( breaks = x_breaks )

bp <- bp + xlab( "kmer frequency" )
bp <- bp + ylab( "# of kmers with given frequency" )
bp <- bp + ggtitle( szTitle )

bp <- bp + theme(plot.title = element_text(size=22), axis.title =
element_text( size = 18 ), axis.text = element_text( size = 16 ) )

#bp <- bp + scale_colour_brewer()

bp

dev.off()

