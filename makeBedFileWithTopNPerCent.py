#!/usr/bin/env python


import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--szInputBedFileWithNonZero20kbRegions", required = True )
# this is necessary because the argument above doesn't include regions
# that have 0 kmers
parser.add_argument("--szBedFileOfAll20kbRegions", required = True )
parser.add_argument("--szOutputBedFile", required = True )
parser.add_argument("--fTopPercent", required = True, type = float )
args = parser.parse_args()



# get nTotal20KbRegions

szCommand = "wc -l " + args.szBedFileOfAll20kbRegions + " | awk '{print $1}' "
print( "about to execute: " + szCommand )
nTotalWindows = int( subprocess.check_output( szCommand, shell = True ) )

# round
nLineNumberOfTopOnePerCent = int( nTotalWindows * args.fTopPercent / 100 + 0.5 )
print( f"nTotalWindows = {nTotalWindows} nLineNumberOfTopOnePerCent = {nLineNumberOfTopOnePerCent}" )


szCommand = "wc -l " + args.szInputBedFileWithNonZero20kbRegions + " | awk '{print $1 }' "
print( "about to execute: " + szCommand )
nWindowsWithNonZeroCounts = int( subprocess.check_output( szCommand, shell = True ) )

# this will occur if there are less than 100 20kb regions in the genome, i.e. if the
# genome is smaller than 2Mb
if ( nLineNumberOfTopOnePerCent < 1 ):
    nLineNumberOfTopOnePerCent = 1


if ( nLineNumberOfTopOnePerCent > nWindowsWithNonZeroCounts ):
    sys.exit( "1% of " + str( nTotalWindows ) + " is " + str( nLineNumberOfTopOnePerCent ) + " but there are only " + str( nWindowsWithNonZeroCounts ) + " windows with non-zero counts so the 1% value is 0" )

szCommand = "cat " + args.szInputBedFileWithNonZero20kbRegions + " |  awk '{print $4}' | sort -nr | sed -n " + str( nLineNumberOfTopOnePerCent ) + "p"
print( "about to execute: " + szCommand )
nMinValueOnePerCentile = int( subprocess.check_output( szCommand, shell = True ) )

with open( args.szInputBedFileWithNonZero20kbRegions, "r" ) as fBedFileOfNonZeroRegions, open( args.szOutputBedFile, "w" ) as fBedFileOfTopOnePerCent:
    while True:
        szLine = fBedFileOfNonZeroRegions.readline()
        if ( szLine == "" ):
            break

        aWords = szLine.split()
        # looks like:
        #test_assembly1   0       475     35
        # 0               1        2      3

        nNumberOfKmersInRegion = int( aWords[3] )

        if ( nNumberOfKmersInRegion >= nMinValueOnePerCentile ):
            fBedFileOfTopOnePerCent.write( szLine )


