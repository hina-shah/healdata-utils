''' 

command line interface for generating HEAL data dictionary/vlmd json files

''' 

import click 


from healdata_utils.validators.validate import validate_vlmd_json,validate_vlmd_csv
import json
from pathlib import Path
import petl as etl
import pandas as pd
import csv
from collections import deque

from healdata_utils.utils import find_docstring_desc
from healdata_utils.conversion import convert_to_vlmd,choice_fxn
from healdata_utils.validators import validate_vlmd_json,validate_vlmd_csv
from healdata_utils.io import write_vlmd_template
# TODO: vlmd group that invokes input prompts and directs towards one of the three sub commands
# TODO: validate takes in either a heal specified json or a csv and validates
subcmds = ["extract","validate","template"]

prompt_subcmds = """
Select one of the following:

validate: check (validate) an existing HEAL data dictionary to see if it maps the HEAL specifications.
extract: take an existing format and extract the variable level metadata out.
template: generate a HEAL template to fill in. 


"""

prompt_inputfile = """
What is the path to your input file? 

This can be an:
1. absolute path (e.g., C:/Users/lastname-firstname/projectfolder/data/inputfilename.csv)
2. relative path (e.g., data/inputfilename.csv)
3. filename (e.g., inputfilename.csv)

"""

prompt_extract_inputtypes = """
What type of file do you want to extract variable level metadata from?
"""

prompt_template_nfields = """
How many variables (ie fields) are in your data (ie are going to be in your data dictionary)?
""" 

prompt_template_outputfile = """
What do you want the output file called?

This can be an:
1. absolute path (e.g., C:/Users/lastname-firstname/projectfolder/heal-data-dictionary.csv)
2. relative path (e.g., heal-data-dictionary.csv)
3. filename (e.g., heal-data-dictionary.csv)

Note, if you specify a csv file, this will generate a HEAL csv templated file and if you specify a json file, this
will generate a HEAL json templated file.


""" 
prompt_extract_outputfile = """ 
What do you want the output file called? 

Note, whether you specify a json or csv, both formats will be generated for convenience 
(i.e., heal-dd.json generates heal-dd.json and heal-dd.csv)

"""

prompt_overwrite = """
Do you want to overwrite the specified output files (if they exist)?

"""

def _prompt_outputfile_overwrite(outputfile_prompt):

    """ 
    Prompts for output file path,
    checks that it is either a csv or json file,
    if the file exists, prompts user if they want to overwrite.

    Prompts (ie function) start over if user specifies no overwrite and file exists
    or if the file specified is not a csv or json

    NOTE
    ----- 
    Reasoning for checking both csv and json is to ensure they are "synced" and
    currently the convert_to_vlmd fxn outputs both csv and json by default

    """ 
    outputfile = click.prompt(
        text=outputfile_prompt,
        type=click.Path()
    )
    outputfile = Path(outputfile)
    # Check for existence and ask if they want to overwrite file
    
    outputfile_csv = Path(outputfile).with_suffix(".csv")
    outputfile_json = Path(outputfile).with_suffix(".json")

    fileexts = [".json",".csv"]
    if not outputfile.suffix in fileexts:
        click.secho(f"File must be {' or '.join(fileexts)}")
        outputfile,outputfile_overwrite = _prompt_outputfile_overwrite(outputfile_prompt)
    else:
        if outputfile_csv.exists():
            click.secho(f"Warning: {outputfile_csv} exists")

        if outputfile_json.exists():
            click.secho(f"Warning: {outputfile_json} exists")  

        if outputfile_json.exists() or outputfile_csv.exists():
            outputfile_overwrite = click.confirm(prompt_overwrite)
            if not outputfile_overwrite:
                outputfile,outputfile_overwrite = _prompt_outputfile_overwrite(outputfile_prompt)

    return outputfile,outputfile_overwrite


@click.group(invoke_without_command=True)
@click.pass_context
def vlmd(ctx):
    click.secho(ctx.invoked_subcommand)
    if ctx.invoked_subcommand is None:
        # For the validate and extract, prompts are put here rather than in subcommand options/args 
        # as this is intended for user unfamiliar with CLI.

        subcommand = click.prompt(
            text=prompt_subcmds,
            type=click.Choice(subcmds)

        )

        if subcommand == "extract":
            inputtype = click.prompt(
                text=prompt_extract_inputtypes,
                type=click.Choice(choice_fxn.keys())

            )
            inputfile = click.prompt(
                text=prompt_inputfile,
                type=click.Path(exists=True)
            )

            outputfile,output_overwrite = _prompt_outputfile_overwrite(prompt_extract_outputfile)



        elif subcommand == "validate":

            inputfile = click.prompt(
                text=prompt_inputfile,
                type=click.Path(exists=True)
            )

        elif subcommand == "template":
            outputfile = click.prompt(
                text=prompt_template_outputfile,
                type=click.Path()
            )
            nfields = click.prompt(
                text=prompt_template_nfields,
                type=int
            )
            outputfile,output_overwrite = _prompt_outputfile_overwrite(prompt_template_outputfile)

        


@vlmd.command(help="Write a template to get started from scratch")
@click.argument("outputfile",type=click.Path())
@click.option('--overwrite-outputfile',is_flag=True,help=prompt_overwrite)
@click.option("--nfields",type=int,help=prompt_template_nfields)
def template(outputfile,nfields):
    write_vlmd_template(outputfile,output_overwrite,nfields=nfields)

@vlmd.command()
@click.argument("inputfile",type=click.Path(exists=True))
#TODO: --output-file or --output-filepath?
@click.option('--outputfile',default="heal-data-dictionary.json",help=prompt_extract_outputfile)
@click.option('--inputtype',type=click.Choice(list(choice_fxn.keys())),help=prompt_extract_inputtypes)
@click.option('--overwrite-outputfile',is_flag=True,help=prompt_overwrite)
def extract(inputfile,outputfile,inputtype,overwrite_outputfile):

    data_dictionary_props = {}

    if inputtype == "sas":
        sas_catalog_search = list(Path(inputfile).parent.glob("*.sas7bcat"))
        if len(sas_catalog_search) == 1:
            sas_catalog_filepath = sas_catalog_search[0]
            click.secho(f"Using the SAS Catalog File: {str(sas_catalog_filepath)}")
        elif len(sas_catalog_search) > 1:
            sas_catalog_filepath = sas_catalog_search[0]
            click.secho(f"Warning: Found multiple SAS Catalog files")
            click.secho(f"Using the SAS Catalog File: {str(sas_catalog_filepath)}")
        else:
            sas_catalog_filepath = None
            click.secho("No sas catalog file found so value labels will not be applied")
    
    else:
        sas_catalog_filepath = None
    #save dds and error reports to files
    data_dictionaries = convert_to_vlmd(
        input_filepath=inputfile,
        data_dictionary_props=data_dictionary_props,
        output_filepath=outputfile,
        inputtype=inputtype,
        sas_catalog_filepath=sas_catalog_filepath,
        overwrite_output_file=overwrite_outputfile
    )

@vlmd.command()
@click.argument("filepath",type=click.Path(exists=True))
@click.option('--outputfile',default="heal-data-dictionary.json",help="Write the report to a file")
def validate(filepath,outputfile):

    ext = Path(filepath).suffix.replace(".","")

    if ext == "csv":
        package = validate_vlmd_csv(filepath, to_sync_fields=True)
        report = package["report"]
    elif ext == "json":
        package = validate_vlmd_json(filepath)
        report = package["report"]
    else:
        raise Exception("Need to specify either a csv or json file")

    if outputfile:
        Path(outputfile).write_text(
            json.dumps(report, indent=4)
        )
    else:
        #TODO: color code; more informative errors
        click.secho(json.dumps(report, indent=4))
         

        
if __name__=='__main__':
    vlmd()