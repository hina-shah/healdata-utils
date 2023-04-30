from healdata_utils.validators.validate import validate_vlmd_csv, validate_vlmd_json


# validate_vlmd_csv
def test_validate_vlmd_csv_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": "1=var1|2=var2",
        },
        {"name": "field2", "encodings": "1"},
        {
            "name": "field1",
            "type":"hello",
            "encodings": "1"
        },
        {"name": "field2", "encodings": "1"},
    ]
    report = validate_vlmd_csv(data)


def test_validate_vlmd_csv_with_path():
    dd_path = "data/invalid_vlmd.csv"


# validate_vlmd_json
def test_validate_vlmd_json_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": {1: "var1", 2: "var2"},
            "type": "float",
        },
        {"name": "field2", "encodings": "1"},
    ]
    report = validate_vlmd_json(data)
    assert not report["valid"]
    assert report["errors"] == {
        'valid': False, 
        'errors': [
            {'json_path': '$', 
            'message': "[{'name': 'field1', 'description': 'This is a test field', 'encodings': {1: 'var1', 2: 'var2'}, 'type': 'float'}, {'name': 'field2', 'encodings': '1'}] is not of type 'object'"}
        ]}


test_validate_vlmd_csv_with_data()
test_validate_vlmd_csv_with_path()
test_validate_vlmd_json_with_data()
