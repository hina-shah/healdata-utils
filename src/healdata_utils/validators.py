""" utilities to validate data and metadata """ 
import jsonschema
import os
import pandas as pd
import json

from healdata_utils.schemas import healjsonschema,healcsvschema
from healdata_utils.io import read_table

def _validate_property(record,schema):
    try:
        jsonschema.validate(record,schema=schema)
        return (True,"")
    except jsonschema.exceptions.ValidationError as e:
        return (False,e.message) 
        
def validate_record(record,schema):
    errors = {}
    is_valid = True
    for propname,prop in schema.get("properties",{}):
        instance = record.get(propname,None)
        if instance:
            is_valid,error_message = _validate_property(instance,prop)
        elif not instance and propname in schema.get("required",[]):
            error_message = "required but missing"
            is_valid = False
        else:
            is_valid = True
            error_message = ""

        errors[propname] = error_message
    
    return is_valid,errors


def validate_records(records,schema):
    table_errors = []
    is_valid = True
    for record in records:
        is_valid,record_errors = validate_record(record,schema)
        table_errors.append(errors)
    return is_valid,table_errors

def validate(jsonarray,schema,raise_valid_error=False,):
    """
    Validates a json array of records against a specified JSON schema's properties.
    This is done by by iterating over every property in every record and comparing to the property 
    specified in the given schema.

    Parameters
    ----------
    jsonarray : list[dict]
        The list of fields to validate.
    schema : dict
        The JSON schema to be validated against.

    Returns
    -------
    dict[dict,dict]
        an object indicating whether all records are valid and an array of object containing error messages 
        (this array has the same dimensions as the json array of records x the properties in the schema)
        (eg., `{"valid":False,"errors":[{"field1":"required but missing","field2":""}]}`)

    Raises
    ------
    Exception
        If `raise_valid_error` is `True` and the validation fails.

    Notes
    -----
    This function uses the `jsonschema` package for validation.

    """
    is_valid,errors = validate_records(data_dictionary,schema)

    if raise_valid_error and is_valid:
        raise Exception("These records are not valid")

    return {"valid":is_valid,"errors":errors}


def validate_vlmd_json(data_or_path,schema=healjsonschema):
    """
    Validates json data by iterating over every property in every record and comparing to the property 
    specified in the given schema

    Parameters
    ----------
    data_or_path : Path-like object indicating a path to a tabular data source (eg CSV or TSV) or a json array of records (see validate fxn)
    schema : dict, optional
        The schema to compare data_or_path to (default: HEAL frictionless template)

    Returns
    -------
    dict[bool,dict]
        the returned `validate` function object 
        (eg., `{"valid":False,"errors":[{"field1":"required but missing","field2":""}]}`)
    """

    if isinstance(data_or_path, (str, os.PathLike)):
        data = json.loads(Path(data_or_path).read_text())
    else:
        data = data_or_path
    
    report = validate(data,schema)

    return report
    
def validate_vlmd_csv(data_or_path,schema=healcsvschema):
    """
    Validates a json array against the heal variable level metadata
    schema catered for a CSV tabular data dictionary file.

    Parameters
    ----------
    data_or_path : Path-like object indicating a path to a tabular data source (eg CSV or TSV) or a json array of records (see validate fxn)
    schema : dict, optional
        The schema to compare data_or_path to (default: HEAL frictionless template)

    Returns
    -------
    dict[bool,dict]
        the returned `validate` function object 
        (eg., `{"valid":False,"errors":[{"field1":"required but missing","field2":""}]}`)
    """

    if isinstance(data_or_path, (str, os.PathLike)):
        data = read_table(data_or_path)
    else:
        data = data_or_path
    
    report = validate(data,schema)

    return report