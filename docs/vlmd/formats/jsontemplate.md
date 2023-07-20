
# `json` HEAL data dictionary (e.g., from template)

While the `csv` HEAL data dictionary provides a tabular format for HEAL-compliant data dictionaries, ultimately, 
these csv data dictionary files are converted to a json file (the most common format to store and exchange data within web applications such as the HEAL Data Platform). 

The HEAL Data Utilities `vlmd` tool can also input this `json` HEAL data dictionary either from a manually filled out template or as an additional step after further annotation. Another advantage of `json` HEAL data dictionaries is that one can specify metadata describing the data dictionary as a whole (e.g., the `description` and `title`). 

## Creating a `json` HEAL data dictionary
1. Use the template and start from scratch (click on the template below to expand)

    [Click here to download a blank __json__ HEAL data dictionary template](https://github.com/norc-heal/heal-metadata-schemas/blob/mbkranz/variable-lvl-dev/variable-level-metadata-schema/templates/template_submission.json){:download .md-button .md-button--primary }

    [Click here to download an example of filled out __json__ HEAL data dictionary template](https://github.com/norc-heal/heal-metadata-schemas/blob/mbkranz/variable-lvl-dev/variable-level-metadata-schema/examples/valid/template_submission.json){:download .md-button .md-button--primary }
2. Output from one of the below software-specific formats and then further annotate.

!!! note
    To further annotate your outputted `json` HEAL data dictionaries, see the variable-level metadata field properties (with examples) for the __`json data dictionary`__: [click here](rendered-schemas/json-data-dictionary.md)


## Validate with the `vlmd` command

After finishing your work on the `json` HEAL data dictionary, run the `vlmd` command to ensure it is HEAL-compliant with:

```bash
vlmd --filepath data/heal-dd-output.json --inputtype jsontemplate
```