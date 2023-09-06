# `Validate` Check (validate) an existing HEAL data dictionary file 

Will indicate if the data dictionary complies with the HEAL specifications.

=== "Command line interface (CLI)"

    ```bash

    vlmd validate data/myhealcsvdd.csv

    vlmd validate data/myhealjsondd.json



    ```

=== "Python"

    ```python

    from healdata_utils import validate_vlmd_csv,validate_vlmd_json

    validate_vlmd_csv("data/myhealcsvdd.csv")

    validate_vlmd_json("data/myhealjsondd.json")

    ```