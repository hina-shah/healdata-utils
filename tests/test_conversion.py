from healdata_utils.transforms.readstat.conversion import convert_readstat
import sys
import traceback
import os

def test_convert_readstat_with_sas7bdat():
    # use to bulk generate assertions statements for testing
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

    assertion_messages=''

    ###regexflagstart###


    csvtemplate_0= {'name': 'CASEID', 'type': 'integer'}

    try:
        assert csv_template[0] == csvtemplate_0
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_1= {'name': 'LST', 'type': 'string', 'constraints.enum': 'AK'}

    try:
        assert csv_template[1] == csvtemplate_1
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_2= {'name': 'MHINTAKE', 'type': 'integer', 'constraints.enum': '0|1'}


test_convert_readstat_with_sas7bdat()