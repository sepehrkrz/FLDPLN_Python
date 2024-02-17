"""
Python script (translated from Matlab) to read header information from a BIL (Band Interleaved by Line) file.

Sepehr Karimi, PhD
Research Software Engineer - Data Science
CIROH at The University of Alabama
mkarimiziarani@ua.edu
"""
import re
from typing import Dict, Union

def read_header_info(hdr_content: str) -> Dict[str, Union[int, float, str]]:
    """
    Extracts header information from the header content.
    
    Args:
        hdr_content (str): Content of the header file.
        
    Returns:
        dict: Dictionary containing header information.
    """
    header_info = {}
    
    # Extracting relevant information using regular expressions
    header_info['bytord'] = 0 if re.search(r'BYTEORDER\s+I', hdr_content) else 1
    header_info['r'] = int(re.search(r'NROWS\s+(\d+)', hdr_content).group(1))
    header_info['c'] = int(re.search(r'NCOLS\s+(\d+)', hdr_content).group(1))
    header_info['bands'] = int(re.search(r'NBANDS\s+(\d+)', hdr_content).group(1))
    nodata_match = re.search(r'NODATA\s+([-+]?\d*\.\d+|\d+)', hdr_content)
    header_info['nodata'] = float(nodata_match.group(1)) if nodata_match else None
    header_info['nbits'] = int(re.search(r'NBITS\s+(\d+)', hdr_content).group(1))
    header_info['nbyts'] = header_info['nbits'] // 8
    
    # Determine the biltyp based on the header content
    header_info['biltyp'] = 'ESRI' if 'ULXMAP' in hdr_content else 'ERDAS'

    # Extract additional information if the file type is ESRI
    if header_info['biltyp'] == 'ESRI':
        header_info['ulx'] = float(re.search(r'ULXMAP\s+([-+]?\d*\.\d+|\d+)', hdr_content).group(1))
        header_info['uly'] = float(re.search(r'ULYMAP\s+([-+]?\d*\.\d+|\d+)', hdr_content).group(1))
        header_info['pxszx'] = float(re.search(r'XDIM\s+([-+]?\d*\.\d+|\d+)', hdr_content).group(1))
        header_info['pxszy'] = float(re.search(r'YDIM\s+([-+]?\d*\.\d+|\d+)', hdr_content).group(1))
        pixeltype_match = re.search(r'PIXELTYPE\s+(\w+)', hdr_content)
        pixeltype = pixeltype_match.group(1) if pixeltype_match else None
        if pixeltype == 'SIGNEDINT':
            header_info['fmt'] = f"int{header_info['nbits']}"
        elif pixeltype == 'UNSIGNEDINT':
            header_info['fmt'] = f"uint{header_info['nbits']}"
        elif pixeltype == 'FLOAT':
            header_info['fmt'] = 'single' if header_info['nbits'] == 32 else 'double'
    else:
        header_info['fmt'] = 'single'  # Placeholder value for ERDAS files
    
    return header_info

def readbilheader(bilfile: str) -> Dict[str, Union[int, float, str]]:
    """
    Reads header information from a BIL file and returns it as a dictionary.
    
    Args:
        bilfile (str): Path to the BIL file.
        
    Returns:
        dict: Dictionary containing header information.
    """
    # Construct the header file name
    hdr_file = bilfile[:-3] + 'hdr'
    
    # Read the content of the header file
    with open(hdr_file, 'r') as hdr:
        hdr_content = hdr.read()
    
    # Extract header information from the content
    header_info = read_header_info(hdr_content)
    
    return header_info

# Test the function
if __name__ == "__main__":
    bilfile = 'C:/Tuscaloosa/bil/Tuscaloosa_10m.bil'
    header_info = readbilheader(bilfile)
    print("Header Information:")
    for key, value in header_info.items():
        print(f"\t{key}: {value}")
