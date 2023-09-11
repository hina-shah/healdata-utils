
Excel workbooks contain tabular data tables across named worksheets.

Extract vlmd from all worksheets of an excel workbook or as a combined data dictionary (python only) or as multiple data dictionaries (ie one dd = one worksheet). Note, to specify specific worksheets, use the tool within python.


## Run the `vlmd` command


=== "CLI"

    ```bash
    vlmd extract --inputtype excel-data myexcelfile.xlsx
    ```


=== "Python"

    ### To output multiple sheets as separate data dictionaries 

    ```python

    from healdata_utils import convert_to_vlmd

    convert_to_vlmd(input_filepath="myexcelfile.xlsx",inputtype="excel-data")
    
    ```

    ### To extract multiple sheets as one data dictionary 

    !!! note

        Be careful about using the `multiple_data_dicts=False`.
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
    
