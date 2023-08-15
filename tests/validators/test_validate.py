from healdata_utils.validators.validate import validate_vlmd_csv, validate_vlmd_json
import json
import os

# validate_vlmd_csv
def test_validate_vlmd_csv_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": "1=var1|2=var2",
        },
        {"name": "field1", "type": "hello", "encodings": "1"},
    ]
    package = validate_vlmd_csv(data)
    with open("tests/criteria_data/validators/validate_vlmd_csv_check1.json", 'r') as fp:
        package_check = json.load(fp)
    test_passed = package == package_check

    assert test_passed


# validate_vlmd_json
def test_validate_vlmd_json_with_data():
    data = {
        "title":"This is a test",
        "description":"This is a test",
        "data_dictionary": [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": {"1": "var1", "2": "var2"},
            "type": "float",
        },
        {"name": "field2", "encodings": "1"},
    ]
    }
    package = validate_vlmd_json(data)
    with open("tests/criteria_data/validators/validate_vlmd_json_check1.json", 'r') as fp:
        package_check = json.load(fp)

    # check for presence of properties
    assert package.keys()==package_check.keys()

    # check property data individually
    for prop in list(package):
        assert package[prop] == package_check[prop],f" Assertion error for property: {prop} "
