# Variable-level Metadata (Data Dictionaries)


## Motivation

Variable level metadata (VLMD), in the form of standardized data dictionaries, provides an exciting opportunity:

-  a way to search, understand, and compare datasets before (potentially sensitive) data is shared. 

> For an example of this searchability in the context of study level metadata, [see the platform's discovery page](https://healdata.org/portal/discovery)

- When data is available, VLMD provides a way to validate the data as well.

- Supports HEAL projects and goals such as the [common data elements program](https://heal.nih.gov/data/common-data-elements)

## Basic usage

The healdata-utils variable-level metadata (vlmd) tool inputs a variety of different input file types and exports HEAL-compliant data dictionaries (JSON and CSV formats). Additionally, exported validation (i.e., "error") reports provide the user information as to a) if the exported data dictionary is valid according to HEAL specifications and b) how to modify one's data dictionary to make it HEAL-compliant.

=== "Python"
    ```python

    from healdata_utils import convert_to_vlmd

    description = "This is a proof of concept to demonstrate the healdata-utils functionality"
    title = "Healdata-utils Demonstration Data Dictionary"

    convert_to_vlmd(
        filepath="myproject/myfile.sav",inputtype="sav",
        data_dictionary_props={"description":"This contains my test data","title":"Test data"})

    ```

    !!! note
    
        for a complete set of options with `convert_to_vlmd` see the docstring (if in a notebook, one can enter `convert_to_vlmd?`)

=== "Command Line Interface (CLI)"

    ```bash

    vlmd --filepath myproject/myfile.sav --inputtype sav --description "This contains my test data" --title "Test data"

    ```
    !!! note

        For descriptions on the different flags/options, run `vlmd --help`

### Output

Both the python and command line routes will result in a JSON and CSV version of the HEAL data dictionary in the output folder along with the validation reports in the `errors` folder. See below:

- `errors/heal-csv-errors.json`: outputted validation report for table in csv file against frictionless schema

- `errors/heal-json-errors.json`:  outputted jsonschema validation report.

- `heal-csvtemplate-data-dictionary.csv`: This is the CSV data dictionary
- `heal-jsontemplate-data-dictionary.json`: This is the JSON version of the data dictionary

## CSV and JSON data dictionary definitions
!!! important
    The main difference* between the CSV and JSON data dictionary validation lies in the way the data dictionaries are structured and the additional metadata included in the JSON data dictionary.
    
    The CSV data dictionary is a plain tabular representation with no additional metadata, while the JSON dataset includes fields along with additional metadata in the form of a root description and title.

    * for field-specific differences, see the schemas in the documentation. 

For more information on variable-level metadata properties (fields), see the [`csv` field specification](schemas/csv-fields.md) and [`json` data dictionary specification](schemas/json-data-dictionary.md). 

!!! note ""

    Typical workflows for creating a HEAL-compliant data dictionary include:

    1. **Run the `vlmd` command** (or `convert_to_vlmd` if in python) to generate a HEAL-compliant data dictionary via your desired input format (See the basic usage section on the homepage for general installation and usage information).
    2. **Add/annotate with** additional information in your preferred HEAL data dictionary format (either `json` or `csv`).
        - To further annotate and use the data dictionary, see the variable-level metadata field property information below:
            - [`csv` data dictionary](schemas/csv-fields.md)
            - [`json` data dictionary](schemas/json-data-dictionary.md)

    3. **Run the `vlmd` command** again with your HEAL data dictioanry as the input to validate.

    4. Repeat (2) and (3) until you are ready to submit. Please note, currently only `name` and `description` are required.

## Interactive notebooks

See the below notebooks demonstrating use and workflows using the `convert_to_vlmd` in python and `vlmd` in the command line. 

> Clicking on the "binder badges" will bring you to an interactive notebook page where you can test out the notebooks. Here, healdata-utils comes pre-installed.

1. Generating a heal data dictionary from a variety of input files 

- [click here for static notebook ](https://github.com/norc-heal/healdata-utils/blob/main/notebooks/demos/inputs-to-heal-data-dictionary.ipynb) 
- click binder badge for interactive [![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/norc-heal/healdata-utils/HEAD?labpath=notebooks%2Fdemos%2Finputs-to-heal-data-dictionary.ipynb) 

<!-- 2. [in development] Creating and iterating over a csv data dictionary to create a valid data dictionary file [click here](notebooks/demos/demo-csvtemplate-validation.ipynb) -->

