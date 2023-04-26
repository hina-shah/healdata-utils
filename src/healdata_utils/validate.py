""" utilities to validate data and metadata """ 
import jsonschema
import os
import pandas as pd
import json

from healdata_utils.schemas import healjsonschema,healcsvschema
from healdata_utils.io import read_table

def __validate_property(instance,property_in_schema):
    try:
        jsonschema.validate(instance,schema=property_in_schema)
        return "VALID"
    except jsonschema.exceptions.ValidationError as e:
        return "ERROR"+e.message
        
def _validate_record(record,schema):
    report = {}
    is_valid = True
    for propname,prop in schema.get("properties",{}).items():
        is_required = propname in schema.get("required",False)
        instance = record.get(propname,{})

        if instance:
            error_message = __validate_property(instance,prop)
        elif not instance and is_required:
            error_message: "ERROR:required"
        elif not instance and not is_required:
            error_message = "MISSING"

        report[propname] = error_message

        #if a property is missing or valid it is "valid"
        if not error_message in ["VALID","MISSING"]:
            is_valid = False
    
    return is_valid,report


def validate_records(records,schema):
    table_report = []
    is_valid = True
    for record in records:
        is_valid,record_report = _validate_record(record,schema)
        if not is_valid:
            is_valid = False

        table_report.append(record_report)

    return {"valid":is_valid,"errors":table_report}

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
    report = validate_records(jsonarray,schema)

    if raise_valid_error and report["valid"]:
        raise Exception("These records are not valid")

    return report


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