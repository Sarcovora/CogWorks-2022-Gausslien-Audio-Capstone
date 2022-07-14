def getFingerprints(peakPoints, nfanout=5):
    """
    Extract fingerprints from peak points of the form (tm, fm)
    
    Parameters
    ----------
    peakPoints : numpy.ndarray, shape-(H, 2)
        The 2D array of data containing all the peaks.
    
    Returns
    -------
    List[Tuple[int, int, int, int]]
        T
    """
    peakCount = len(peakPoints)
    peakpairs = []
    
    for i1 in range(peakCount-1):
        i2 = i1
        while i2 < peakCount-1 and i2-i1 < nfanout:
            i2+=1
            
            f1 = peakPoints[i1][1]
            f2 = peakPoints[i2][1]
            dt = peakPoints[i2][0] - peakPoints[i1][0]
            t = peakPoints[i1][0]
            
            peakpairs.append((f1,f2,dt,t))
    
    return peakpairs
