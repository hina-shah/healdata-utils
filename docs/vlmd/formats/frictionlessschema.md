# Frictionless Table Schema

While vlmd specifications are designed (and still being developed), to support interoperability with the heal platform, minor naming translations may be needed. This function supports any of said translations (eg., frictionless `fields` name --> heal `data_dictionary`)

Note, this conversion supports either `yaml` or `json` format (currently only tests for `json` format but should work with yaml). 

## Creating a frictionless table schema

Below are the official frictionless table schema specifications, which you will notice a high degree of overlap with the heal variable level metadata specifications.

<iframe
    src="https://specs.frictionlessdata.io/table-schema"
    style="width:100%; height:500px;overflow:auto"
>
</iframe>

## Run the `vlmd` command
```bash
vlmd extract --inputtype frictionless data/frictionless_dataset1.frictionless.schema.json
```