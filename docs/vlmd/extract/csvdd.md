# `csv` (Minimal) Data Dictionary


A minimal data dictionary in a csv (or tsv file). For example, may have `name`, `type`, and description and then this adds the rest of the fields. 

> Also maps a few common data types (such as char, character,text to 'string' and 'float' to 'number'.)

## Run the `vlmd` command

=== "CLI"

```bash
vlmd extract --inputtype csv-data-dict data/minimal-csv-dd.csv
```