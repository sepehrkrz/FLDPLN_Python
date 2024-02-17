"""
Python script to scan an ERDAS or ESRI BIL file to extract minimum, maximum, and background values.

This script reads header information from the BIL file using the 'readbilheader' module.
It then scans the data to determine the minimum, maximum, and background values.

Author: Sepehr Karimi, PhD
Research Software Engineer - Data Science
CIROH at The University of Alabama
Contact: mkarimiziarani@ua.edu
"""

import numpy as np
from readbilheader import readbilheader

def scanbil(fnam):
    """
    Scans an ERDAS or ESRI BIL file to extract the minimum, maximum, and background values.

    Parameters:
        fnam (str): The file path to the BIL file.

    Returns:
        tuple: A tuple containing the minimum, maximum, and background values.
    """
    # Read BIL header
    filinfo = readbilheader(fnam)
    rows = filinfo['r']
    cols = filinfo['c']
    datfmt = filinfo['fmt']
    bytord = filinfo['bytord']

    # Open BIL file for reading
    with open(fnam, 'rb') as fid:
        # Initialize variables
        mn = np.finfo(float).max
        mx = -np.finfo(float).max
        mn2 = mn

        dv = rows // 100
        md = rows - dv * 100

        # Scan the BIL file
        for j in range(dv):
            dat = np.fromfile(fid, dtype=datfmt, count=cols * 100)
            mn = min(mn, np.min(dat))
            mx = max(mx, np.max(dat))
            if np.any(dat > mn):
                mn2 = min(mn2, np.min(dat[dat > mn]))

        if md:
            dat = np.fromfile(fid, dtype=datfmt, count=md)
            mn = min(mn, np.min(dat))
            mx = max(mx, np.max(dat))
            if np.any(dat > mn):
                mn2 = min(mn2, np.min(dat[dat > mn]))

    # Determine background value
    if mn > 0:
        bg = np.nan
    else:
        bg = mn
        mn = mn2

    return mn, mx, bg

# Test scanbil.py functionality
if __name__ == "__main__":
    fnam = 'C:/Tuscaloosa/bil/Tuscaloosa_10m.bil'
    mn, mx, bg = scanbil(fnam)

    # Display results
    print("Results:")
    print("Minimum value:", mn)
    print("Maximum value:", mx)
    print("Background value:", bg)
