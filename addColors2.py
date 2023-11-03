#!/usr/bin/env python

import sys


dictColors = {}


dictColors["haplotype1-0000043"] = "gold1"
dictColors["haplotype1-0000027"] = "burlywood"
dictColors["haplotype1-0000007"] = "gold1"
dictColors["haplotype1-0000030"] = "burlywood"
dictColors["haplotype1-0000050"] = "gold1"
dictColors["haplotype1-0000039"] = "burlywood"
dictColors["haplotype1-0000046"] = "gold1"
dictColors["haplotype1-0000044"] = "burlywood"
dictColors["haplotype1-0000004"] = "gold1"
dictColors["haplotype1-0000031"] = "burlywood"
dictColors["haplotype1-0000028"] = "gold1"
dictColors["haplotype1-0000042"] = "burlywood"
dictColors["haplotype1-0000035"] = "gold1"
dictColors["haplotype1-0000023"] = "burlywood"
dictColors["haplotype1-0000012"] = "gold1"
dictColors["haplotype1-0000033"] = "burlywood"
dictColors["haplotype1-0000013"] = "gold1"
dictColors["haplotype1-0000022"] = "burlywood"
dictColors["haplotype1-0000015"] = "gold1"
dictColors["haplotype1-0000001"] = "burlywood"


while True:
    szLine = sys.stdin.readline()
    if ( szLine == "" ):
        break

    aWords = szLine.split()
    
    szContig = aWords[0]
    if ( szContig in dictColors ):
        szColor = dictColors[ szContig ]
    else:
        szColor = "black"

    aWords.append( szColor )

    szNewLine = " ".join( aWords )

    sys.stdout.write( szNewLine + "\n" )


    
