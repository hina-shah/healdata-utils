""" utilities to validate data and metadata """ 
import jsonschema
import os
import pandas as pd
import json

from healdata_utils.schemas import healjsonschema,healcsvschema
from healdata_utils.io import read_table
from healdata_utils.transforms.frictionless.conversion import convert_frictionless_to_jsonschema


class TabularValidator:
   
    @classmethod
    def from_csv_file(cls,path,schema,schema_type):
        data = read_table(path)
        return cls(data,schema,schema_type)

    @classmethod
    def from_pandas(cls,df,schema,schema_type):
        data = df.to_dict(orient="records")
        return cls(data,schema,schema_type)
    
    @classmethod 
    def from_jsonarray(cls,jsonarray,schema,schema_type):
        return cls(jsonarray,schema,schema_type)

    @classmethod
    def from_jsonfile(cls,path,schema,schema_type):
        data = json.loads(Path(path).read_text())
        return cls(jsonarray,schema,schema_type)

    def __init__(self,jsonarray,schema,schema_type):

        self.data = jsonarray
        self.schema = schema
        self.schematype = schema_type

        return self

    def against_frictionless(self):
        raise NotImplementedError("Not implemented yet. Use against_jsonschema with inputtype='frictionless'")

    def against_jsonschema(self):

        if self.schema_type=="frictionless":
            schema = convert_frictionless_to_jsonschema(schema)

        return validate_against_jsonschema(self.data,schema)

    def against_pandera(self):
        raise NotImplementedError("Still need to implement conversions and validation fxns")

    def raise_invalid_error(self):
        if not self.report["valid"]:
            raise Exception("These records are not valid")


    def validate(self,validation_schema_type):
        if validation_schema_type=="jsonschema":
            return self.against_jsonschema()
        else:
            raise NotImplementedError(f"{validation_schema_type} not implemented")



def validate_vlmd_json(
    data_or_path,
    schema=healjsonschema,
    input_spec="jsonschema",
    validation_spec="jsonschema"
    ):
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
        validator = TabularValidator.from_jsonfile(data_or_path,schema,"jsonschema")
    else:
        validator = TabularValidator.from_jsonarray(data_or_path,schema,"jsonschema")
    
    report = validator.validate(validation_spec)

    return report
    
def validate_vlmd_csv(
    data_or_path,
    schema=healcsvschema,
    input_spec="frictionless",
    validation_spec="jsonschema"
):
    """
    Validates a json array against the heal variable level metadata
    schema catered for a CSV tabular data dictionary file.

    As there are many options to validate a tabular data file, 
    this function provides options for different different specification
    conversions. The default is to input a frictionless schema and run
    validation with jsonschema library 
    NOTE: (the frictionless v4 tools have some
    issues with pyinstaller currently (haven't tried frictionless v5 though)) 

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
        validator = TabularValidator.from_csv_file(data_or_path,input_spec)
    else:
        validator = TabularValidator.from_jsonarray(data_or_path,input_spec)
    
    report = validator.validate(data,schema)

    return report


    

        


