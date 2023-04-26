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
healcsvschema = requests.get(csvschema_url).json()   

def convert_frictionless_to_jsonschema():
    frictionless_fields = list(frictionless_schema.get("fields"))
    assert frictionless_fields,"A frictionless schema MUST have a set of fields"


    for field in frictionless_fields:

        # required, pattern are not nested, TODO: look into others
        constraints = field.pop("constraints",{})
        field.update(constraints)

        # enum is a type
        if "enum" in constraints:
            del field["type"]


        ## TODO: format mappings
        ## TODO: type mappings (eg bare number)

    return frictionless_fields


