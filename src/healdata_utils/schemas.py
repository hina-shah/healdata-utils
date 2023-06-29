import requests

jsonschema_url = (
    "https://raw.githubusercontent.com/norc-heal/"
    "heal-metadata-schemas/mbkranz/variable-lvl-dev/"
    "variable-level-metadata-schema/schemas/jsonschema"
)
csvschema_url = (
    "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
    "mbkranz/variable-lvl-dev/"
    "variable-level-metadata-schema/schemas/frictionless/csvtemplate/fields.json"
)

# NOTE: replaces relative fields.json with fields 
# TODO: install schemas from pip or make it a submodule (so no GET call necessary for fields.json)
healjsonschema = requests.get(jsonschema_url+"/data-dictionary.json").json()
healjsonschema["properties"]["data_dictionary"]["items"] = requests.get(jsonschema_url+"/fields.json").json()
healcsvschema = requests.get(csvschema_url).json()
