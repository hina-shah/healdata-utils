''' 

command line interface for generating HEAL data dictionary/vlmd json files

''' 

from healdata_utils.transforms.csvtemplate.conversion import convert_templatecsv
from healdata_utils.transforms.jsontemplate.conversion import convert_templatejson
from healdata_utils.transforms.readstat.conversion import convert_readstat
from healdata_utils.transforms.redcapcsv.conversion import convert_redcapcsv
from healdata_utils.transforms.csvdata.conversion import convert_datacsv
from healdata_utils.transforms.frictionless.conversion import convert_frictionless_tableschema

from healdata_utils.validators.validate import validate_vlmd_json,validate_vlmd_csv
import json
from pathlib import Path
import petl as etl
import pandas as pd
import csv
from collections import deque

from healdata_utils.utils import find_docstring_desc

choice_fxn = {
    'csv-data':convert_datacsv,
    #'csv-data-dictionary':convert_datadictcsv,
    #'template.csv':convert_templatecsv,
    #'csv': convert_templatecsv, #maintained for backwards compatibility
    'spss': convert_readstat,
    'stata':convert_readstat,
    #'por':convert_readstat,
    'sas':convert_readstat,
    #'template.json':convert_templatejson,
    #'json':convert_templatejson, #maintain for bwds compat
    "redcap":convert_redcapcsv,
    "frictionless":convert_frictionless_tableschema

}

input_types = " - "+"\n - ".join(list(choice_fxn.keys()))

input_descriptions = {
    name:find_docstring_desc(fxn)
    for name,fxn in choice_fxn.items()
}


def _write_vlmd(jsontemplate,csvtemplate,csvreport,jsonreport,output_filepath=None):
    # NOTE: currently the default is to auto generate file name if output_filepath not specified

    # flipped wording around for vars
    templatejson = jsontemplate
    templatecsv = csvtemplate
    reportjson = csvreport
    reportcsv = jsonreport
    
    if output_filepath:
        output_filepath = Path(output_filepath)
        jsontemplate_path = output_filepath.with_suffix(".json")
        csvtemplate_path = output_filepath.with_suffix(".csv")
    else:
        jsontemplate_path = "heal-json-data-dictionary.json"
        csvtemplate_path = "heal-csv-data-dictionary.csv"
    # check existence of directory and output files
    dir_exists = output_filepath.parent.exists()
    json_exists = jsontemplate_path.exists()
    csv_exists = csvtemplate_path.exists()

    if not dir_exists:
        raise FileNotFoundError(f"{str(output_filepath.parent)} does not exist so cannot create {output_filepath.name}")
    elif json_exists and csv_exists:
        raise FileExistsError(f"{str(jsontemplate_path)}\nand\n{str(csvtemplate_path)}\nexist.")
    elif json_exists:
        raise FileExistsError(f"{str(jsontemplate_path)} exists.")
    elif csv_exists:
        raise FileExistsError(f"{str(csvtemplate_path)} exists.")



    # print data dictionaries
    jsontemplate_path.write_text(json.dumps(templatejson,indent=4))

    quoting = csv.QUOTE_NONNUMERIC if output_csv_quoting else csv.QUOTE_MINIMAL
    # NOTE: quoting non-numeric to allow special characters for nested delimiters within string columns (ie "=")
    # (
    #     etl.fromdicts(templatecsv)
    #     .tocsv(
    #         csvtemplate_path,
    #         quoting=csv.QUOTE_NONNUMERIC if output_csv_quoting else csv.QUOTE_MINIMAL)

    # )
    pd.DataFrame(templatecsv).to_csv(csvtemplate_path,quoting=quoting,index=False)

    # print errors

    if not report_json['valid']:
        print("JSON data dictionary not valid, see heal-json-errors.json for errors.")
        print(f"(view the outputted data dictionary at {jsontemplate_path})")

    if not report_csv['valid']:
        print("CSV data dictionary not valid, see heal-csv-errors.json")
        print(f"(view the outputted data dictionary at {csvtemplate_path})")
    
    # write error reports to file
    errordir = Path(output_filepath).parent.joinpath('errors')
    errordir.mkdir(exist_ok=True)
    errordir.joinpath('heal-json-errors.json').write_text(
        json.dumps(report_json,indent=4)
    )
    errordir.joinpath('heal-csv-errors.json').write_text(
        json.dumps(report_csv,indent=4)
    )




def convert_to_vlmd(
    input_filepath,
    data_dictionary_props={},
    inputtype=None,
    output_filepath=None,
    sas_catalog_filepath=None,
    output_csv_quoting=None,
    **kwargs
    ):
    """
    Writes a data dictionary (i.e. variable level metadata) to a HEAL metadata JSON file using a registered function.

    Parameters
    ----------
    input_filepath : str
        Path to input file. See documentation on individual input types for more details.
    output_filepath : str
        output file path or directory to where output will go. Note, the extension specified (csv or json will change as necessary)
    data_dictionary_props : dict, optional
        The other data-dictionary level properties. By default, will give the data_dictionary `title` property as the file name stem.
    inputtype : str, optional
        The input type. If none specified, will default to using the file extension.
        See the currently registered input types in the input_types list.
    sas_catalog_filepath: str,optional
        Path to a sas catalog file (sas7bcat). Needed for value formats if a sas (sas7bdat) input file
    output_csv_quoting: bool, optional
        If true, all nonnumeric values will be quoted. This helps reduce ambiguity for programs
        like excel that uses special characters for specific purposes (eg = for formulas)
    
    Returns
    -------
    dict
        Dictionary with:
         1. csvtemplated array of fields.
         2. jsontemplated data dictionary object as specified by an originally drafted design doc.
            That is, a dictionary with title:<title>,description:<description>,data_dictionary:<fields>
            where data dictionary is an array of fields as specified by the JSON schema.
         3. error objects for corresponding validators (ie frictionless for csv and jsonschema for json)
    NOTE
    ----
    In future versions, this will be more of a package bundled with corresponding schemas (whether csv or JSON),better organization 
    (e.g., see frictionless Package). 
    However, right now, it simply returns the csvtemplate and jsontemplate as specified
    in the heal specification repository.
    This is an intermediate solution to socialize a proof-of-concept.

    TODO
    --------
    make sub command for each file format rather than just one function? Added sas7bcat and can predict additional complexity
    
    """

    input_filepath = Path(input_filepath)
    
    #infer input type
    if not inputtype:
        ext = ''.join(input_filepath.suffixes)[1:].lower()
        inputtype = ext_to_inputtype.get(ext)
        if not inputtype:
            raise Exception(f"No inputtype specified as file of type {ext} does not have a registered inputtype")

    # backwards compatability
    if sas7bcat_filepath:
        sas_catalog_filepath = sas7bcat_filepath

    ## add dd title
    if not data_dictionary_props.get('title'):
        data_dictionary_props['title'] = input_filepath.stem


    # get data dictionary package based on the input type
    if inputtype=="sas":
        if sas_catalog_filepath:
            data_dictionary_package = choice_fxn[inputtype](input_filepath,data_dictionary_props,sas7bcat_file_path=sas_catalog_filepath) 
    else:
        data_dictionary_package = choice_fxn[inputtype](input_filepath,data_dictionary_props)


    #TODO: json validate root AND fields while csv currently only validates fields (ie table) but no reason it cant validate entire data package
    package_csv = validate_vlmd_csv(data_dictionary_package['templatecsv']['data_dictionary'],to_sync_fields=True)
    package_json = validate_vlmd_json(data_dictionary_package['templatejson'])

    # TODO: in future just return the packages (eg reports nested within package and not out of)
    # for now, keep same (report_xxx and templatexxx)

    report_csv = package_csv["report"]
    report_json = package_json["report"]
    dd_csv = package_csv["data"]
    dd_json = package_json["data"]

    # write to file
    _write_vlmd(jsontemplate=dd_json,csvtemplate=dd_csv,csvreport=report_csv,
        jsonreport=report_json,output_filepath=output_filepath)
    # format csv and json paths
 
    return {
        "csvtemplate":dd_csv,
        "jsontemplate":dd_json,
        "errors":{
            "csvtemplate":report_csv,
            "jsontemplate":report_json}
        }