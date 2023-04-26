import jsonschema
import requests
# currently using fields.json and hardcoding 
jsonschema_url = (
"https://raw.githubusercontent.com/norc-heal/"
"heal-metadata-schemas/mbkranz/variable-lvl-csvs/"
"variable-level-metadata-schema/schemas/jsonschema/fields.json"
)
csvschema_url = (
        "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
        "mbkranz/variable-lvl-csvs/"
        "variable-level-metadata-schema/schemas/frictionless/csvtemplate/fields.json"
    )

healjsonschema = requests.get(jsonschema_url).json()
healcsv = requests.get(csvschema_url).json()

def validate_json(data_dictionary,raise_valid_error=False,schema=healjsonschema):
    """
    Validates the `data_dictionary` fields property against the specified JSON schema.

    Parameters
    ----------
    data_dictionary : list[dict]
        The list of fields to validate.
    raise_valid_error : bool, optional
        If `True`, raises an exception if the validation fails.
        Default is `False`.
    schema : dict, optional
        The JSON schema to be validated against.
        Default is `schema`.

    Returns
    -------
    tuple
        A tuple containing the validated `data_dictionary` and the JSON schema
        validation error report in the form of a dictionary.

    Raises
    ------
    Exception
        If `raise_valid_error` is `True` and the validation fails.

    Notes
    -----
    This function uses the `jsonschema` package for validation.
    """
    try:
        print(f'Validating heal-specified json fields.....')
        jsonschema.validate(data_dictionary,schema=schema)
        report = {"valid":True}
        print(f"JSON array of data dictionary fields is VALID")
    except jsonschema.exceptions.ValidationError as e:
        report = e.__dict__
        report['valid'] = False
        if raise_valid_error:
            raise Exception(f"Data dictionary not valid: {e.message}")
            
        
    return data_dictionary,report


def validate_csv(data_or_path,schema=healcsv):
    """
    Validates tabular data by ordering columns according to a schema
    with frictionless Table Schema standards profile and adds missing
    columns before validating.

    Parameters
    ----------
    data_dict_or_path : str or Path or anything excepted by frictionless Resource data
        data parameter (eg array of fields in the correct specification for csv)
        Path to data with the data being a tabular HEAL-specified data dictionary
    schema : dict, optional
        The schema to compare data_or_path to (default: HEAL frictionless template)

    Returns
    -------
    List[dict]
        Tabular data in the form of an array of dictionaries for each field (ie keyed) and the validation report
    Report
        frictionless report object
    Notes
    -----
    Currently, in contrast to the `validate_json` function, this validates only
    at the field level.
    """

    #return data_tbl,report

    pass 
