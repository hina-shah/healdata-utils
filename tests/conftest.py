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
    input_params = {
        "dta":{"filepath":inputdir.joinpath("stata_dta_dataset1.dta"),"data_dictionary_props":data_dictionary_props},
        "sav":{"filepath":inputdir.joinpath("spss_sav_dataset1.sav"),"data_dictionary_props":data_dictionary_props},
        "redcap.csv":{"filepath":inputdir.joinpath("redcap_dd_export.redcap.csv"),"data_dictionary_props":data_dictionary_props},
    }
    return input_params

@pytest.fixture(scope="module")
def valid_output_json():
    path = Path("data/valid/output")
    filenames = {
        "dta":"heal_dd_from_stata_dta_dataset1.json",
        "sav":"heal_dd_from_spss_sav_dataset1.json",
        "redcap.csv":"heal_dd_from_redcap_dd_export.json",
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
        "dta":"heal_dd_from_stata_dta_dataset1.csv",
        "sav":"heal_dd_from_spss_sav_dataset1.csv",
        "redcap.csv":"heal_dd_from_redcap_dd_export.csv",
    }
    csvs = {}
    for inputtype,name in filenames.items():
        if inputtype in choice_fxn:
            csvs[inputtype] = path.joinpath(name).read_text().split("\n")
        else:
            raise Exception("Inputtype not in registered fxns")
            
    return csvs


    