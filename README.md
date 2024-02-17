# FLDPLN Translation Project

**Note: This project is actively being developed. We appreciate contributions from other developers to help translate this MATLAB project to Python.**

## Overview

This repository aims to translate a MATLAB project, FLDPLN, into Python. The FLDPLN concept, documented in [Jude Kastens' 2008 Ph.D. dissertation](https://kuscholarworks.ku.edu/handle/1808/5354), introduces a physically-based computational model for mapping potential inundation extents (floodplains) using gridded topographic data. Since its publication, FLDPLN has been utilized in various instances to estimate flood inundation extents for research and real-time emergency management purposes, particularly in Kansas and other regions.

## Demonstration

Using FLDPLN involves three general steps:

1. Preparing a DEM and other basic input data.
2. Computing a FLDPLN library.
3. Using the library for mapping.

A demonstration case based on Tuscaloosa, Alabama, is provided, with input files available as a [Package on hydroshare.org](https://www.hydroshare.org/resource/2ba43947ef6447beaf055349c883c96e/). Instructions for preparing a set of FLDPLN library files based on this package are outlined below.

## Translated Functions

- **readbilheader.py:** Translated MATLAB function to extract header information from BIL files into Python.
- **scanbil.py:** Python script to scan an ERDAS or ESRI BIL file to extract minimum, maximum, and background values.
## Steps to Contribute

1. Clone this repository to your computer:
    ```
    git clone https://github.com/AlabamaWaterInstitute/fldpln
    ```

2. Install Python and necessary packages according to the instructions provided.

3. Review the MATLAB codebase and corresponding functions to understand the functionality and algorithms.

4. Translate MATLAB functions into Python functions while maintaining functionality and performance.

5. Test the translated Python functions to ensure correctness and compatibility.

6. Submit pull requests with your translated Python code for review and integration into the main repository.

## Notes

- Contributions in translating the MATLAB project to Python are welcome.
- Please adhere to the coding conventions and guidelines specified in the repository.
- If you encounter any issues or have questions, feel free to open an issue or reach out to the project maintainers.

---

For further details and access to the MATLAB repository, please visit [here](https://github.com/AlabamaWaterInstitute/fldpln/tree/main).

This project is under active development, and contributions are welcome!
