# Variable-level Metadata (Data Dictionaries)


## Motivation

Variable level metadata (VLMD), in the form of standardized data dictionaries, provides an exciting opportunity:

-  a way to search, understand, and compare datasets before (potentially sensitive) data is shared. 

> For an example of this searchability in the context of study level metadata, [see the platform's discovery page](https://healdata.org/portal/discovery)

- When data is available, VLMD provides a way to validate the data as well.

- Supports HEAL projects and goals such as the [common data elements program](https://heal.nih.gov/data/common-data-elements)


## Quick start

=== "Command Line Interface (CLI)"

**Double click** on the `vlmd` (or `vlmd.exe`) executable or **run** the `vlmd` executable without any arguments to quickly start using this tool. This "quick start" will take walk you through step by step.

The executables can be found 

## Basic usage


### `Extract` VLMD from another data type and format

The healdata-utils variable-level metadata (vlmd) tool inputs a variety of different input file types and extracts HEAL-compliant data dictionaries (JSON and CSV formats). Additionally, exported validation (i.e., "error") reports provide the user information as to a) if the exported data dictionary is valid according to HEAL specifications and b) how to modify one's data dictionary to make it HEAL-compliant.

=== "Command Line Interface (CLI)"

    ```bash

    vlmd extract --inputtype spss myproject/myfile.sav

    ```
    !!! note

        To continue, it's recommended to go to the [input types and formats](#input-types-and-formats). Also, for more details on the different flags/options, run `vlmd --help`

=== "Python"
    ```python

    from healdata_utils import convert_to_vlmd

    convert_to_vlmd(filepath="myproject/myfile.sav",inputtype="spss")

    ```

    !!! note

        To continue, it's recommended to go to the [input types and formats](#input-types-and-formats). For a complete set of options with `convert_to_vlmd` see the docstring (if in a notebook, one can enter `convert_to_vlmd?`)


#### Input Types and Formats

This section provides the specific syntax for running each of the supported types for generating HEAL-compliant data dictionaries are listed. Additional instructions on how to obtain the necessary input files/software are also provided. 


!!! note
    To further annotate your outputted data dictionaries, see the variable-level metadata field properties (with examples) for either the __`csv data dictionary`__ [click here](./schemas/csv-fields.md) or the __`json data dictionary`__ [click here](./schemas/json-data-dictionary.md).

<!-- TODO: Automate creation of these lists below -->


Extract variable level metadata from your data:

- [CSV datasets](./formats/csvdata.md)
- [SPSS datasets](./formats/spss.md)
- [SAS datasets](./formats/sas.md)
- [Stata datasets](./formats/stata.md)
- [REDCap data dictionary](./formats/redcapcsv.md)
- [Frictionless Table Schema](./formats/frictionlessschema.md)

#### Output

Both the python and command line routes will result in a JSON and CSV version of the HEAL data dictionary in the output folder along with the validation reports in the `errors` folder. See below:

- `errors/heal-csv-errors.json`: outputted validation report for table in csv file against frictionless schema

If valid, this file will contain:
```json
{
    "valid": true,
    "errors": []
}
```
- `errors/heal-json-errors.json`:  outputted jsonschema validation report.

- If valid, this file will contain:
```json
{
    "valid": true,
    "errors": []
}
```

If no `outputdir` specified, the resulting HEAL-compliant data dictionaries will be named:

- `heal-csvtemplate-data-dictionary.csv`: This is the CSV data dictionary
- `heal-jsontemplate-data-dictionary.json`: This is the JSON version of the data dictionary
### `Template`: Create and annotate a HEAL data dictionary

Some folks may prefer to extract their vlmd themselves. To support this, we have created a utility that creates either a json or csv template. 

For more details (and downloadable examples) see:

- [HEAL CSV template data dictionary](./formats/csvtemplate.md)
- [HEAL JSON template data dictionary](./formats/jsontemplate.md)

=== Command line interface (CLI)


To create a template `json` version with 10 fields (variables):

```bash

vlmd template myhealdd.json --numfields 10

```

To create a template `csv` version with 10 fields (variables):

```bash

vlmd template myhealdd.csv --numfields 10

```


=== Python

```python

from healdata_utils import write_vlmd_template

write_vlmd_template(tmpdir.joinpath("heal.json"),numfields=10)
    
```

To create a template csv version with 10 fields (variables):

```python

from healdata_utils import write_vlmd_template

write_vlmd_template(tmpdir.joinpath("heal.csv"),numfields=10)

```

### `Validate` Check (validate) an existing HEAL data dictionary file 

Will indicate if the data dictionary complies with the HEAL specifications.

=== Command line interface (CLI)

```bash

vlmd validate data/myhealcsvdd.csv

vlmd validate data/myhealjsondd.json



```

=== Python


```python

from healdata_utils import validate_vlmd_csv,validate_vlmd_json

validate_vlmd_csv("data/myhealcsvdd.csv")

validate_vlmd_json("data/myhealjsondd.json")

```


## CSV and JSON data dictionary definitions
!!! important
    The main difference* between the CSV and JSON data dictionary validation lies in the way the data dictionaries are structured and the additional metadata included in the JSON data dictionary.
    
    The CSV data dictionary is a plain tabular representation with no additional metadata, while the JSON dataset includes fields along with additional metadata in the form of a root description and title.

    * for field-specific differences, see the schemas in the documentation. 

For more information on variable-level metadata properties (fields), see the [`csv` field specification](./schemas/csv-fields.md) and [`json` data dictionary specification](./schemas/json-data-dictionary.md). 

!!! note ""

    Typical workflows for creating a HEAL-compliant data dictionary include:

    1. **Run the `vlmd` command** (or `convert_to_vlmd` if in python) to generate a HEAL-compliant data dictionary via your desired input format (See the basic usage section on the homepage for general installation and usage information).
    2. **Add/annotate with** additional information in your preferred HEAL data dictionary format (either `json` or `csv`).
        - To further annotate and use the data dictionary, see the variable-level metadata field property information below:
            - [`csv` data dictionary](./schemas/csv-fields.md)
            - [`json` data dictionary](./schemas/json-data-dictionary.md)

    3. **Run the `vlmd` command** again with your HEAL data dictioanry as the input to validate.

    4. Repeat (2) and (3) until you are ready to submit. Please note, currently only `name` and `description` are required.

<!-- ## Interactive notebooks

See the below notebooks demonstrating use and workflows using the `convert_to_vlmd` in python and `vlmd` in the command line. 

> Clicking on the "binder badges" will bring you to an interactive notebook page where you can test out the notebooks. Here, healdata-utils comes pre-installed.

1. Generating a heal data dictionary from a variety of input files 

- [click here for static notebook ](https://github.com/norc-heal/healdata-utils/blob/main/notebooks/demos/inputs-to-heal-data-dictionary.ipynb) 
- click binder badge for interactive [![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/norc-heal/healdata-utils/HEAD?labpath=notebooks%2Fdemos%2Finputs-to-heal-data-dictionary.ipynb)  -->

<!-- 2. [in development] Creating and iterating over a csv data dictionary to create a valid data dictionary file [click here](notebooks/demos/demo-csvtemplate-validation.ipynb) -->

