import pyreadstat
import pandas as pd 
from pathlib import Path
from healdata_utils.utils import to_int_if_base10
from ..jsontemplate.conversion import convert_templatejson

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

def convert_readstat(file_path,
    data_dictionary_props={}):
    """
    Converts a "metadata-rich" (ie statistical software file) 
    into a HEAL-specified data dictionary in both csv format and json format.

    This function relies on [readstat](https://github.com/Roche/pyreadstat) which supports SPSS (sav and por), 
    SAS (sas7bdat), and Stata (dta). 

    > Currently, this function uses both data and metadata to generate 
    a HEAL specified data dictionary. That is, types are inferred from the 
    data (so at least test or synthetic data needed) in addition to the metadata 
    (ie variable labels and value labels). 

    Parameters
    ----------
    csvtemplate : str or path-like or any object
        Data or path to data with the data being a tabular HEAL-specified data dictionary.
        This input can be any data object or path-like string excepted by a frictionless Resource object.
    data_dictionary_props : dict
        The HEAL-specified data dictionary properties.
    mappings : dict, optional
        Mappings (which can be a dictionary of either lambda functions or other to-be-mapped objects).
        Default: specified fieldmap.

    Returns
    -------
    dict
        A dictionary with two keys:
            - 'templatejson': the HEAL-specified JSON object.
            - 'templatecsv': the HEAL-specified tabular template.

    """
    
    df,meta = read_pyreadstat(file_path)
    df = df.convert_dtypes() #TODO: use visions package for inference (from pandas profile project)
    fields = pd.io.json.build_table_schema(df,index=False)['fields'] #converts to frictionless Table Schema


    for field in fields:
        field.pop('extDtype',None)
        fieldname = field['name']

        value_labels = meta.variable_value_labels.get(fieldname)
        if value_labels:
            field['encodings'] = {
                to_int_if_base10(key):to_int_if_base10(val)
                for key,val in value_labels.items()
            }

            #NOTE: enums are assumed if labels represent entire set of values
            # this avoids value labels that are, for example, partials such as top/bottom encodings
            enums = set(value_labels.keys())
            values = set(df[fieldname].dropna()) 
            if not values.difference(enums):
                constraints_enums = {'constraints':{'enum':[to_int_if_base10(v) for v in enums]}}
                field.update(constraints_enums)

        #NOTE/TODO: for SPSS no functionality for incorporating missing ranges
        missing_values = meta.missing_user_values.get(fieldname)
        if missing_values:
            field['missingValues'] = {
                to_int_if_base10(key):to_int_if_base10(val)
                for key,val in missing_values.items()
            }

        variable_label = meta.column_names_to_labels.get(fieldname)
        if variable_label:
            field['description'] = variable_label

    data_dictionary = data_dictionary_props.copy()
    data_dictionary['data_dictionary'] = fields 

    package = convert_templatejson(data_dictionary)
    return package
