from healdata_utils.validate import validate_vlmd_csv, validate_vlmd_json


# validate_vlmd_csv
def test_validate_vlmd_csv_with_data():
    data = [
        {
            "name": "field1",
            "description": "This is a test field",
            "encodings": "1=var1|2=var2",
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
    assert not report["valid"] == False
    assert report["errors"] == [
        {
            "module": "MISSING",
            "name": "VALID",
            "title": "MISSING",
            "description": "VALID",
            "type": "ERROR'float' is not one of ['number', 'integer', 'string', 'any', 'boolean', 'date', 'datetime', 'time', 'year', 'yearmonth', 'duration', 'geopoint']",
            "format": "MISSING",
            "constraints": "MISSING",
            "encodings": "VALID",
            "ordered": "MISSING",
            "missingValues": "MISSING",
            "trueValues": "MISSING",
            "falseValues": "MISSING",
            "repo_link": "MISSING",
            "cde_id": "MISSING",
            "ontology_id": "MISSING",
            "univar_stats": "MISSING",
        },
        {
            "module": "MISSING",
            "name": "VALID",
            "title": "MISSING",
            "description": "MISSING",
            "type": "MISSING",
            "format": "MISSING",
            "constraints": "MISSING",
            "encodings": "ERROR'1' is not of type 'object'",
            "ordered": "MISSING",
            "missingValues": "MISSING",
            "trueValues": "MISSING",
            "falseValues": "MISSING",
            "repo_link": "MISSING",
            "cde_id": "MISSING",
            "ontology_id": "MISSING",
            "univar_stats": "MISSING",
        },
    ]


test_validate_vlmd_csv_with_data()
test_validate_vlmd_csv_with_path()
test_validate_vlmd_json_with_data()
