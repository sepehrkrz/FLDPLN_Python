"""
Python script to create a stream network map from a BIL (Band Interleaved by Line) file.
This script reads header information from the BIL file using the 'readbilheader' module.
It then processes the data to identify stream pixels based on a specified threshold value.
The resulting stream map is saved in another BIL file.

Author: Sepehr Karimi, PhD
Research Software Engineer - Data Science
CIROH at The University of Alabama
Contact: mkarimiziarani@ua.edu
"""

import numpy as np
from readbilheader import readbilheader

def make_stream_map(facf, thr, strf):
    # Read spatial parameters from FAC
    facinfo = readbilheader(facf)
    r = facinfo['r']  # rows
    c = facinfo['c']  # cols
    bytord = facinfo['bytord']  # byte order; if 1 then open file with 'b' option
    fmt = facinfo['fmt']  # FAC BIL file data format

    # Open FAC file for reading
    if bytord:
        fac = open(facf, 'rb', newline='')
    else:
        fac = open(facf, 'rb')
    
    # Open STR file for writing
    str_file = open(strf, 'wb')
    
   # Initialize zro array with appropriate shape
    zro = np.zeros((c, 1), dtype=np.uint8)

    # Print type and dimensions of zro
    print("Type of zro:", type(zro))
    print("Dimensions of zro:", zro.shape)

    for j in range(r):
        # Read a row of data
        ln = np.fromfile(fac, dtype=fmt, count=c).reshape(-1, 1)
        
        if len(ln) > 0:
            # Check if any element meets the condition
            if np.any(ln >= thr):
                # Create a copy, update elements, and write to file
                zro1 = np.zeros((len(ln), 1), dtype=np.uint8)
                print("Shape of ln:", ln.shape)
                print("Shape of zro1:", zro1.shape)
                zro1[ln >= thr] = 1
                zro1.tofile(str_file)
                #print('zro:::::',zro1)
                # Print type and dimensions of zro1 (current iteration)
                print(f"Type of zro1 (iteration {j+1}):", type(zro1))
                print(f"Dimensions of zro1 (iteration {j+1}):", zro1.shape)
            else:
                # Write original zro to file
                zro.tofile(str_file)

    # Close files explicitly
    fac.close()
    str_file.close()
    
    # Modify the header file
    with open(facf[:-3] + 'hdr', 'r') as fhdr0, open(strf[:-3] + 'hdr', 'w') as fhdr:
        for line in fhdr0:
            if line.startswith("NBIT"):
                fhdr.write("NBITS          8\n")
            elif line.startswith("BANDROWBYTE"):
                fhdr.write("BANDROWBYTES   2703\n")
            elif line.startswith("TOTALROWBYTE"):
                fhdr.write("TOTALROWBYTES  2703\n")
            elif line.startswith("PIXELTYP"):
                fhdr.write("PIXELTYPE      UNSIGNEDINT\n")
            elif line.startswith("NODATA"):
                fhdr.write("NODATA         0\n")
            else:
                fhdr.write(line)
    

    print('Binary stream network map creation completed')

if __name__ == "__main__":
    # Test script
    # Specify the path and filename for the FAC ERDAS BIL file
    facf = 'C:\\Tuscaloosa\\bil\\Tuscaloosa_10m.bil'

    # Specify the minimum number of pixels to use for stream pixel designation
    thr = 1812992  # Example threshold value (adjust as needed)

    # Specify the path and filename for the output STR ERDAS BIL file
    strf = 'C:\\Tuscaloosa\\bil\\pythonstr.bil'

    # Call the make_stream_map function
    make_stream_map(facf, thr, strf)
