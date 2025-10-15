#!/usr/bin/env python

nErrorsAreGreater = 1
nPredictedIsGreater = 2
nStarting = 3

nState = nStarting


with open( "plot_data_output.txt", "r" ) as fTable:
    bHeaderLine = True
    nChangedAtThisX = -666
    for szLine in fTable.readlines():
        if ( bHeaderLine ):
            # X_Value Predicted_Value Error_Kmers
            bHeaderLine = False
            continue
        
        aWords = szLine.split()
        # looks like:
        # 1       31647.880986645 2987012423.11901
        # 2       151746.209803167        80006808.7901968

        fPredictedValue = float( aWords[1] )
        fErrorKmers = float( aWords[2] )

        bErrorsGreater = fErrorKmers > fPredictedValue
        if ( nState == nStarting ):
            if ( not bErrorsGreater ):
                exit( "something wrong:  started out without errors being greater" )

            nState = nErrorsAreGreater
        elif( nState == nErrorsAreGreater ):
            if ( bErrorsGreater ):
                continue
            else:
                nChangedAtThisX = int( aWords[0] )
                break
    #for szLine in fTable.readlines():
    assert nChangedAtThisX != -666

    # at nChangedAtThisX there are more good kmers than error kmers so
    # decrease by 1
    nFilteredKmersThisFreqAndLess = nChangedAtThisX - 1
        
    print( f"eliminate kmers at this freq and less: {nFilteredKmersThisFreqAndLess}" )
    
