
# SPSS `.sav` files

For SPSS users, the HEAL Data Utilities generates HEAL-compliant data dictionaries from SPSS's default file format for storing datasets: a `SAV` file. It stores not only the data itself but also metadata such as variable names, variable labels, types, and value labels. The HEAL Data Utilities extracts these data and metadata to create HEAL-compliant data dictionaries.

<!-- # Creating a well-annotated `sav` file

TO ADD -->

## Run the `vlmd` command
```bash
vlmd extract --inputtype spss data/example_pyreadstat_output.sav 
```