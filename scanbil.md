## scanbil.py

Python script to scan an ERDAS or ESRI BIL file to extract minimum, maximum, and background values.

This script reads header information from the BIL file using the 'readbilheader' module.
It then scans the data to determine the minimum, maximum, and background values.

Author: Sepehr Karimi, PhD  
Research Software Engineer - Data Science  
CIROH at The University of Alabama  
Contact: mkarimiziarani@ua.edu

### Functionality:

- **scanbil(fnam):**
  - Scans an ERDAS or ESRI BIL file to extract the minimum, maximum, and background values.
  
    - Parameters:
      - `fnam (str)`: The file path to the BIL file.
      
    - Returns:
      - `tuple`: A tuple containing the minimum, maximum, and background values.

### Example Usage:
```python
fnam = 'C:/Tuscaloosa/bil/Tuscaloosa_10m.bil'
mn, mx, bg = scanbil(fnam)

# Display results
print("Results:")
print("Minimum value:", mn)
print("Maximum value:", mx)
print("Background value:", bg)
