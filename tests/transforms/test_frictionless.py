from healdata_utils.transforms.frictionless import convert_frictionless_to_jsonschema
from healdata_utils.schemas.frictionless import healcsvschema
from pathlib import Path
import yaml
import json

#%%
def test_convert_frictionless_to_jsonschema():
    frictionless_input_schema = healcsvschema
    jsonschema_props = convert_frictionless_to_jsonschema(frictionless_input_schema)
    with open("tests/criteria_data/transforms/frictionless/convert_frictionless_to_jsonschema_check1.json", "r") as fp:
        jsonschema_props_check = json.load(fp)
    test_passed = jsonschema_props == jsonschema_props_check

    assert test_passed,"Assertion statement for conversion from frictonless to jsonschema failed"
