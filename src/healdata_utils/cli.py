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

prompt_subcmds = f"""
{click.style("SELECT ONE OF THE FOLLOWING:",fg="green",bold=True)}

{click.style("validate",bold=True)}: check (validate) an existing HEAL data dictionary to see if it maps the HEAL specifications.
{click.style("extract",bold=True)}: take an existing format and extract the variable level metadata out.
{click.style("template",bold=True)}: generate a HEAL template to fill in. 


"""

prompt_file = f"""
{click.style("What is the path to your input file?",bold=True,fg="green")}

This can be an:
1. absolute path (e.g., C:/Users/lastname-firstname/projectfolder/data/filename.csv)
2. relative path (e.g., data/filename.csv)
3. filename (e.g., filename.csv)

"""

prompt_extract_inputtypes = f"""
{click.style("What type of file do you want to extract variable level metadata from?",bold=True,fg="green")}

"""

prompt_template_nfields = f"""
{click.style("How many variables (ie fields) are in your data (ie are going to be in your data dictionary)?",bold=True,fg="green")}

""" 

prompt_template_outputfile = f"""

{click.style("What do you want the output file called?",bold=True,fg="green")}

This can be an:
1. absolute path (e.g., C:/Users/lastname-firstname/projectfolder/heal-data-dictionary.csv)
2. relative path (e.g., heal-data-dictionary.csv)
3. filename (e.g., heal-data-dictionary.csv)

Note, if you specify a csv file, this will generate a HEAL csv templated file and if you specify a json file, this
will generate a HEAL json templated file.

""" 
prompt_extract_outputfile = f""" 

{click.style("What do you want the output file called?",bold=True,fg="green")}

Note, whether you specify a json or csv, both formats will be generated for convenience 
(i.e., heal-dd.json generates heal-dd.json and heal-dd.csv)

"""

prompt_overwrite = f"""

{click.style("Do you want to overwrite the specified output files (if they exist)?",bold=True,fg="green")}

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
        click.secho(f"File must be {' or '.join(fileexts)}",fg="red")
        outputfile,outputfile_overwrite = _prompt_outputfile_overwrite(outputfile_prompt)
    else:
        if outputfile_csv.exists():
            click.secho(f"Warning: {outputfile_csv} exists",fg="red")

        if outputfile_json.exists():
            click.secho(f"Warning: {outputfile_json} exists",fg="red")  

        if outputfile_json.exists() or outputfile_csv.exists():
            outputfile_overwrite = click.confirm(prompt_overwrite)
            if not outputfile_overwrite:
                outputfile,outputfile_overwrite = _prompt_outputfile_overwrite(outputfile_prompt)

    return outputfile,outputfile_overwrite

def _prompt_arg(ctx,param,value):
    pass 


@click.group(invoke_without_command=True)
@click.pass_context
def vlmd(ctx):
    if ctx.invoked_subcommand is None:
        # For the validate and extract, prompts are put here rather than in subcommand options/args 
        # as this is intended for user unfamiliar with CLI.

        subcmds = vlmd.list_commands(ctx)
        subcmd = click.prompt(text=prompt_subcmds,
            type=click.Choice(subcmds)
        )
        # invoke subcommand chosen with "all bells and whistles"
        #NOTE: for Command.main method:
        # https://github.com/pallets/click/blob/b63ace28d50b53e74b5260f6cb357ccfe5560133/src/click/core.py#L1255
        ctx.command.commands[subcmd].main()
        

@vlmd.command(help="Write a template to get started from scratch",callback=add_arg)
@click.argument("file",type=click.Path(),
    default=click.prompt(text=prompt_template_outputfile,type=click.Path()))
@click.option('--overwrite',default=False,is_flag=True)
@click.option("--nfields",default=1,type=int,prompt=prompt_template_nfields)
def template(file,overwrite,nfields):
    write_vlmd_template(outputfile,output_overwrite=overwrite,nfields=nfields)

@vlmd.command(help="Extract the variable level metadata into HEAL compliant format.")
@click.argument("file",type=click.Path(exists=True),
    default=click.prompt(text=prompt_template_outputfile,type=click.Path(exists=True)))
#TODO: --output-file or --output-filepath?
@click.option('--inputtype',type=click.Choice(list(choice_fxn.keys())),prompt=prompt_extract_inputtypes)
@click.option('--outputfile',
    default="heal-data-dictionary.json",
    prompt=prompt_extract_outputfile,
    callback=_prompt_outputfile_overwrite(outputfile_prompt))
@click.option('--overwrite',default=False,is_flag=True)
def extract(file,outputfile,inputtype,overwrite):

    data_dictionary_props = {}

    if inputtype == "sas":
        sas_catalog_search = list(Path(file).parent.glob("*.sas7bcat"))
        if len(sas_catalog_search) == 1:
            sas_catalog_filepath = sas_catalog_search[0]
            click.secho(f"Using the SAS Catalog File: {str(sas_catalog_filepath)}",fg="green")
        elif len(sas_catalog_search) > 1:
            sas_catalog_filepath = sas_catalog_search[0]
            click.secho(f"Warning: Found multiple SAS Catalog files",fg="red")
            click.secho(f"Using the SAS Catalog File: {str(sas_catalog_filepath)}")
        else:
            sas_catalog_filepath = None
            click.secho("No sas catalog file found so value labels will not be applied")
    
    else:
        sas_catalog_filepath = None
    #save dds and error reports to files
    data_dictionaries = convert_to_vlmd(
        input_filepath=file,
        data_dictionary_props=data_dictionary_props,
        output_filepath=outputfile,
        inputtype=inputtype,
        sas_catalog_filepath=sas_catalog_filepath,
        overwrite_output_file=overwrite
    )

@vlmd.command("check (validate) an existing HEAL data dictionary to see if it maps the HEAL specifications.")
@click.argument("file",type=click.Path(exists=True))
@click.option('--outputfile',default="heal-data-dictionary.json",help="Write the report to a file")
def validate(file,outputfile):

    ext = Path(file).suffix.replace(".","")

    if ext == "csv":
        package = validate_vlmd_csv(file, to_sync_fields=True)
        report = package["report"]
    elif ext == "json":
        package = validate_vlmd_json(file)
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