# SAS `sas7bdat` (and `sas7bcat`) files

To accommodate SAS users, the HEAL Data Utilities supports the binary `sas7bdat` file format, which contains the actual data values (observations/records). This file also includes variable metadata (variable `names` and variable labels/ `descriptions`).

The HEAL Data Utilities also provides the option to include a catalog file – `sas7bcat` format - with the `sas7bdat`.  A `sas7bcat` file contains variable value labels, or `encodings`, that can be mapped onto the corresponding data from a `sas7bdat` file.

## Creating a `sas7bdat` and a `sas7bcat` file

Many SAS users build formats and labels into their data processing and analysis scripts. In this section, we provide syntax that can be easily copy-pasted into these existing workflows to create `sas7bdat` and `sas7bcat` files to input into the `vlmd` tool. 

This script template can be run separately or inserted directly at the end of a SAS user's workflow. 

!!! note
    If inserted directly, remember to delete the lines with `%INCLUDE`)

???+ Template
    ```sas title="template.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary. You may have defined variable labels and values in separate scripts for different analyses. In order to capture all your defined variable labels and values across scripts, you will need an %INCLUDE statement for each SAS script that defines unique variable labels or value labels.*/

    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/
    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SECOND SEPARATE SAS SCRIPT*/ 

    /*2. Output the format catalog (sas7bcat) */
    /*2a. If you do not have an out directory, assign one to output the SAS catalog and data file. If you already have an out directory assigned, skip this step and replace “out” with your out directory libname in the flow*/

    libname out "<INSERT THE DESIRED LOCATION (FILE PATH) TO YOUR SAS7BCAT AND SAS7BDAT FILES HERE>";

    /*2b. Output the format catalog.
            Note: The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) */
    data out.yourdata;
        set <INSERT THE NAME OF YOUR FINAL SAS DATASET HERE>;
        run;

    ```

The below SAS syntax is an example of how to use the template within your SAS workflow.

The below sample script creates all of our variable and value labels. Your workflow may include multiple SAS scripts with multiple format statements and may include analyses and other PROC calls for data exploration, 
but for demonstration purposes, this example only uses one script and focuses on defining the variable and value labels.

???+ Example Template Usage

    ```sas title="my_existing_sas_workflow.sas"
    /*1. Read in input data */
    proc import datafile="myprojectfolder/input/mydata.csv"
        out=raw
        dbms=csv replace;
        getnames=yes;
    run;

    /*2. Set up proc format and apply formats and variable labels in data step */
    /*Create encodings (value labels)*/
    proc format;
        VALUE YESNO
        0       ="No"
        1       ="Yes"
        
        VALUE PUBLIC
        1='State mental health authority (SMHA)'
        2='Other state government agency or department'
        3='Regional/district authority or county, local, or municipal government'
        4='Tribal government'
        5='Indian Health Service'
        6='Department of Veterans Affairs'
        7='Other'
        
        VALUE FOCUS
        1='Mental health treatment'
        2='Substance abuse treatment'
        3='Mix of mental health and substance abuse treatment (neither is primary)'
        4='General health care'
        5='Other service focus';

    **Apply formats to dataset;
    data processed;
        set raw;
        
    	/*Assign formats*/
        format YOUNGADULTS TREATPSYCHOTHRPY TREATTRAUMATHRPY YESNO. FOCUS FOCUS. PUBLIC PUBLIC.;
    	/*Add variable labels*/
        label YOUNGADULTS="Accepts young adults (aged 18-25 years old) for Tx"
                TREATPSYCHOTHRPY="Facility offers individual psychotherapy"
                TREATTRAUMATHRPY="Facility offers trauma therapy"
                FOCUS="Primary treatment focus of facility"
                PUBLIC="Public agency or department that operates facility";
    run;
    ```

    This second script called `my_output.sas` is the filled out template. Note the `%INCLUDE` function that calls `my_existing_sas_workflow.sas`

    ```sas title="my_output.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary. You may have defined variable labels and values in separate scripts for different analyses. In order to capture all your defined variable labels and values across scripts, you will need an %INCLUDE statement for each SAS script that defines unique variable labels or value labels.*/*/

    %INCLUDE "myprojectfolder/my_existing_workflow.sas"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/

    /*2. Output the format catalog (sas7bcat) */
    /*2a. If you do not have an out directory, assign one to output the SAS catalog and data file.*/
    libname out "myprojectfolder/output";

    /*2b. Output the format catalog.
            Note: The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) to your output folder*/
    data out.yourdata;
        set processed;
        run;

    ```

## Run the `vlmd` command

After creating the necessary `sas7bdat` and `sas7bcat` files, you can then run the `vlmd` command. The tool, will automatically detect the sas7bcat file **if** located in the same directory as your data file. If not detected, the command will run without the sas7bcat catalog file and the `encodings` (i.e., value labels) will not be extracted from the catalog file.


```bash
vlmd extract --inputtype sas input/data.sas7bdat 
```
