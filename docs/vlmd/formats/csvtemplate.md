
# `csv` HEAL data dictionary (e.g., from template)

The HEAL Data Utilities can also input a `csv` HEAL data dictionary either from a manually filled out template or 
as an additional step after further annotation (e.g., from the `csv` HEAL data dictionary output of the other file formats).

## Creating a `csv` HEAL data dictionary

1. Use the template and start from scratch

    [Click here to download a blank __csv__ HEAL data dictionary template](../../assets/templates/template_submission.csv){:download="example_submission.csv" .md-button .md-button--primary }

    [Click here to download an example of a filled out __csv__ HEAL data dictionary template](../../assets/examples/valid/template_submission.csv){:download="template_submission.csv" .md-button .md-button--primary }

2. Output from one of the below software-specific formats and then further annotate.

!!! note
    To further annotate your outputted `csv` HEAL data dictionaries, see the variable level metadata field properties (with examples) for the __`csv data dictionary`__: [click here](../schemas/csv-fields.md)


## Validate with the `vlmd` command

After finishing your work on the `csv` HEAL data dictionary, run the `vlmd` command to ensure it is HEAL-compliant with:

```bash
vlmd --filepath data/heal-dd-output.csv --inputtype csvtemplate
```
