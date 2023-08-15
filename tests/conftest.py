import pytest 
from pathlib import Path
from healdata_utils.cli import choice_fxn
import json

@pytest.fixture(scope="module")
def fields_propname():
    return "data_dictionary"

@pytest.fixture(scope="module")
def valid_input_params():
    inputdir = Path("data/valid/input")
    data_dictionary_props = {
        "description": (
            "This is a proof of concept to demonstrate"
            " the healdata-utils functionality"
        ),
        "title": "Healdata-utils Demonstration Data Dictionary",
    }
    get_input_params = lambda input_filepath: {"filepath":inputdir.joinpath(input_filepath),"data_dictionary_props":data_dictionary_props}
    input_params = {
        "data.csv":{
            **get_input_params("data_csv_dataset1.data.csv"),
            "inputtype":"data.csv"
        },
        "sas7bdat":{**get_input_params("sas-nmhss-2019/data.sas7bdat"),
            "sas7bcat_filepath":inputdir.joinpath("sas-nmhss-2019/formats.sas7bcat")
        }, #TODO: reduce data so easier to manage and test
        "dta":get_input_params("stata_dta_dataset1.dta"),
        # "sav":get_input_params("../../JCOIN_NORC_Omnibus_SURVEY3_June2020.sav"),
        "sav":get_input_params("spss_sav_dataset1.sav"),
        "redcap.csv":get_input_params("redcap_dd_export.redcap.csv"),
        "frictionless.schema.json":get_input_params("frictionless_dataset1.frictionless.schema.json")
    }
    return input_params

@pytest.fixture(scope="module")
def valid_output_json():
    path = Path("data/valid/output")
    filenames = {
        "data.csv":"heal_dd_from_csv_data_dataset1.json",
        "sas7bdat":"heal_dd_from_sas7bdat_with_sas7bcat.json", #TODO: reduce data so easier to manage and test
        "dta":"heal_dd_from_stata_dta_dataset1.json",
        "sav":"heal_dd_from_spss_sav_dataset1.json",
        "redcap.csv":"heal_dd_from_redcap_dd_export.json",
        "frictionless.schema.json":"heal_dd_from_frictionless_schema.json"
    }
    jsons = {}
    for inputtype,name in filenames.items():
        if inputtype in choice_fxn:
            jsons[inputtype] = json.loads(path.joinpath(name).read_text())
        else:
            raise Exception("Inputtype not in registered fxns")
            
    return jsons

@pytest.fixture(scope="module")
def valid_output_csv():
    path = Path("data/valid/output")
    filenames = {
        "data.csv":"heal_dd_from_csv_data_dataset1.csv",
        "sas7bdat":"heal_dd_from_sas7bdat_with_sas7bcat.csv",#TODO: reduce data so easier to manage and test
        "dta":"heal_dd_from_stata_dta_dataset1.csv",
        "sav":"heal_dd_from_spss_sav_dataset1.csv",
        "redcap.csv":"heal_dd_from_redcap_dd_export.csv",
        "frictionless.schema.json":"heal_dd_from_frictionless_schema.csv"
    }
    csvs = {}
    for inputtype,name in filenames.items():
        if inputtype in choice_fxn:
            csvs[inputtype] = path.joinpath(name).read_text().split("\n")
        else:
            raise Exception("Inputtype not in registered fxns")
            
    return csvs


    