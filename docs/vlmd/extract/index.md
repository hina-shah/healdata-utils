
# `Extract` VLMD from another data type and format

The healdata-utils variable-level metadata (vlmd) tool inputs a variety of different input file types and extracts HEAL-compliant data dictionaries (JSON and CSV formats). Additionally, exported validation (i.e., "error") reports provide the user information as to a) if the exported data dictionary is valid according to HEAL specifications and b) how to modify one's data dictionary to make it HEAL-compliant.

!!! warning 

    Currently the python subcommand is `convert` but will be changed to `extract_to_vlmd` to be
    consistent with CLI. `extract` was chosen to better reflect the functionality.


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