# HEAL Data Utilities
The HEAL data utilities package provides data packaging tools for the HEAL data ecosystem to facilitate data discovery,sharing, and harmonization with a focus on the HEAL platform data consultancy (DSC).

Currently, the focus of the repo is on generating data-dictionaries (see Variable level metadata section below). However, in the future, this will be expanded for all heal specific data packaging functions (e.g., study and file level metadata and data). 

## Variable level metadata (data dictionaries)

To use the functionality for variable level metadata, please review the notebook demonstrations below:

1. Generating a heal data dictionary from a variety of input files 

- [click here for static notebook ](notebooks/demos/inputs-to-heal-data-dictionary.ipynb) 
- click binder badge for interactive --> [![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/norc-heal/healdata-utils/HEAD?labpath=notebooks%2Fdemos%2Finputs-to-heal-data-dictionary.ipynb) 
2. [in development] Creating and iterating over a csv data dictionary to create a valid data dictionary file [click here](notebooks/demos/demo-csvtemplate-validation.ipynb)

The following file inputs are currently available:


### `csv`
Converts a CSV conforming to HEAL specifications (but see 2 additional notes below) 
    into a HEAL-specified data dictionary in both csv format and json format.

    Converts an in-memory data dictionary or a path to a data dictionary file into a HEAL-specified tabular template by:
        1. Adding missing fields, and
        2. Converting fields from a specified mapping.
            NOTE: currently this mapping is only float/num to number or text/char to string (case insensitive)
                In future versions, there will be a specified module for csv input mappings.
    
    
### `sav`
Converts a "metadata-rich" (ie statistical software file) 
    into a HEAL-specified data dictionary in both csv format and json format.

    This function relies on [readstat](https://github.com/Roche/pyreadstat) which supports SPSS (sav and por), 
    SAS (sas7bdat), and Stata (dta). 

    > Currently, this function uses both data and metadata to generate 
    a HEAL specified data dictionary. That is, types are inferred from the 
    data (so at least test or synthetic data needed) in addition to the metadata 
    (ie variable labels and value labels). 

    
### `dta`
Converts a "metadata-rich" (ie statistical software file) 
    into a HEAL-specified data dictionary in both csv format and json format.

    This function relies on [readstat](https://github.com/Roche/pyreadstat) which supports SPSS (sav and por), 
    SAS (sas7bdat), and Stata (dta). 

    > Currently, this function uses both data and metadata to generate 
    a HEAL specified data dictionary. That is, types are inferred from the 
    data (so at least test or synthetic data needed) in addition to the metadata 
    (ie variable labels and value labels). 

    
### `por`
Converts a "metadata-rich" (ie statistical software file) 
    into a HEAL-specified data dictionary in both csv format and json format.

    This function relies on [readstat](https://github.com/Roche/pyreadstat) which supports SPSS (sav and por), 
    SAS (sas7bdat), and Stata (dta). 

    > Currently, this function uses both data and metadata to generate 
    a HEAL specified data dictionary. That is, types are inferred from the 
    data (so at least test or synthetic data needed) in addition to the metadata 
    (ie variable labels and value labels). 

    
### `sas7bdat`
Converts a "metadata-rich" (ie statistical software file) 
    into a HEAL-specified data dictionary in both csv format and json format.

    This function relies on [readstat](https://github.com/Roche/pyreadstat) which supports SPSS (sav and por), 
    SAS (sas7bdat), and Stata (dta). 

    > Currently, this function uses both data and metadata to generate 
    a HEAL specified data dictionary. That is, types are inferred from the 
    data (so at least test or synthetic data needed) in addition to the metadata 
    (ie variable labels and value labels). 

    
### `json`
Converts a JSON file or dictionary conforming to HEAL specifications
    into a HEAL-specified data dictionary in both csv format and json format.

    Converts in-memory data or a path to a data dictionary file.
    
    
### `redcap.csv`
Takes in an exported Redcap Data Dictionary csv,
    and translates each field into a HEAL specified
    data dictionary based on field type (e.g., checkbox, radio, text and 
    other conditional logic based on Redcap specifications.)


    > While there are a variety of options for Redcap exports (eg directly through
    the API or via an XML), the Redcap CSV provides an easy-to-edit format comfortable by 
    technical and non-technical users.
