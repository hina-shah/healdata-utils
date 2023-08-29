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
# TODO: vlmd group that invokes input prompts and directs towards one of the three sub commands
# TODO: validate takes in either a heal specified json or a csv and validates
@click.group()
def vlmd():
    pass 

@vlmd.command("quick-start")
def quick_start():
    pass 

@vlmd.command()
@click.argument("inputfile",type=click.Path(exists=True))
#TODO: --output-file or --output-filepath?
@click.option('--outfile',default="",help='File path (or file name) where you want to output your HEAL data dictionary')
@click.option('--inputtype',required=True,type=click.Choice(list(choice_fxn.keys())),help='The type of your input file.')
@click.option('--title',default=None,help='The title of your data dictionary. If not specified, then the file name will be used')
@click.option('--description',default=None,help='Description of data dictionary')
def extract(inputfile,outfile,inputtype,title,description):

    data_dictionary_props = {'title':title,'description':description}

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
        output_filepath=outfile,
        inputtype=inputtype,
        sas_catalog_filepath=sas_catalog_filepath
    )

#TODO: 
@vlmd.command()
@click.argument("filepath",type=click.Path(exists=True))
@click.option("--outfile",default=None)
def validate(filepath):
    ext = Path(filepath).suffix.replace(".","")

    if ext == "csv":
        package = validate_vlmd_csv(file, to_sync_fields=True)
        report = package["report"]
    elif ext == "json":
        package = validate_vlmd_json(file)
        report = package["report"]
    else:
        raise Exception("Need to specify either a csv or json file")

    if output_filepath:
        Path(outfile).write_text(
            json.dumps(report, indent=4)
        )
    else:
        #TODO: color code; more informative errors
        click.echo_via_pager(json.dumps(report, indent=4))
         

        
if __name__=='__main__':
    vlmd()