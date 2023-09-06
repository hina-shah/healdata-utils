# Stata `.dta` files

For Stata users, the HEAL Data Utilities generates HEAL-compliant data dictionaries through Stata's default file format: a `DTA` file. `DTA` files store not only the data itself but also metadata such as variable names, variable labels, types, and value labels.

<!-- ## Creating a well-annotated `dta` file

TO ADD -->

## Run the `vlmd` command
```bash
vlmd extract --inputtype stata data/mydatafile.dta 
```