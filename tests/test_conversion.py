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

    csvtemplate_2= {'name': 'MHINTAKE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[2] == csvtemplate_2
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_3= {'name': 'MHDIAGEVAL', 'type': 'number', 'constraints.enum': '1.0'}

    try:
        assert csv_template[3] == csvtemplate_3
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_4= {'name': 'MHREFERRAL', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[4] == csvtemplate_4
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_5= {'name': 'SMISEDSUD', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[5] == csvtemplate_5
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_6= {'name': 'TREATMT', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[6] == csvtemplate_6
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_7= {'name': 'ADMINSERV', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[7] == csvtemplate_7
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_8= {'name': 'SETTINGIP', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[8] == csvtemplate_8
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_9= {'name': 'SETTINGRC', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[9] == csvtemplate_9
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_10= {'name': 'SETTINGDTPH', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[10] == csvtemplate_10
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_11= {'name': 'SETTINGOP', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[11] == csvtemplate_11
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_12= {'name': 'FACILITYTYPE', 'type': 'integer'}

    try:
        assert csv_template[12] == csvtemplate_12
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_13= {'name': 'FOCUS', 'type': 'number', 'constraints.enum': '1.0|2.0|3.0|4.0|5.0', 'encodings': '1.0=Mental health treatment|2.0=Substance abuse treatment|3.0=Mix of mental health and substance abuse treatment (neither is primary)|4.0=General health care|5.0=Other service focus', 'description': 'Primary treatment focus of facility'}

    try:
        assert csv_template[13] == csvtemplate_13
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_14= {'name': 'OWNERSHP', 'type': 'number', 'constraints.enum': '1.0|2.0|3.0'}

    try:
        assert csv_template[14] == csvtemplate_14
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_15= {'name': 'PUBLICAGENCY', 'type': 'integer'}

    try:
        assert csv_template[15] == csvtemplate_15
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_16= {'name': 'TREATPSYCHOTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0', 'encodings': '0.0=No|1.0=Yes', 'description': 'Facility offers individual psychotherapy'}

    try:
        assert csv_template[16] == csvtemplate_16
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_17= {'name': 'TREATFAMTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[17] == csvtemplate_17
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_18= {'name': 'TREATGRPTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[18] == csvtemplate_18
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_19= {'name': 'TREATCOGTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[19] == csvtemplate_19
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_20= {'name': 'TREATDIALTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[20] == csvtemplate_20
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_21= {'name': 'TREATBEHAVMOD', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[21] == csvtemplate_21
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_22= {'name': 'TREATDUALMHSA', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[22] == csvtemplate_22
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_23= {'name': 'TREATTRAUMATHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0', 'encodings': '0.0=No|1.0=Yes', 'description': 'Facility offers trauma therapy'}

    try:
        assert csv_template[23] == csvtemplate_23
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_24= {'name': 'TREATACTVTYTHRPY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[24] == csvtemplate_24
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_25= {'name': 'TREATELECTRO', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[25] == csvtemplate_25
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_26= {'name': 'TREATTELEMEDINCE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[26] == csvtemplate_26
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_27= {'name': 'TREATPSYCHOMED', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[27] == csvtemplate_27
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_28= {'name': 'TREATOTH', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[28] == csvtemplate_28
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_29= {'name': 'NOTREAT', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[29] == csvtemplate_29
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_30= {'name': 'ASSERTCOMM', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[30] == csvtemplate_30
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_31= {'name': 'MHINTCASEMGMT', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[31] == csvtemplate_31
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_32= {'name': 'MHCASEMGMT', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[32] == csvtemplate_32
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_33= {'name': 'MHCOURTORDERED', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[33] == csvtemplate_33
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_34= {'name': 'MHCHRONIC', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[34] == csvtemplate_34
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_35= {'name': 'ILLNESSMGMT', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[35] == csvtemplate_35
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_36= {'name': 'PRIMARYCARE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[36] == csvtemplate_36
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_37= {'name': 'DIETEXERCOUNSEL', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[37] == csvtemplate_37
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_38= {'name': 'FAMPSYCHED', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[38] == csvtemplate_38
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_39= {'name': 'MHEDUCATION', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[39] == csvtemplate_39
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_40= {'name': 'MHHOUSING', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[40] == csvtemplate_40
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_41= {'name': 'SUPPHOUSING', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[41] == csvtemplate_41
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_42= {'name': 'MHPSYCHREHAB', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[42] == csvtemplate_42
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_43= {'name': 'MHVOCREHAB', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[43] == csvtemplate_43
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_44= {'name': 'SUPPEMPLOY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[44] == csvtemplate_44
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_45= {'name': 'FOSTERCARE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[45] == csvtemplate_45
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_46= {'name': 'MHLEGAL', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[46] == csvtemplate_46
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_47= {'name': 'MHEMGCY', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[47] == csvtemplate_47
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_48= {'name': 'MHSUICIDE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[48] == csvtemplate_48
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_49= {'name': 'MHCONSUMER', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[49] == csvtemplate_49
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_50= {'name': 'MHTOBACCOUSE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[50] == csvtemplate_50
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_51= {'name': 'MHTOBACCOCESS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[51] == csvtemplate_51
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_52= {'name': 'MHNICOTINEREP', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[52] == csvtemplate_52
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_53= {'name': 'SMOKINGCESSATION', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[53] == csvtemplate_53
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_54= {'name': 'MHOTH', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[54] == csvtemplate_54
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_55= {'name': 'MHNOSVCS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[55] == csvtemplate_55
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_56= {'name': 'CHILDAD', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[56] == csvtemplate_56
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_57= {'name': 'ADOLES', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[57] == csvtemplate_57
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_58= {'name': 'YOUNGADULTS', 'type': 'number', 'constraints.enum': '0.0|1.0', 'encodings': '0.0=No|1.0=Yes', 'description': 'Accepts young adults (aged 18-25 years old) for Tx'}

    try:
        assert csv_template[58] == csvtemplate_58
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_59= {'name': 'ADULT', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[59] == csvtemplate_59
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_60= {'name': 'SENIORS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[60] == csvtemplate_60
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_61= {'name': 'SED', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[61] == csvtemplate_61
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_62= {'name': 'TAYOUNGADULTS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[62] == csvtemplate_62
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_63= {'name': 'SPMI', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[63] == csvtemplate_63
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_64= {'name': 'SRVC63', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[64] == csvtemplate_64
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_65= {'name': 'ALZHDEMENTIA', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[65] == csvtemplate_65
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_66= {'name': 'SRVC31', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[66] == csvtemplate_66
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_67= {'name': 'SPECGRPEATING', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[67] == csvtemplate_67
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_68= {'name': 'POSTTRAUM', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[68] == csvtemplate_68
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_69= {'name': 'SRVC116', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[69] == csvtemplate_69
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_70= {'name': 'TRAUMATICBRAIN', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[70] == csvtemplate_70
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_71= {'name': 'SRVC113', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[71] == csvtemplate_71
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_72= {'name': 'SRVC114', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[72] == csvtemplate_72
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_73= {'name': 'SRVC115', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[73] == csvtemplate_73
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_74= {'name': 'SRVC62', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[74] == csvtemplate_74
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_75= {'name': 'SRVC61', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[75] == csvtemplate_75
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_76= {'name': 'SRVC32', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[76] == csvtemplate_76
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_77= {'name': 'SRVC35', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[77] == csvtemplate_77
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_78= {'name': 'NOSPECGRP', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[78] == csvtemplate_78
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_79= {'name': 'CRISISTEAM2', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[79] == csvtemplate_79
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_80= {'name': 'SIGNLANG', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[80] == csvtemplate_80
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_81= {'name': 'LANG', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[81] == csvtemplate_81
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_82= {'name': 'LANGPROV', 'type': 'integer'}

    try:
        assert csv_template[82] == csvtemplate_82
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_83= {'name': 'LANG16', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[83] == csvtemplate_83
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_84= {'name': 'LANG_B', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[84] == csvtemplate_84
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_85= {'name': 'LANG1', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[85] == csvtemplate_85
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_86= {'name': 'LANG2', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[86] == csvtemplate_86
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_87= {'name': 'LANG3', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[87] == csvtemplate_87
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_88= {'name': 'LANG21', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[88] == csvtemplate_88
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_89= {'name': 'LANG4', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[89] == csvtemplate_89
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_90= {'name': 'LANG5', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[90] == csvtemplate_90
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_91= {'name': 'LANG6', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[91] == csvtemplate_91
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_92= {'name': 'LANG7', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[92] == csvtemplate_92
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_93= {'name': 'LANG8', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[93] == csvtemplate_93
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_94= {'name': 'LANG24', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[94] == csvtemplate_94
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_95= {'name': 'LANG9', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[95] == csvtemplate_95
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_96= {'name': 'LANG10', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[96] == csvtemplate_96
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_97= {'name': 'LANG22', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[97] == csvtemplate_97
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_98= {'name': 'LANG25', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[98] == csvtemplate_98
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_99= {'name': 'LANG26', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[99] == csvtemplate_99
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_100= {'name': 'LANG11', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[100] == csvtemplate_100
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_101= {'name': 'LANG19', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[101] == csvtemplate_101
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_102= {'name': 'LANG23', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[102] == csvtemplate_102
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_103= {'name': 'LANG12', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[103] == csvtemplate_103
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_104= {'name': 'LANG13', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[104] == csvtemplate_104
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_105= {'name': 'LANG14', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[105] == csvtemplate_105
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_106= {'name': 'LANG15', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[106] == csvtemplate_106
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_107= {'name': 'LANG20', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[107] == csvtemplate_107
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_108= {'name': 'LANG17', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[108] == csvtemplate_108
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_109= {'name': 'LANG18', 'type': 'number', 'constraints.enum': '-2.0|0.0'}

    try:
        assert csv_template[109] == csvtemplate_109
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_110= {'name': 'SMOKINGPOLICY', 'type': 'number', 'constraints.enum': '1.0|2.0'}

    try:
        assert csv_template[110] == csvtemplate_110
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_111= {'name': 'FEESCALE', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[111] == csvtemplate_111
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_112= {'name': 'PAYASST', 'type': 'number', 'constraints.enum': '-2.0|0.0|1.0'}

    try:
        assert csv_template[112] == csvtemplate_112
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_113= {'name': 'REVCHK1', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[113] == csvtemplate_113
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_114= {'name': 'REVCHK2', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[114] == csvtemplate_114
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_115= {'name': 'REVCHK8', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[115] == csvtemplate_115
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_116= {'name': 'REVCHK5', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[116] == csvtemplate_116
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_117= {'name': 'REVCHK10', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[117] == csvtemplate_117
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_118= {'name': 'FUNDSMHA', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[118] == csvtemplate_118
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_119= {'name': 'FUNDSTATEWELFARE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[119] == csvtemplate_119
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_120= {'name': 'FUNDSTATEJUV', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[120] == csvtemplate_120
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_121= {'name': 'FUNDSTATEEDUC', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[121] == csvtemplate_121
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_122= {'name': 'FUNDOTHSTATE', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[122] == csvtemplate_122
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_123= {'name': 'FUNDLOCALGOV', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[123] == csvtemplate_123
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_124= {'name': 'FUNDCSBG', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[124] == csvtemplate_124
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_125= {'name': 'FUNDCMHG', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[125] == csvtemplate_125
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_126= {'name': 'REVCHK15', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[126] == csvtemplate_126
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_127= {'name': 'FUNDVA', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[127] == csvtemplate_127
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_128= {'name': 'REVCHK17', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[128] == csvtemplate_128
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_129= {'name': 'REVCHK2A', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[129] == csvtemplate_129
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_130= {'name': 'LICENMH', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[130] == csvtemplate_130
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_131= {'name': 'LICENSED', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[131] == csvtemplate_131
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_132= {'name': 'LICENPH', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[132] == csvtemplate_132
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_133= {'name': 'LICENSEDFCS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[133] == csvtemplate_133
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_134= {'name': 'LICENHOS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[134] == csvtemplate_134
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_135= {'name': 'JCAHO', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[135] == csvtemplate_135
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_136= {'name': 'CARF', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[136] == csvtemplate_136
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_137= {'name': 'COA', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[137] == csvtemplate_137
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_138= {'name': 'CMS', 'type': 'number', 'constraints.enum': '0.0|1.0'}

    try:
        assert csv_template[138] == csvtemplate_138
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_139= {'name': 'OTHSTATE', 'type': 'number', 'constraints.enum': '0.0'}

    try:
        assert csv_template[139] == csvtemplate_139
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_0= {'name': 'CASEID', 'type': 'integer'}

    try:
        assert json_template[0] == jsontemplate_0
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_1= {'name': 'LST', 'type': 'string', 'constraints': {'enum': ['AK']}}

    try:
        assert json_template[1] == jsontemplate_1
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_2= {'name': 'MHINTAKE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[2] == jsontemplate_2
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_3= {'name': 'MHDIAGEVAL', 'type': 'number', 'constraints': {'enum': [1.0]}}

    try:
        assert json_template[3] == jsontemplate_3
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_4= {'name': 'MHREFERRAL', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[4] == jsontemplate_4
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_5= {'name': 'SMISEDSUD', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[5] == jsontemplate_5
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_6= {'name': 'TREATMT', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[6] == jsontemplate_6
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_7= {'name': 'ADMINSERV', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[7] == jsontemplate_7
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_8= {'name': 'SETTINGIP', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[8] == jsontemplate_8
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_9= {'name': 'SETTINGRC', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[9] == jsontemplate_9
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_10= {'name': 'SETTINGDTPH', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[10] == jsontemplate_10
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_11= {'name': 'SETTINGOP', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[11] == jsontemplate_11
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_12= {'name': 'FACILITYTYPE', 'type': 'integer'}

    try:
        assert json_template[12] == jsontemplate_12
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_13= {'name': 'FOCUS', 'type': 'number', 'constraints': {'enum': ['1.0', '2.0', '3.0', '4.0', '5.0']}, 'encodings': {1.0: 'Mental health treatment', 2.0: 'Substance abuse treatment', 3.0: 'Mix of mental health and substance abuse treatment (neither is primary)', 4.0: 'General health care', 5.0: 'Other service focus'}, 'description': 'Primary treatment focus of facility'}

    try:
        assert json_template[13] == jsontemplate_13
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_14= {'name': 'OWNERSHP', 'type': 'number', 'constraints': {'enum': [1.0, 2.0, 3.0]}}

    try:
        assert json_template[14] == jsontemplate_14
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_15= {'name': 'PUBLICAGENCY', 'type': 'integer'}

    try:
        assert json_template[15] == jsontemplate_15
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_16= {'name': 'TREATPSYCHOTHRPY', 'type': 'number', 'constraints': {'enum': ['0.0', '1.0']}, 'encodings': {0.0: 'No', 1.0: 'Yes'}, 'description': 'Facility offers individual psychotherapy'}

    try:
        assert json_template[16] == jsontemplate_16
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_17= {'name': 'TREATFAMTHRPY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[17] == jsontemplate_17
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_18= {'name': 'TREATGRPTHRPY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[18] == jsontemplate_18
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_19= {'name': 'TREATCOGTHRPY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[19] == jsontemplate_19
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_20= {'name': 'TREATDIALTHRPY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[20] == jsontemplate_20
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_21= {'name': 'TREATBEHAVMOD', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[21] == jsontemplate_21
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_22= {'name': 'TREATDUALMHSA', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[22] == jsontemplate_22
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_23= {'name': 'TREATTRAUMATHRPY', 'type': 'number', 'constraints': {'enum': ['0.0', '1.0']}, 'encodings': {0.0: 'No', 1.0: 'Yes'}, 'description': 'Facility offers trauma therapy'}

    try:
        assert json_template[23] == jsontemplate_23
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_24= {'name': 'TREATACTVTYTHRPY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[24] == jsontemplate_24
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_25= {'name': 'TREATELECTRO', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[25] == jsontemplate_25
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_26= {'name': 'TREATTELEMEDINCE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[26] == jsontemplate_26
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_27= {'name': 'TREATPSYCHOMED', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[27] == jsontemplate_27
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_28= {'name': 'TREATOTH', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[28] == jsontemplate_28
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_29= {'name': 'NOTREAT', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[29] == jsontemplate_29
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_30= {'name': 'ASSERTCOMM', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[30] == jsontemplate_30
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_31= {'name': 'MHINTCASEMGMT', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[31] == jsontemplate_31
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_32= {'name': 'MHCASEMGMT', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[32] == jsontemplate_32
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_33= {'name': 'MHCOURTORDERED', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[33] == jsontemplate_33
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_34= {'name': 'MHCHRONIC', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[34] == jsontemplate_34
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_35= {'name': 'ILLNESSMGMT', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[35] == jsontemplate_35
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_36= {'name': 'PRIMARYCARE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[36] == jsontemplate_36
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_37= {'name': 'DIETEXERCOUNSEL', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[37] == jsontemplate_37
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_38= {'name': 'FAMPSYCHED', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[38] == jsontemplate_38
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_39= {'name': 'MHEDUCATION', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[39] == jsontemplate_39
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_40= {'name': 'MHHOUSING', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[40] == jsontemplate_40
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_41= {'name': 'SUPPHOUSING', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[41] == jsontemplate_41
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_42= {'name': 'MHPSYCHREHAB', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[42] == jsontemplate_42
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_43= {'name': 'MHVOCREHAB', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[43] == jsontemplate_43
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_44= {'name': 'SUPPEMPLOY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[44] == jsontemplate_44
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_45= {'name': 'FOSTERCARE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[45] == jsontemplate_45
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_46= {'name': 'MHLEGAL', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[46] == jsontemplate_46
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_47= {'name': 'MHEMGCY', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[47] == jsontemplate_47
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_48= {'name': 'MHSUICIDE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[48] == jsontemplate_48
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_49= {'name': 'MHCONSUMER', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[49] == jsontemplate_49
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_50= {'name': 'MHTOBACCOUSE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[50] == jsontemplate_50
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_51= {'name': 'MHTOBACCOCESS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[51] == jsontemplate_51
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_52= {'name': 'MHNICOTINEREP', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[52] == jsontemplate_52
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_53= {'name': 'SMOKINGCESSATION', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[53] == jsontemplate_53
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_54= {'name': 'MHOTH', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[54] == jsontemplate_54
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_55= {'name': 'MHNOSVCS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[55] == jsontemplate_55
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_56= {'name': 'CHILDAD', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[56] == jsontemplate_56
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_57= {'name': 'ADOLES', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[57] == jsontemplate_57
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_58= {'name': 'YOUNGADULTS', 'type': 'number', 'constraints': {'enum': ['0.0', '1.0']}, 'encodings': {0.0: 'No', 1.0: 'Yes'}, 'description': 'Accepts young adults (aged 18-25 years old) for Tx'}

    try:
        assert json_template[58] == jsontemplate_58
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_59= {'name': 'ADULT', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[59] == jsontemplate_59
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_60= {'name': 'SENIORS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[60] == jsontemplate_60
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_61= {'name': 'SED', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[61] == jsontemplate_61
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_62= {'name': 'TAYOUNGADULTS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[62] == jsontemplate_62
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_63= {'name': 'SPMI', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[63] == jsontemplate_63
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_64= {'name': 'SRVC63', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[64] == jsontemplate_64
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_65= {'name': 'ALZHDEMENTIA', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[65] == jsontemplate_65
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_66= {'name': 'SRVC31', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[66] == jsontemplate_66
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_67= {'name': 'SPECGRPEATING', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[67] == jsontemplate_67
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_68= {'name': 'POSTTRAUM', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[68] == jsontemplate_68
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_69= {'name': 'SRVC116', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[69] == jsontemplate_69
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_70= {'name': 'TRAUMATICBRAIN', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[70] == jsontemplate_70
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_71= {'name': 'SRVC113', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[71] == jsontemplate_71
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_72= {'name': 'SRVC114', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[72] == jsontemplate_72
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_73= {'name': 'SRVC115', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[73] == jsontemplate_73
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_74= {'name': 'SRVC62', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[74] == jsontemplate_74
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_75= {'name': 'SRVC61', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[75] == jsontemplate_75
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_76= {'name': 'SRVC32', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[76] == jsontemplate_76
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_77= {'name': 'SRVC35', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[77] == jsontemplate_77
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_78= {'name': 'NOSPECGRP', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[78] == jsontemplate_78
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_79= {'name': 'CRISISTEAM2', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[79] == jsontemplate_79
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_80= {'name': 'SIGNLANG', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[80] == jsontemplate_80
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_81= {'name': 'LANG', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[81] == jsontemplate_81
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_82= {'name': 'LANGPROV', 'type': 'integer'}

    try:
        assert json_template[82] == jsontemplate_82
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_83= {'name': 'LANG16', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[83] == jsontemplate_83
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_84= {'name': 'LANG_B', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[84] == jsontemplate_84
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_85= {'name': 'LANG1', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[85] == jsontemplate_85
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_86= {'name': 'LANG2', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[86] == jsontemplate_86
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_87= {'name': 'LANG3', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[87] == jsontemplate_87
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_88= {'name': 'LANG21', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[88] == jsontemplate_88
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_89= {'name': 'LANG4', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[89] == jsontemplate_89
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_90= {'name': 'LANG5', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[90] == jsontemplate_90
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_91= {'name': 'LANG6', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[91] == jsontemplate_91
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_92= {'name': 'LANG7', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[92] == jsontemplate_92
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_93= {'name': 'LANG8', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[93] == jsontemplate_93
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_94= {'name': 'LANG24', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[94] == jsontemplate_94
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_95= {'name': 'LANG9', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[95] == jsontemplate_95
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_96= {'name': 'LANG10', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[96] == jsontemplate_96
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_97= {'name': 'LANG22', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[97] == jsontemplate_97
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_98= {'name': 'LANG25', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[98] == jsontemplate_98
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_99= {'name': 'LANG26', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[99] == jsontemplate_99
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_100= {'name': 'LANG11', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[100] == jsontemplate_100
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_101= {'name': 'LANG19', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[101] == jsontemplate_101
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_102= {'name': 'LANG23', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[102] == jsontemplate_102
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_103= {'name': 'LANG12', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[103] == jsontemplate_103
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_104= {'name': 'LANG13', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[104] == jsontemplate_104
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_105= {'name': 'LANG14', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[105] == jsontemplate_105
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_106= {'name': 'LANG15', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[106] == jsontemplate_106
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_107= {'name': 'LANG20', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[107] == jsontemplate_107
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_108= {'name': 'LANG17', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[108] == jsontemplate_108
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_109= {'name': 'LANG18', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0]}}

    try:
        assert json_template[109] == jsontemplate_109
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_110= {'name': 'SMOKINGPOLICY', 'type': 'number', 'constraints': {'enum': [1.0, 2.0]}}

    try:
        assert json_template[110] == jsontemplate_110
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_111= {'name': 'FEESCALE', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[111] == jsontemplate_111
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_112= {'name': 'PAYASST', 'type': 'number', 'constraints': {'enum': [-2.0, 0.0, 1.0]}}

    try:
        assert json_template[112] == jsontemplate_112
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_113= {'name': 'REVCHK1', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[113] == jsontemplate_113
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_114= {'name': 'REVCHK2', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[114] == jsontemplate_114
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_115= {'name': 'REVCHK8', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[115] == jsontemplate_115
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_116= {'name': 'REVCHK5', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[116] == jsontemplate_116
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_117= {'name': 'REVCHK10', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[117] == jsontemplate_117
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_118= {'name': 'FUNDSMHA', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[118] == jsontemplate_118
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_119= {'name': 'FUNDSTATEWELFARE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[119] == jsontemplate_119
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_120= {'name': 'FUNDSTATEJUV', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[120] == jsontemplate_120
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_121= {'name': 'FUNDSTATEEDUC', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[121] == jsontemplate_121
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_122= {'name': 'FUNDOTHSTATE', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[122] == jsontemplate_122
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_123= {'name': 'FUNDLOCALGOV', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[123] == jsontemplate_123
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_124= {'name': 'FUNDCSBG', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[124] == jsontemplate_124
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_125= {'name': 'FUNDCMHG', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[125] == jsontemplate_125
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_126= {'name': 'REVCHK15', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[126] == jsontemplate_126
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_127= {'name': 'FUNDVA', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[127] == jsontemplate_127
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_128= {'name': 'REVCHK17', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[128] == jsontemplate_128
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_129= {'name': 'REVCHK2A', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[129] == jsontemplate_129
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_130= {'name': 'LICENMH', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[130] == jsontemplate_130
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_131= {'name': 'LICENSED', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[131] == jsontemplate_131
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_132= {'name': 'LICENPH', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[132] == jsontemplate_132
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_133= {'name': 'LICENSEDFCS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[133] == jsontemplate_133
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_134= {'name': 'LICENHOS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[134] == jsontemplate_134
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_135= {'name': 'JCAHO', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[135] == jsontemplate_135
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_136= {'name': 'CARF', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[136] == jsontemplate_136
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_137= {'name': 'COA', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[137] == jsontemplate_137
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_138= {'name': 'CMS', 'type': 'number', 'constraints': {'enum': [0.0, 1.0]}}

    try:
        assert json_template[138] == jsontemplate_138
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    jsontemplate_139= {'name': 'OTHSTATE', 'type': 'number', 'constraints': {'enum': [0.0]}}

    try:
        assert json_template[139] == jsontemplate_139
    except AssertionError:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    ###regexflagend###

    if assertion_messages != '':
        raise Exception(assertion_messages)