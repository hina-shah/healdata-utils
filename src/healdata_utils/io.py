""" 
functions to read and write files in a "smart" way
"""
import pyreadstat
import pandas as pd 
from pathlib import Path
import charset_normalizer
import re

from healdata_utils import schemas
# read pyreadstat files

def read_pyreadstat(file_path,**kwargs):
    ''' 
    reads in a "metadata rich file"
    (dta, sav,b7bdat). Note, xport format not supported
    as it doesnt supply value labels.

    '''
    file_path = Path(file_path)
    ext = file_path.suffix 
    if ext=='.sav':
        read = pyreadstat.read_sav
    elif ext=='.sas7bdat':
        read = pyreadstat.read_sas7bdat
    elif ext=='.dta':
        read = pyreadstat.read_dta
    elif ext=='.por':
        read = pyreadstat.read_por

    return read(file_path,**kwargs)



def detect_file_encoding(file_path):
    """ 
    detects file encoding using charset_normalizer package
    """ 
    with open(file_path,'rb') as f:
        data = f.read()
        encoding_for_input = charset_normalizer.detect(data)

    is_confident = encoding_for_input["confidence"]==1
    if not is_confident:
        print("Be careful, the detected file encoding for:")
        print(f"{file_path}")
        print(r"has less than 100% confidence")
    #chardet_normalizer.detect returns confidence,encoding (as a string), and language (eg English)
    return encoding_for_input["encoding"]


def read_table(file_path,castdtype = "string"):
    """ 
    reads in a tabular file (ie spreadsheet) after detecting
    encoding and file extension without any type casting.

    currently supports csv and tsv

    defaults to not casting values (ie all columns are string dtypes)
    and not parsing strings into NA values (eg "" is kept as "")
    """ 
    ext = Path(file_path).suffix
    if ext==".csv":
        sep = ","
    elif ext==".tsv":
        sep = "\t"
        
    encoding = detect_file_encoding(file_path)
    file_encoding = pd.read_csv(
        file_path,sep=sep,encoding=encoding,dtype=castdtype,
        keep_default_na=False)

    return file_encoding


def _generate_jsontemplate(schema):
    template = {}
    if 'properties' in schema:
        for prop, prop_schema in schema['properties'].items():
            if 'type' in prop_schema:
                if prop_schema['type'] == 'object':
                    template[prop] = generate_template(prop_schema)
                elif prop_schema['type'] == 'array':
                    if prop_schema.get("items"):
                        template[prop] = [generate_template(prop_schema['items'])]
                    else:
                        template[prop] = []
                else:
                    template[prop] = None
    return template

    
def write_vlmd_template(outputfile,output_overwrite=False,field_num=1):

    """ 
    Writes a  json or csv template:
    If writing a json template, will iniiate null vals for all fields
    If writing a csv template (ie csv tabular template), will copy the recommendation level across num fields specified.
    

    NOTE
    -----
    - Recommendation level is in description property with expression [<recommendation level>]. The 
    "required" property takes precdence over rec level.

    - csv is a frictionless table schema and json is a jsonschema
    """  
    

    ext = Path(outputfile).suffix 

    # if file exists and overwrite option is false, raise error
    if Path(outputfile).exists() and not output_overwrite:
        raise FileExistsError(f"{outputfile} exists")


    if ext == ".json":
        schema = schemas.healjsonschema
        fields_propname = "data_dictionary"
        template = _generate_jsontemplate(schema)
        template[fields_propname] = field_num*[template[fields_propname]]
        Path(outputfile).write_text(json.dumps(template,indent=2))
    
    elif ext == ".csv":
        schema = schemas.healcsvschema
        fields_propname = "fields"
        cols = [field["name"] for field in schema["fields"]]
        vals = [field_num* [
            "[Required]" if field.get("constraints",{}).get("required") else
            re.search("\[.*\]",field["description"]).group()
            ] for field in schema["fields"]]

        template = pd.DataFrame(vals,columns=cols)
        template.to_csv(outputfile,index=False)


