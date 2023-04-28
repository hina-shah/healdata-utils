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



