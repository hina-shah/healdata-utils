# `csv` Datasets

CSV (comma-separated values) is the main open tabular data format for storage and exchange. It is easy to create and understand using basic text editors in addition to popular spreadsheet software like Google Sheets and Excel. Importantly, CSVs are simple and can be easily integrated into web applications and just about any software.

Currently, the HEAL Data Utilities `vlmd` function can infer a minimal, HEAL-compliant dataset by inferring `name`, `type`, and `enum` (i.e., possible values). After this minimal data dictionary is generated, the researcher can further annotate
it with fields' `description` and other optional properties in either the HEAL-compliant `csv`- or `json`-formatted data dictionary (see the HEAL data dictionary template sections below for more information).
