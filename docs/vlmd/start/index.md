
# `Start` from a template

Some folks may prefer to create their HEAL data dictionary from scratch. To support this, we have created a utility that creates either a json or csv template. 


!!! warning

    Currently, the command is `template` but will change to `start` to be consistent with the verb subcommand vocabulary.
    
## `csv` template

The HEAL Data Utilities can also input a `csv` HEAL data dictionary either from a manually filled out template or 
as an additional step after further annotation (e.g., from the `csv` HEAL data dictionary output of the other file formats).


To create a template `csv` version with 10 fields (variables):

=== "Command line interface (CLI)"

    ```bash

    vlmd template myhealdd.csv --numfields 10

    ```

=== "Python"

    ```python

    from healdata_utils import write_vlmd_template

    write_vlmd_template(tmpdir.joinpath("heal.csv"),numfields=10)
        
    ```

[Click here to download an example of a filled out __csv__ HEAL data dictionary template](../../assets/examples/valid/template_submission.csv){:download="template_submission.csv" .md-button .md-button--primary }

## `json` template

While the `csv` HEAL data dictionary provides a tabular format for HEAL-compliant data dictionaries, ultimately, 
these csv data dictionary files are converted to a json file (the most common format to store and exchange data within web applications such as the HEAL Data Platform). 

Another advantage of `json` HEAL data dictionaries is that one can specify metadata describing the data dictionary as a whole (e.g., the `description` and `title`). 

To create a template `json` version with 10 fields (variables):

=== "Command line interface (CLI)"

    ```bash

    vlmd template myhealdd.json --numfields 10

    ```

=== "Python"

    ```python

    from healdata_utils import write_vlmd_template

    write_vlmd_template(tmpdir.joinpath("heal.json"),numfields=10)
        
    ```

[Click here to download an example of filled out __json__ HEAL data dictionary template](https://github.com/norc-heal/heal-metadata-schemas/blob/mbkranz/variable-lvl-dev/variable-level-metadata-schema/examples/valid/template_submission.json){:download .md-button .md-button--primary }