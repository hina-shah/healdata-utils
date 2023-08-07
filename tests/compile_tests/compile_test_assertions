from healdata_utils.transforms.readstat.conversion import convert_readstat
from healdata_utils.cli import convert_to_vlmd
import os

# calling this file from /healdata-utils/. recompiles the 
# files test_cli.py and test_conversion.py with new assertion statements

def compile_assertions_test_conversion():
    # use to bulk generate assertions statements for testing
    file_name="tests/test_conversion.py"
    file_path = "tests/data/valid/input/sas-nmhss-2019/data.sas7bdat"
    if os.path.isfile(file_path):
        print('file exists: regex')
    sas7bcat_file_path = "tests/data/valid/input/sas-nmhss-2019/formats.sas7bcat"
    data_dictionaries = convert_readstat(
        file_path=file_path,
        data_dictionary_props={},
        sas7bcat_file_path=sas7bcat_file_path,
    )
    json_template = data_dictionaries["templatejson"]["data_dictionary"]
    csv_template = data_dictionaries["templatecsv"]["data_dictionary"]
    # helper function to bulk generate assertion statements for data structures.
    assertion_statements = ""
    for i, item in enumerate([csv_template, json_template]):
        if i == 0:
            text = "csvtemplate_{}"
            var = "csv_template"
        else:
            text = "jsontemplate_{}"
            var = "json_template"
        for j, component in enumerate(item):
            assertion_statements += (
                "\n\n    " + text.format(str(j)) + "= {}".format(str(component))
            )
            assertion_statements += (
                "\n\n    try:" +\
                "\n        assert {}[{}]".format(var, str(j)) + " == " + text.format(j) +\
                "\n    except AssertionError:" +\
                "\n        _, _, tb = sys.exc_info()" +\
                "\n        tb_info = traceback.extract_tb(tb)" +\
                "\n        filename, line, func, text = tb_info[-1]" +\
                "\n        assertion_messages+='\\nfailure at line: '+ str(line) + ', text: ' + text"
            )
    with open(file_name, "r") as cur_file:
        test_file = cur_file.read()
        cur_file.close()
    lines = test_file.split("\n")

    for i, line in enumerate(lines):
        if line.replace(" ", "") == "###regexflagstart###":
            j = i
        elif line.replace(" ", "") == "###regexflagend###":
            n = i
    for x in range(n - j - 1):
        lines.pop(j + 1)
    new_text = ""
    for i, line in enumerate(lines):
        preamb = "" if i == 0 else "\n"
        if i == j + 1:
            new_text += "\n" + assertion_statements + "\n"
        new_text += preamb + line

    with open(file_name, "w") as cur_file:
        cur_file.write(new_text)
    # os.system('cmd /k " venv\\Scripts\\activate"'.format(__file__))
    # os.system('cmd /c "black {}"'.format(__file__))
    return

def compile_assertions_test_cli():
    file_name="tests/test_cli.py"
    data_dictionary_metadata = {
        "description": (
            "This is a proof of concept to demonstrate"
            " the healdata-utils functionality"
        ),
        "title": "Healdata-utils Demonstration Data Dictionary",
    }
    filepath = "tests/data/valid/input/redcap_dd_export.redcap.csv"
    data_dictionaries = convert_to_vlmd(
        filepath, data_dictionary_props=data_dictionary_metadata
    )
    csvtemplate = data_dictionaries["csvtemplate"]
    jsontemplate = data_dictionaries["jsontemplate"]
    errors = data_dictionaries["errors"]
    # helper function to bulk generate assertion statements for data structures.
    assertion_statements = ""
    for i, item in enumerate([csvtemplate, jsontemplate["data_dictionary"]]):
        if i == 0:
            text = "csvtemplate_{}"
            var = "csvtemplate"
        else:
            text = "data_dictionary_{}"
            var = 'jsontemplate["data_dictionary"]'
        for j, component in enumerate(item):
            assertion_statements += (
                "\n\n    " + text.format(str(j)) + "= {}".format(str(component))
            )
            assertion_statements += (
                "\n\n    try:" +\
                "\n        assert {}[{}]".format(var, str(j)) + " == " + text.format(j) +\
                "\n    except AssertionError:" +\
                "\n        _, _, tb = sys.exc_info()" +\
                "\n        traceback.print_tb(tb) # Fixed format" +\
                "\n        tb_info = traceback.extract_tb(tb)" +\
                "\n        filename, line, func, text = tb_info[-1]" +\
                "\n        assertion_messages+='\\nfailure at line: '+ str(line) + ', text: ' + text"
            )
    with open(file_name, "r") as cur_file:
        test_file = cur_file.read()
        cur_file.close()
    lines = test_file.split("\n")

    for i, line in enumerate(lines):
        if line.replace(" ", "") == "###regexflagstart###":
            j = i
        elif line.replace(" ", "") == "###regexflagend###":
            n = i
    for x in range(n - j - 1):
        lines.pop(j + 1)
    new_text = ""
    for i, line in enumerate(lines):
        preamb = "" if i == 0 else "\n"
        if i == j + 1:
            new_text += "\n" + assertion_statements + "\n"
        new_text += preamb + line

    with open(file_name, "w") as cur_file:
        cur_file.write(new_text)

    return


if __name__ == "__main__":
    compile_assertions_test_conversion()
    compile_assertions_test_cli()
