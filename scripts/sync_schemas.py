import requests
from pathlib import Path
import pprint
def copy_schemas():
    pp = pprint.PrettyPrinter(indent=2,compact=True, sort_dicts=False)
    jsonschema_url = (
        "https://raw.githubusercontent.com/norc-heal/"
        "heal-metadata-schemas/mbkranz/variable-lvl-dev/"
        "variable-level-metadata-schema/schemas/jsonschema/data-dictionary.json"
    )
    csvschema_url = (
        "https://raw.githubusercontent.com/norc-heal/heal-metadata-schemas/"
        "mbkranz/variable-lvl-dev/"
        "variable-level-metadata-schema/schemas/frictionless/csvtemplate/fields.json"
    )
    healjsonschema = requests.get(jsonschema_url).json()
    healcsvtemplate = requests.get(csvschema_url).json()

    healjsonschema_str = pp.pformat(healjsonschema)
    healcsvtemplate_str = pp.pformat(healcsvtemplate)

    py_schema_dir = Path(__file__).parents[1].joinpath("src/healdata_utils/schemas") 
    py_schema_dir.joinpath("__init__.py").write_text("from .jsonschema import healjsonschema\nfrom .frictionless import healcsvschema")
    py_schema_dir.joinpath("jsonschema.py").write_text(f"healjsonschema = {healjsonschema_str}")
    py_schema_dir.joinpath("frictionless.py").write_text(f"healcsvschema = {healcsvtemplate_str}")


copy_schemas()