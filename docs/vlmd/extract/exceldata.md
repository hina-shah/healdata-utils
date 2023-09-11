# Excel (xlsx) dataset

Excel workbooks contain tabular data tables across named worksheets.

Extract and infer a partially completed data dictionary from excel worksheets. The command line tool will automatically generate one data dictionary per worksheet. Working in python provides a little more flexibility as you can specify specific worksheets and if you want to combine sheets into one data dictionary (rather than one dd per sheet). 

## Run the `vlmd` command

=== "Python"

    ### To output multiple sheets as separate data dictionaries 

    ```python

    from healdata_utils import convert_to_vlmd

    convert_to_vlmd(input_filepath="myexcelfile.xlsx",inputtype="excel-data")
    
    ```

    ### To extract multiple sheets as one data dictionary 

    !!! note

        The parameter `multiple_data_dicts` is to specify whether multiple data dictionaries should be inferred (one per sheet). The default value is `True`. Be careful about using the `multiple_data_dicts=False`.
        In most instances, one sheet should correspond to one separate
        data table and thus have one corresponding data dictionary.  

    Note, this combines (ie concatenates all data tables) and then
    infers fields. This use case is when sheets are viewed as "chunks"
    of one resource/dataset. 

    ```python

    from healdata_utils import convert_to_vlmd

    convert_to_vlmd(
        input_filepath="myexcelfile.xlsx",
        inputtype="excel-data",
        multiple_data_dicts=False
        )
    
    ```


    ### To extract a subset of sheets as one data dictionary


    ```python

    from healdata_utils import convert_to_vlmd

    convert_to_vlmd(
        input_filepath="myexcelfile.xlsx",
        inputtype="excel-data",
        multiple_data_dicts=False,
        sheet_name=["mysheet1","mysheet2"]
        )
    
    ```
    
=== "CLI"

    ```bash
    vlmd extract --inputtype excel-data myexcelfile.xlsx
    ```