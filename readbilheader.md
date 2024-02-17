## readbilheader.py

Python script to read header information from a BIL (Band Interleaved by Line) file.

Author: Sepehr Karimi, PhD  
Research Software Engineer - Data Science  
CIROH at The University of Alabama  
Contact: mkarimiziarani@ua.edu

### Functionality:

- **read_header_info(hdr_content: str) -> Dict[str, Union[int, float, str]]:**
  - Extracts header information from the header content.
  
    - Args:
      - `hdr_content (str)`: Content of the header file.
      
    - Returns:
      - `dict`: Dictionary containing header information.

- **readbilheader(bilfile: str) -> Dict[str, Union[int, float, str]]:**
  - Reads header information from a BIL file and returns it as a dictionary.
  
    - Args:
      - `bilfile (str)`: Path to the BIL file.
      
    - Returns:
      - `dict`: Dictionary containing header information.

### Example Usage:
```python
bilfile = 'C:/Tuscaloosa/bil/Tuscaloosa_10m.bil'
header_info = readbilheader(bilfile)
print("Header Information:")
for key, value in header_info.items():
    print(f"\t{key}: {value}")
