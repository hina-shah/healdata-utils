import pprint
import os
from pathlib import Path
import sys
import traceback
from healdata_utils.cli import convert_to_vlmd


# test convert vlmd with redcap csv

def test_convert_to_vlmd_with_redcap_csv_no_output(compile_assertion=False):
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

    assertion_messages=''
    ###regexflagstart###


    csvtemplate_0= {'module': 'demographics', 'name': 'study_id', 'title': 'Study ID', 'description': 'Study ID', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[0] == csvtemplate_0
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_1= {'module': 'demographics', 'name': 'date_enrolled', 'title': 'Date subject signed consent', 'description': 'Demographic Characteristics: Date subject signed consent', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[1] == csvtemplate_1
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_2= {'module': 'demographics', 'name': 'first_name', 'title': 'First Name', 'description': 'Demographic Characteristics: First Name', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[2] == csvtemplate_2
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_3= {'module': 'demographics', 'name': 'last_name', 'title': 'Last Name', 'description': 'Demographic Characteristics: Last Name', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[3] == csvtemplate_3
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_4= {'module': 'demographics', 'name': 'address', 'title': 'Street, City, State, ZIP', 'description': 'Contact Information: Street, City, State, ZIP', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[4] == csvtemplate_4
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_5= {'module': 'demographics', 'name': 'telephone_1', 'title': 'Phone number', 'description': 'Contact Information: Phone number', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[5] == csvtemplate_5
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_6= {'module': 'demographics', 'name': 'telephone_2', 'title': 'Second phone number', 'description': 'Contact Information: Second phone number', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[6] == csvtemplate_6
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_7= {'module': 'demographics', 'name': 'email', 'title': 'E-mail', 'description': 'Contact Information: E-mail', 'type': 'string', 'format': 'email', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[7] == csvtemplate_7
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_8= {'module': 'demographics', 'name': 'sex', 'title': 'Gender', 'description': 'Contact Information: Gender', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Female|1=Male', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[8] == csvtemplate_8
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_9= {'module': 'demographics', 'name': 'given_birth', 'title': 'Has the subject given birth before?', 'description': 'Contact Information: Has the subject given birth before?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[9] == csvtemplate_9
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_10= {'module': 'demographics', 'name': 'num_children', 'title': 'How many times has the subject given birth?', 'description': 'Contact Information: How many times has the subject given birth?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[10] == csvtemplate_10
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_11= {'module': 'demographics', 'name': 'ethnicity', 'title': 'Ethnicity', 'description': 'Contact Information: Ethnicity', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Hispanic or Latino|1=NOT Hispanic or Latino|2=Unknown / Not Reported', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[11] == csvtemplate_11
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_12= {'module': 'demographics', 'name': 'race___0', 'title': 'Race:American Indian/Alaska NativeRace', 'description': 'Contact Information: Race[choice=American Indian/Alaska Native]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[12] == csvtemplate_12
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_13= {'module': 'demographics', 'name': 'race___1', 'title': 'Race:AsianRace', 'description': 'Contact Information: Race[choice=Asian]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[13] == csvtemplate_13
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_14= {'module': 'demographics', 'name': 'race___2', 'title': 'Race:Native Hawaiian or Other Pacific IslanderRace', 'description': 'Contact Information: Race[choice=Native Hawaiian or Other Pacific Islander]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[14] == csvtemplate_14
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_15= {'module': 'demographics', 'name': 'race___3', 'title': 'Race:Black or African AmericanRace', 'description': 'Contact Information: Race[choice=Black or African American]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[15] == csvtemplate_15
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_16= {'module': 'demographics', 'name': 'race___4', 'title': 'Race:WhiteRace', 'description': 'Contact Information: Race[choice=White]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[16] == csvtemplate_16
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_17= {'module': 'demographics', 'name': 'race___5', 'title': 'Race:More Than One RaceRace', 'description': 'Contact Information: Race[choice=More Than One Race]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[17] == csvtemplate_17
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_18= {'module': 'demographics', 'name': 'race___6', 'title': 'Race:Unknown / Not ReportedRace', 'description': 'Contact Information: Race[choice=Unknown / Not Reported]', 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[18] == csvtemplate_18
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_19= {'module': 'demographics', 'name': 'dob', 'title': 'Date of birth', 'description': 'Contact Information: Date of birth', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[19] == csvtemplate_19
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_20= {'module': 'demographics', 'name': 'age', 'title': 'Age (years)', 'description': "Contact Information: Age (years)[calculation: round(datediff([dob],'today','y'),0)]", 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[20] == csvtemplate_20
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_21= {'module': 'demographics', 'name': 'height', 'title': 'Height (cm)', 'description': 'Contact Information: Height (cm)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[21] == csvtemplate_21
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_22= {'module': 'demographics', 'name': 'weight', 'title': 'Weight (kilograms)', 'description': 'Contact Information: Weight (kilograms)', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[22] == csvtemplate_22
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_23= {'module': 'demographics', 'name': 'bmi', 'title': 'BMI', 'description': 'Contact Information: BMI[calculation: round(([weight]*10000)/(([height])^(2)),1)]', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[23] == csvtemplate_23
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_24= {'module': 'demographics', 'name': 'patient_document', 'title': 'Patient document', 'description': 'Contact Information: Patient document', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[24] == csvtemplate_24
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_25= {'module': 'demographics', 'name': 'comorbidities', 'title': 'Any comorbid condition', 'description': 'Contact Information: Any comorbid condition', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[25] == csvtemplate_25
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_26= {'module': 'demographics', 'name': 'diabetes', 'title': 'Patient has a diagnosis of diabetes mellitus?', 'description': 'Contact Information: Patient has a diagnosis of diabetes mellitus?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[26] == csvtemplate_26
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_27= {'module': 'demographics', 'name': 'diabetes_type', 'title': 'Type of Diabetes Mellitus', 'description': 'Contact Information: Type of Diabetes Mellitus', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Type 1 insulin-dependent|1=Type 2 insulin-dependent|2=Type 2 non insulin-dependent', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[27] == csvtemplate_27
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_28= {'module': 'demographics', 'name': 'gym___0', 'title': 'Gym:MondayGym (Weight Training)', 'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Monday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[28] == csvtemplate_28
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_29= {'module': 'demographics', 'name': 'gym___1', 'title': 'Gym:TuesdayGym (Weight Training)', 'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Tuesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[29] == csvtemplate_29
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_30= {'module': 'demographics', 'name': 'gym___2', 'title': 'Gym:WednesdayGym (Weight Training)', 'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Wednesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[30] == csvtemplate_30
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_31= {'module': 'demographics', 'name': 'gym___3', 'title': 'Gym:ThursdayGym (Weight Training)', 'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Thursday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[31] == csvtemplate_31
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_32= {'module': 'demographics', 'name': 'gym___4', 'title': 'Gym:FridayGym (Weight Training)', 'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Friday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[32] == csvtemplate_32
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_33= {'module': 'demographics', 'name': 'aerobics___0', 'title': 'Aerobics:MondayAerobics', 'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Monday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[33] == csvtemplate_33
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_34= {'module': 'demographics', 'name': 'aerobics___1', 'title': 'Aerobics:TuesdayAerobics', 'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Tuesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[34] == csvtemplate_34
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_35= {'module': 'demographics', 'name': 'aerobics___2', 'title': 'Aerobics:WednesdayAerobics', 'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Wednesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[35] == csvtemplate_35
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_36= {'module': 'demographics', 'name': 'aerobics___3', 'title': 'Aerobics:ThursdayAerobics', 'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Thursday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[36] == csvtemplate_36
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_37= {'module': 'demographics', 'name': 'aerobics___4', 'title': 'Aerobics:FridayAerobics', 'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Friday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[37] == csvtemplate_37
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_38= {'module': 'demographics', 'name': 'eat___0', 'title': 'Eat:MondayEat Out (Dinner/Lunch)', 'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Monday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[38] == csvtemplate_38
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_39= {'module': 'demographics', 'name': 'eat___1', 'title': 'Eat:TuesdayEat Out (Dinner/Lunch)', 'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Tuesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[39] == csvtemplate_39
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_40= {'module': 'demographics', 'name': 'eat___2', 'title': 'Eat:WednesdayEat Out (Dinner/Lunch)', 'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Wednesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[40] == csvtemplate_40
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_41= {'module': 'demographics', 'name': 'eat___3', 'title': 'Eat:ThursdayEat Out (Dinner/Lunch)', 'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Thursday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[41] == csvtemplate_41
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_42= {'module': 'demographics', 'name': 'eat___4', 'title': 'Eat:FridayEat Out (Dinner/Lunch)', 'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Friday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[42] == csvtemplate_42
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_43= {'module': 'demographics', 'name': 'drink___0', 'title': 'Drink:MondayDrink (Alcoholic Beverages)', 'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Monday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[43] == csvtemplate_43
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_44= {'module': 'demographics', 'name': 'drink___1', 'title': 'Drink:TuesdayDrink (Alcoholic Beverages)', 'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Tuesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[44] == csvtemplate_44
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_45= {'module': 'demographics', 'name': 'drink___2', 'title': 'Drink:WednesdayDrink (Alcoholic Beverages)', 'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Wednesday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[45] == csvtemplate_45
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_46= {'module': 'demographics', 'name': 'drink___3', 'title': 'Drink:ThursdayDrink (Alcoholic Beverages)', 'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Thursday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[46] == csvtemplate_46
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_47= {'module': 'demographics', 'name': 'drink___4', 'title': 'Drink:FridayDrink (Alcoholic Beverages)', 'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Friday]", 'type': 'boolean', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Unchecked|1=Checked', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[47] == csvtemplate_47
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_48= {'module': 'demographics', 'name': 'dialysis_initiation', 'title': 'Date of first outpatient dialysis treatment', 'description': 'Dialysis Information: Date of first outpatient dialysis treatment', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[48] == csvtemplate_48
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_49= {'module': 'demographics', 'name': 'access_type', 'title': 'Type of vascular access', 'description': 'Dialysis Information: Type of vascular access', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Graft|1=Fistula|2=Catheter with maturing graft|3=Catheter with maturing fistula', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[49] == csvtemplate_49
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_50= {'module': 'demographics', 'name': 'access_location', 'title': 'Location of currently used vascular access', 'description': 'Dialysis Information: Location of currently used vascular access', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Forearm|1=Upper arm|2=Internal jugular vein|3=Subclavian vein|4=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[50] == csvtemplate_50
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_51= {'module': 'demographics', 'name': 'dialysis_unit_name', 'title': 'Name of dialysis unit', 'description': 'Dialysis Information: Name of dialysis unit', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[51] == csvtemplate_51
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_52= {'module': 'demographics', 'name': 'dialysis_unit_phone', 'title': 'Phone number', 'description': 'Dialysis Information: Phone number', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[52] == csvtemplate_52
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_53= {'module': 'demographics', 'name': 'dialysis_schedule_days', 'title': 'Days of the week patient is dialyzed', 'description': 'Dialysis Information: Days of the week patient is dialyzed', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Monday-Wednesday-Friday|1=Tuesday-Thursday-Saturday|2=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[53] == csvtemplate_53
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_54= {'module': 'demographics', 'name': 'dialysis_schedule_time', 'title': 'Shift patient is dialyzed', 'description': 'Dialysis Information: Shift patient is dialyzed', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=First shift|1=Second shift|2=Third shift|3=Fourth shift', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[54] == csvtemplate_54
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_55= {'module': 'demographics', 'name': 'etiology_esrd', 'title': 'Etiology of ESRD', 'description': 'Dialysis Information: Etiology of ESRD', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4|5|6', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Diabetes|1=Hypertension|2=Glomerulonephritis|3=Polycystic Kidney Disease|4=Interstitial Nephritis|5=Hereditary Nephritis|6=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[55] == csvtemplate_55
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_56= {'module': 'demographics', 'name': 'subject_comments', 'title': 'Comments', 'description': 'General Comments: Comments', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[56] == csvtemplate_56
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_57= {'module': 'baseline_data', 'name': 'date_visit_b', 'title': 'Date of baseline visit', 'description': 'Baseline Measurements: Date of baseline visit', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[57] == csvtemplate_57
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_58= {'module': 'baseline_data', 'name': 'date_blood_b', 'title': 'Date blood was drawn', 'description': 'Baseline Measurements: Date blood was drawn', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[58] == csvtemplate_58
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_59= {'module': 'baseline_data', 'name': 'alb_b', 'title': 'Serum Albumin (g/dL)', 'description': 'Baseline Measurements: Serum Albumin (g/dL)', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[59] == csvtemplate_59
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_60= {'module': 'baseline_data', 'name': 'prealb_b', 'title': 'Serum Prealbumin (mg/dL)', 'description': 'Baseline Measurements: Serum Prealbumin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[60] == csvtemplate_60
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_61= {'module': 'baseline_data', 'name': 'creat_b', 'title': 'Creatinine (mg/dL)', 'description': 'Baseline Measurements: Creatinine (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[61] == csvtemplate_61
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_62= {'module': 'baseline_data', 'name': 'npcr_b', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'description': 'Baseline Measurements: Normalized Protein Catabolic Rate (g/kg/d)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[62] == csvtemplate_62
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_63= {'module': 'baseline_data', 'name': 'chol_b', 'title': 'Cholesterol (mg/dL)', 'description': 'Baseline Measurements: Cholesterol (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[63] == csvtemplate_63
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_64= {'module': 'baseline_data', 'name': 'transferrin_b', 'title': 'Transferrin (mg/dL)', 'description': 'Baseline Measurements: Transferrin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[64] == csvtemplate_64
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_65= {'module': 'baseline_data', 'name': 'kt_v_b', 'title': 'Kt/V', 'description': 'Baseline Measurements: Kt/V', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[65] == csvtemplate_65
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_66= {'module': 'baseline_data', 'name': 'drywt_b', 'title': 'Dry weight (kilograms)', 'description': 'Baseline Measurements: Dry weight (kilograms)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[66] == csvtemplate_66
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_67= {'module': 'baseline_data', 'name': 'plasma1_b', 'title': 'Collected Plasma 1?', 'description': 'Baseline Measurements: Collected Plasma 1?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[67] == csvtemplate_67
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_68= {'module': 'baseline_data', 'name': 'plasma2_b', 'title': 'Collected Plasma 2?', 'description': 'Baseline Measurements: Collected Plasma 2?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[68] == csvtemplate_68
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_69= {'module': 'baseline_data', 'name': 'plasma3_b', 'title': 'Collected Plasma 3?', 'description': 'Baseline Measurements: Collected Plasma 3?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[69] == csvtemplate_69
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_70= {'module': 'baseline_data', 'name': 'serum1_b', 'title': 'Collected Serum 1?', 'description': 'Baseline Measurements: Collected Serum 1?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[70] == csvtemplate_70
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_71= {'module': 'baseline_data', 'name': 'serum2_b', 'title': 'Collected Serum 2?', 'description': 'Baseline Measurements: Collected Serum 2?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[71] == csvtemplate_71
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_72= {'module': 'baseline_data', 'name': 'serum3_b', 'title': 'Collected Serum 3?', 'description': 'Baseline Measurements: Collected Serum 3?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[72] == csvtemplate_72
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_73= {'module': 'baseline_data', 'name': 'sga_b', 'title': 'Subject Global Assessment (score = 1-7)', 'description': 'Baseline Measurements: Subject Global Assessment (score = 1-7)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[73] == csvtemplate_73
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_74= {'module': 'baseline_data', 'name': 'date_supplement_dispensed', 'title': 'Date patient begins supplement', 'description': 'Baseline Measurements: Date patient begins supplement', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[74] == csvtemplate_74
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_75= {'module': 'month_1_data', 'name': 'date_visit_1', 'title': 'Date of Month 1 visit', 'description': 'Month 1: Date of Month 1 visit', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[75] == csvtemplate_75
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_76= {'module': 'month_1_data', 'name': 'alb_1', 'title': 'Serum Albumin (g/dL)', 'description': 'Month 1: Serum Albumin (g/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[76] == csvtemplate_76
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_77= {'module': 'month_1_data', 'name': 'prealb_1', 'title': 'Serum Prealbumin (mg/dL)', 'description': 'Month 1: Serum Prealbumin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[77] == csvtemplate_77
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_78= {'module': 'month_1_data', 'name': 'creat_1', 'title': 'Creatinine (mg/dL)', 'description': 'Month 1: Creatinine (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[78] == csvtemplate_78
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_79= {'module': 'month_1_data', 'name': 'npcr_1', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'description': 'Month 1: Normalized Protein Catabolic Rate (g/kg/d)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[79] == csvtemplate_79
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_80= {'module': 'month_1_data', 'name': 'chol_1', 'title': 'Cholesterol (mg/dL)', 'description': 'Month 1: Cholesterol (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[80] == csvtemplate_80
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_81= {'module': 'month_1_data', 'name': 'transferrin_1', 'title': 'Transferrin (mg/dL)', 'description': 'Month 1: Transferrin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[81] == csvtemplate_81
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_82= {'module': 'month_1_data', 'name': 'kt_v_1', 'title': 'Kt/V', 'description': 'Month 1: Kt/V', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[82] == csvtemplate_82
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_83= {'module': 'month_1_data', 'name': 'drywt_1', 'title': 'Dry weight (kilograms)', 'description': 'Month 1: Dry weight (kilograms)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[83] == csvtemplate_83
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_84= {'module': 'month_1_data', 'name': 'no_show_1', 'title': 'Number of treatments missed', 'description': 'Month 1: Number of treatments missed', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[84] == csvtemplate_84
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_85= {'module': 'month_1_data', 'name': 'compliance_1', 'title': 'How compliant was the patient in drinking the supplement?', 'description': 'Month 1: How compliant was the patient in drinking the supplement?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=100 percent|1=99-75 percent|2=74-50 percent|3=49-25 percent|4=0-24 percent', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[85] == csvtemplate_85
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_86= {'module': 'month_1_data', 'name': 'hospit_1', 'title': 'Was patient hospitalized since last visit?', 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[86] == csvtemplate_86
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_87= {'module': 'month_1_data', 'name': 'cause_hosp_1', 'title': 'What was the cause of hospitalization?', 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2|3', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=Vascular access related events|2=CVD events|3=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[87] == csvtemplate_87
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_88= {'module': 'month_1_data', 'name': 'admission_date_1', 'title': 'Date of hospital admission', 'description': 'Hospitalization Data: Date of hospital admission', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[88] == csvtemplate_88
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_89= {'module': 'month_1_data', 'name': 'discharge_date_1', 'title': 'Date of hospital discharge', 'description': 'Hospitalization Data: Date of hospital discharge', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[89] == csvtemplate_89
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_90= {'module': 'month_1_data', 'name': 'discharge_summary_1', 'title': 'Discharge summary in patients binder?', 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[90] == csvtemplate_90
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_91= {'module': 'month_1_data', 'name': 'death_1', 'title': 'Has patient died since last visit?', 'description': 'Mortality Data: Has patient died since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[91] == csvtemplate_91
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_92= {'module': 'month_1_data', 'name': 'date_death_1', 'title': 'Date of death', 'description': 'Mortality Data: Date of death', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[92] == csvtemplate_92
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_93= {'module': 'month_1_data', 'name': 'cause_death_1', 'title': 'What was the cause of death?', 'description': 'Mortality Data: What was the cause of death?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=All-cause|2=Cardiovascular', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[93] == csvtemplate_93
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_94= {'module': 'month_2_data', 'name': 'date_visit_2', 'title': 'Date of Month 2 visit', 'description': 'Month 2: Date of Month 2 visit', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[94] == csvtemplate_94
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_95= {'module': 'month_2_data', 'name': 'alb_2', 'title': 'Serum Albumin (g/dL)', 'description': 'Month 2: Serum Albumin (g/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[95] == csvtemplate_95
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_96= {'module': 'month_2_data', 'name': 'prealb_2', 'title': 'Serum Prealbumin (mg/dL)', 'description': 'Month 2: Serum Prealbumin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[96] == csvtemplate_96
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_97= {'module': 'month_2_data', 'name': 'creat_2', 'title': 'Creatinine (mg/dL)', 'description': 'Month 2: Creatinine (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[97] == csvtemplate_97
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_98= {'module': 'month_2_data', 'name': 'npcr_2', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'description': 'Month 2: Normalized Protein Catabolic Rate (g/kg/d)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[98] == csvtemplate_98
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_99= {'module': 'month_2_data', 'name': 'chol_2', 'title': 'Cholesterol (mg/dL)', 'description': 'Month 2: Cholesterol (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[99] == csvtemplate_99
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_100= {'module': 'month_2_data', 'name': 'transferrin_2', 'title': 'Transferrin (mg/dL)', 'description': 'Month 2: Transferrin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[100] == csvtemplate_100
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_101= {'module': 'month_2_data', 'name': 'kt_v_2', 'title': 'Kt/V', 'description': 'Month 2: Kt/V', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[101] == csvtemplate_101
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_102= {'module': 'month_2_data', 'name': 'drywt_2', 'title': 'Dry weight (kilograms)', 'description': 'Month 2: Dry weight (kilograms)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[102] == csvtemplate_102
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_103= {'module': 'month_2_data', 'name': 'no_show_2', 'title': 'Number of treatments missed', 'description': 'Month 2: Number of treatments missed', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[103] == csvtemplate_103
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_104= {'module': 'month_2_data', 'name': 'compliance_2', 'title': 'How compliant was the patient in drinking the supplement?', 'description': 'Month 2: How compliant was the patient in drinking the supplement?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=100 percent|1=99-75 percent|2=74-50 percent|3=49-25 percent|4=0-24 percent', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[104] == csvtemplate_104
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_105= {'module': 'month_2_data', 'name': 'hospit_2', 'title': 'Was patient hospitalized since last visit?', 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[105] == csvtemplate_105
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_106= {'module': 'month_2_data', 'name': 'cause_hosp_2', 'title': 'What was the cause of hospitalization?', 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2|3', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=Vascular access related events|2=CVD events|3=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[106] == csvtemplate_106
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_107= {'module': 'month_2_data', 'name': 'admission_date_2', 'title': 'Date of hospital admission', 'description': 'Hospitalization Data: Date of hospital admission', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[107] == csvtemplate_107
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_108= {'module': 'month_2_data', 'name': 'discharge_date_2', 'title': 'Date of hospital discharge', 'description': 'Hospitalization Data: Date of hospital discharge', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[108] == csvtemplate_108
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_109= {'module': 'month_2_data', 'name': 'discharge_summary_2', 'title': 'Discharge summary in patients binder?', 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[109] == csvtemplate_109
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_110= {'module': 'month_2_data', 'name': 'death_2', 'title': 'Has patient died since last visit?', 'description': 'Mortality Data: Has patient died since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[110] == csvtemplate_110
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_111= {'module': 'month_2_data', 'name': 'date_death_2', 'title': 'Date of death', 'description': 'Mortality Data: Date of death', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[111] == csvtemplate_111
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_112= {'module': 'month_2_data', 'name': 'cause_death_2', 'title': 'What was the cause of death?', 'description': 'Mortality Data: What was the cause of death?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=All-cause|2=Cardiovascular', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[112] == csvtemplate_112
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_113= {'module': 'month_3_data', 'name': 'date_visit_3', 'title': 'Date of Month 3 visit', 'description': 'Month 3: Date of Month 3 visit', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[113] == csvtemplate_113
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_114= {'module': 'month_3_data', 'name': 'date_blood_3', 'title': 'Date blood was drawn', 'description': 'Month 3: Date blood was drawn', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[114] == csvtemplate_114
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_115= {'module': 'month_3_data', 'name': 'alb_3', 'title': 'Serum Albumin (g/dL)', 'description': 'Month 3: Serum Albumin (g/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[115] == csvtemplate_115
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_116= {'module': 'month_3_data', 'name': 'prealb_3', 'title': 'Serum Prealbumin (mg/dL)', 'description': 'Month 3: Serum Prealbumin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[116] == csvtemplate_116
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_117= {'module': 'month_3_data', 'name': 'creat_3', 'title': 'Creatinine (mg/dL)', 'description': 'Month 3: Creatinine (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[117] == csvtemplate_117
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_118= {'module': 'month_3_data', 'name': 'npcr_3', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'description': 'Month 3: Normalized Protein Catabolic Rate (g/kg/d)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[118] == csvtemplate_118
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_119= {'module': 'month_3_data', 'name': 'chol_3', 'title': 'Cholesterol (mg/dL)', 'description': 'Month 3: Cholesterol (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[119] == csvtemplate_119
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_120= {'module': 'month_3_data', 'name': 'transferrin_3', 'title': 'Transferrin (mg/dL)', 'description': 'Month 3: Transferrin (mg/dL)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[120] == csvtemplate_120
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_121= {'module': 'month_3_data', 'name': 'kt_v_3', 'title': 'Kt/V', 'description': 'Month 3: Kt/V', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[121] == csvtemplate_121
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_122= {'module': 'month_3_data', 'name': 'drywt_3', 'title': 'Dry weight (kilograms)', 'description': 'Month 3: Dry weight (kilograms)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[122] == csvtemplate_122
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_123= {'module': 'month_3_data', 'name': 'plasma1_3', 'title': 'Collected Plasma 1?', 'description': 'Month 3: Collected Plasma 1?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[123] == csvtemplate_123
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_124= {'module': 'month_3_data', 'name': 'plasma2_3', 'title': 'Collected Plasma 2?', 'description': 'Month 3: Collected Plasma 2?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[124] == csvtemplate_124
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_125= {'module': 'month_3_data', 'name': 'plasma3_3', 'title': 'Collected Plasma 3?', 'description': 'Month 3: Collected Plasma 3?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[125] == csvtemplate_125
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_126= {'module': 'month_3_data', 'name': 'serum1_3', 'title': 'Collected Serum 1?', 'description': 'Month 3: Collected Serum 1?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[126] == csvtemplate_126
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_127= {'module': 'month_3_data', 'name': 'serum2_3', 'title': 'Collected Serum 2?', 'description': 'Month 3: Collected Serum 2?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[127] == csvtemplate_127
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_128= {'module': 'month_3_data', 'name': 'serum3_3', 'title': 'Collected Serum 3?', 'description': 'Month 3: Collected Serum 3?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[128] == csvtemplate_128
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_129= {'module': 'month_3_data', 'name': 'sga_3', 'title': 'Subject Global Assessment (score = 1-7)', 'description': 'Month 3: Subject Global Assessment (score = 1-7)', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[129] == csvtemplate_129
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_130= {'module': 'month_3_data', 'name': 'no_show_3', 'title': 'Number of treatments missed', 'description': 'Month 3: Number of treatments missed', 'type': 'number', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[130] == csvtemplate_130
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_131= {'module': 'month_3_data', 'name': 'compliance_3', 'title': 'How compliant was the patient in drinking the supplement?', 'description': 'Month 3: How compliant was the patient in drinking the supplement?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=100 percent|1=99-75 percent|2=74-50 percent|3=49-25 percent|4=0-24 percent', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[131] == csvtemplate_131
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_132= {'module': 'month_3_data', 'name': 'hospit_3', 'title': 'Was patient hospitalized since last visit?', 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[132] == csvtemplate_132
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_133= {'module': 'month_3_data', 'name': 'cause_hosp_3', 'title': 'What was the cause of hospitalization?', 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2|3', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=Vascular access related events|2=CVD events|3=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[133] == csvtemplate_133
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_134= {'module': 'month_3_data', 'name': 'admission_date_3', 'title': 'Date of hospital admission', 'description': 'Hospitalization Data: Date of hospital admission', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[134] == csvtemplate_134
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_135= {'module': 'month_3_data', 'name': 'discharge_date_3', 'title': 'Date of hospital discharge', 'description': 'Hospitalization Data: Date of hospital discharge', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[135] == csvtemplate_135
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_136= {'module': 'month_3_data', 'name': 'discharge_summary_3', 'title': 'Discharge summary in patients binder?', 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[136] == csvtemplate_136
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_137= {'module': 'month_3_data', 'name': 'death_3', 'title': 'Has patient died since last visit?', 'description': 'Mortality Data: Has patient died since last visit?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[137] == csvtemplate_137
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_138= {'module': 'month_3_data', 'name': 'date_death_3', 'title': 'Date of death', 'description': 'Mortality Data: Date of death', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[138] == csvtemplate_138
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_139= {'module': 'month_3_data', 'name': 'cause_death_3', 'title': 'What was the cause of death?', 'description': 'Mortality Data: What was the cause of death?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '1|2', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '1=All-cause|2=Cardiovascular', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[139] == csvtemplate_139
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_140= {'module': 'completion_data', 'name': 'complete_study', 'title': 'Has patient completed study?', 'description': 'Study Completion Information: Has patient completed study?', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=No|1=Yes', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[140] == csvtemplate_140
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_141= {'module': 'completion_data', 'name': 'withdraw_date', 'title': 'Put a date if patient withdrew study', 'description': 'Study Completion Information: Put a date if patient withdrew study', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[141] == csvtemplate_141
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_142= {'module': 'completion_data', 'name': 'withdraw_reason', 'title': 'Reason patient withdrew from study', 'description': 'Study Completion Information: Reason patient withdrew from study', 'type': 'integer', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '0|1|2|3|4', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '0=Non-compliance|1=Did not wish to continue in study|2=Could not tolerate the supplement|3=Hospitalization|4=Other', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[142] == csvtemplate_142
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_143= {'module': 'completion_data', 'name': 'complete_study_date', 'title': 'Date of study completion', 'description': 'Study Completion Information: Date of study completion', 'type': 'date', 'format': 'any', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[143] == csvtemplate_143
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    csvtemplate_144= {'module': 'completion_data', 'name': 'study_comments', 'title': 'Comments', 'description': 'General Comments: Comments', 'type': 'string', 'format': '', 'constraints.maxLength': '', 'constraints.enum': '', 'constraints.pattern': '', 'constraints.maximum': '', 'constraints.minimum': '', 'encodings': '', 'ordered': '', 'missingValues': '', 'trueValues': '', 'falseValues': '', 'repo_link': '', 'standardsMappings.type': '', 'standardsMappings.label': '', 'standardsMappings.url': '', 'standardsMappings.source': '', 'standardsMappings.id': '', 'relatedConcepts.type': '', 'relatedConcepts.label': '', 'relatedConcepts.url': '', 'relatedConcepts.source': '', 'relatedConcepts.id': '', 'univarStats.median': '', 'univarStats.mean': '', 'univarStats.std': '', 'univarStats.min': '', 'univarStats.max': '', 'univarStats.mode': '', 'univarStats.count': '', 'univarStats.twentyFifthPercentile': '', 'univarStats.seventyFifthPercentile': '', 'univarStats.categoricalMarginals.name': '', 'univarStats.categoricalMarginals.count': ''}

    try:
        assert csvtemplate[144] == csvtemplate_144
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_0= {'name': 'study_id', 'type': 'string', 'description': 'Study ID', 'title': 'Study ID', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][0] == data_dictionary_0
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_1= {'name': 'date_enrolled', 'type': 'date', 'format': 'any', 'description': 'Demographic Characteristics: Date subject signed consent', 'title': 'Date subject signed consent', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][1] == data_dictionary_1
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_2= {'name': 'first_name', 'type': 'string', 'description': 'Demographic Characteristics: First Name', 'title': 'First Name', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][2] == data_dictionary_2
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_3= {'name': 'last_name', 'type': 'string', 'description': 'Demographic Characteristics: Last Name', 'title': 'Last Name', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][3] == data_dictionary_3
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_4= {'name': 'address', 'type': 'string', 'description': 'Contact Information: Street, City, State, ZIP', 'title': 'Street, City, State, ZIP', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][4] == data_dictionary_4
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_5= {'name': 'telephone_1', 'type': 'string', 'constraints': {'pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'}, 'description': 'Contact Information: Phone number', 'title': 'Phone number', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][5] == data_dictionary_5
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_6= {'name': 'telephone_2', 'type': 'string', 'constraints': {'pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'}, 'description': 'Contact Information: Second phone number', 'title': 'Second phone number', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][6] == data_dictionary_6
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_7= {'name': 'email', 'type': 'string', 'format': 'email', 'description': 'Contact Information: E-mail', 'title': 'E-mail', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][7] == data_dictionary_7
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_8= {'name': 'sex', 'type': 'integer', 'encodings': {'0': 'Female', '1': 'Male'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Contact Information: Gender', 'title': 'Gender', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][8] == data_dictionary_8
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_9= {'name': 'given_birth', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Contact Information: Has the subject given birth before?', 'title': 'Has the subject given birth before?', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][9] == data_dictionary_9
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_10= {'name': 'num_children', 'type': 'integer', 'description': 'Contact Information: How many times has the subject given birth?', 'title': 'How many times has the subject given birth?', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][10] == data_dictionary_10
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_11= {'name': 'ethnicity', 'type': 'integer', 'encodings': {'0': 'Hispanic or Latino', '1': 'NOT Hispanic or Latino', '2': 'Unknown / Not Reported'}, 'constraints': {'enum': ['0', '1', '2']}, 'description': 'Contact Information: Ethnicity', 'title': 'Ethnicity', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][11] == data_dictionary_11
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_12= {'description': 'Contact Information: Race[choice=American Indian/Alaska Native]', 'title': 'Race:American Indian/Alaska NativeRace', 'name': 'race___0', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][12] == data_dictionary_12
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_13= {'description': 'Contact Information: Race[choice=Asian]', 'title': 'Race:AsianRace', 'name': 'race___1', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][13] == data_dictionary_13
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_14= {'description': 'Contact Information: Race[choice=Native Hawaiian or Other Pacific Islander]', 'title': 'Race:Native Hawaiian or Other Pacific IslanderRace', 'name': 'race___2', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][14] == data_dictionary_14
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_15= {'description': 'Contact Information: Race[choice=Black or African American]', 'title': 'Race:Black or African AmericanRace', 'name': 'race___3', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][15] == data_dictionary_15
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_16= {'description': 'Contact Information: Race[choice=White]', 'title': 'Race:WhiteRace', 'name': 'race___4', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][16] == data_dictionary_16
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_17= {'description': 'Contact Information: Race[choice=More Than One Race]', 'title': 'Race:More Than One RaceRace', 'name': 'race___5', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][17] == data_dictionary_17
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_18= {'description': 'Contact Information: Race[choice=Unknown / Not Reported]', 'title': 'Race:Unknown / Not ReportedRace', 'name': 'race___6', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][18] == data_dictionary_18
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_19= {'name': 'dob', 'type': 'date', 'format': 'any', 'description': 'Contact Information: Date of birth', 'title': 'Date of birth', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][19] == data_dictionary_19
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_20= {'name': 'age', 'description': "Contact Information: Age (years)[calculation: round(datediff([dob],'today','y'),0)]", 'type': 'number', 'title': 'Age (years)', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][20] == data_dictionary_20
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_21= {'name': 'height', 'type': 'number', 'description': 'Contact Information: Height (cm)', 'title': 'Height (cm)', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][21] == data_dictionary_21
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_22= {'name': 'weight', 'type': 'integer', 'description': 'Contact Information: Weight (kilograms)', 'title': 'Weight (kilograms)', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][22] == data_dictionary_22
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_23= {'name': 'bmi', 'description': 'Contact Information: BMI[calculation: round(([weight]*10000)/(([height])^(2)),1)]', 'type': 'number', 'title': 'BMI', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][23] == data_dictionary_23
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_24= {'name': 'patient_document', 'type': 'string', 'description': 'Contact Information: Patient document', 'title': 'Patient document', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][24] == data_dictionary_24
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_25= {'name': 'comorbidities', 'type': 'string', 'description': 'Contact Information: Any comorbid condition', 'title': 'Any comorbid condition', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][25] == data_dictionary_25
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_26= {'name': 'diabetes', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Contact Information: Patient has a diagnosis of diabetes mellitus?', 'title': 'Patient has a diagnosis of diabetes mellitus?', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][26] == data_dictionary_26
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_27= {'name': 'diabetes_type', 'type': 'integer', 'encodings': {'0': 'Type 1 insulin-dependent', '1': 'Type 2 insulin-dependent', '2': 'Type 2 non insulin-dependent'}, 'constraints': {'enum': ['0', '1', '2']}, 'description': 'Contact Information: Type of Diabetes Mellitus', 'title': 'Type of Diabetes Mellitus', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][27] == data_dictionary_27
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_28= {'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Monday]", 'title': 'Gym:MondayGym (Weight Training)', 'name': 'gym___0', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][28] == data_dictionary_28
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_29= {'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Tuesday]", 'title': 'Gym:TuesdayGym (Weight Training)', 'name': 'gym___1', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][29] == data_dictionary_29
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_30= {'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Wednesday]", 'title': 'Gym:WednesdayGym (Weight Training)', 'name': 'gym___2', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][30] == data_dictionary_30
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_31= {'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Thursday]", 'title': 'Gym:ThursdayGym (Weight Training)', 'name': 'gym___3', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][31] == data_dictionary_31
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_32= {'description': "Please provide the patient's weekly schedule for the activities below.: Gym (Weight Training)[choice=Friday]", 'title': 'Gym:FridayGym (Weight Training)', 'name': 'gym___4', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][32] == data_dictionary_32
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_33= {'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Monday]", 'title': 'Aerobics:MondayAerobics', 'name': 'aerobics___0', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][33] == data_dictionary_33
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_34= {'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Tuesday]", 'title': 'Aerobics:TuesdayAerobics', 'name': 'aerobics___1', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][34] == data_dictionary_34
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_35= {'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Wednesday]", 'title': 'Aerobics:WednesdayAerobics', 'name': 'aerobics___2', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][35] == data_dictionary_35
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_36= {'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Thursday]", 'title': 'Aerobics:ThursdayAerobics', 'name': 'aerobics___3', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][36] == data_dictionary_36
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_37= {'description': "Please provide the patient's weekly schedule for the activities below.: Aerobics[choice=Friday]", 'title': 'Aerobics:FridayAerobics', 'name': 'aerobics___4', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][37] == data_dictionary_37
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_38= {'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Monday]", 'title': 'Eat:MondayEat Out (Dinner/Lunch)', 'name': 'eat___0', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][38] == data_dictionary_38
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_39= {'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Tuesday]", 'title': 'Eat:TuesdayEat Out (Dinner/Lunch)', 'name': 'eat___1', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][39] == data_dictionary_39
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_40= {'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Wednesday]", 'title': 'Eat:WednesdayEat Out (Dinner/Lunch)', 'name': 'eat___2', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][40] == data_dictionary_40
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_41= {'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Thursday]", 'title': 'Eat:ThursdayEat Out (Dinner/Lunch)', 'name': 'eat___3', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][41] == data_dictionary_41
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_42= {'description': "Please provide the patient's weekly schedule for the activities below.: Eat Out (Dinner/Lunch)[choice=Friday]", 'title': 'Eat:FridayEat Out (Dinner/Lunch)', 'name': 'eat___4', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][42] == data_dictionary_42
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_43= {'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Monday]", 'title': 'Drink:MondayDrink (Alcoholic Beverages)', 'name': 'drink___0', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][43] == data_dictionary_43
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_44= {'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Tuesday]", 'title': 'Drink:TuesdayDrink (Alcoholic Beverages)', 'name': 'drink___1', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][44] == data_dictionary_44
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_45= {'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Wednesday]", 'title': 'Drink:WednesdayDrink (Alcoholic Beverages)', 'name': 'drink___2', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][45] == data_dictionary_45
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_46= {'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Thursday]", 'title': 'Drink:ThursdayDrink (Alcoholic Beverages)', 'name': 'drink___3', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][46] == data_dictionary_46
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_47= {'description': "Please provide the patient's weekly schedule for the activities below.: Drink (Alcoholic Beverages)[choice=Friday]", 'title': 'Drink:FridayDrink (Alcoholic Beverages)', 'name': 'drink___4', 'type': 'boolean', 'constraints': {'enum': ['0', '1']}, 'encodings': {'0': 'Unchecked', '1': 'Checked'}, 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][47] == data_dictionary_47
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_48= {'name': 'dialysis_initiation', 'type': 'date', 'format': 'any', 'description': 'Dialysis Information: Date of first outpatient dialysis treatment', 'title': 'Date of first outpatient dialysis treatment', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][48] == data_dictionary_48
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_49= {'name': 'access_type', 'type': 'integer', 'encodings': {'0': 'Graft', '1': 'Fistula', '2': 'Catheter with maturing graft', '3': 'Catheter with maturing fistula'}, 'constraints': {'enum': ['0', '1', '2', '3']}, 'description': 'Dialysis Information: Type of vascular access', 'title': 'Type of vascular access', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][49] == data_dictionary_49
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_50= {'name': 'access_location', 'type': 'integer', 'encodings': {'0': 'Forearm', '1': 'Upper arm', '2': 'Internal jugular vein', '3': 'Subclavian vein', '4': 'Other'}, 'constraints': {'enum': ['0', '1', '2', '3', '4']}, 'description': 'Dialysis Information: Location of currently used vascular access', 'title': 'Location of currently used vascular access', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][50] == data_dictionary_50
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_51= {'name': 'dialysis_unit_name', 'type': 'string', 'description': 'Dialysis Information: Name of dialysis unit', 'title': 'Name of dialysis unit', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][51] == data_dictionary_51
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_52= {'name': 'dialysis_unit_phone', 'type': 'string', 'constraints': {'pattern': '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'}, 'description': 'Dialysis Information: Phone number', 'title': 'Phone number', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][52] == data_dictionary_52
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_53= {'name': 'dialysis_schedule_days', 'type': 'integer', 'encodings': {'0': 'Monday-Wednesday-Friday', '1': 'Tuesday-Thursday-Saturday', '2': 'Other'}, 'constraints': {'enum': ['0', '1', '2']}, 'description': 'Dialysis Information: Days of the week patient is dialyzed', 'title': 'Days of the week patient is dialyzed', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][53] == data_dictionary_53
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_54= {'name': 'dialysis_schedule_time', 'type': 'integer', 'encodings': {'0': 'First shift', '1': 'Second shift', '2': 'Third shift', '3': 'Fourth shift'}, 'constraints': {'enum': ['0', '1', '2', '3']}, 'description': 'Dialysis Information: Shift patient is dialyzed', 'title': 'Shift patient is dialyzed', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][54] == data_dictionary_54
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_55= {'name': 'etiology_esrd', 'type': 'integer', 'encodings': {'0': 'Diabetes', '1': 'Hypertension', '2': 'Glomerulonephritis', '3': 'Polycystic Kidney Disease', '4': 'Interstitial Nephritis', '5': 'Hereditary Nephritis', '6': 'Other'}, 'constraints': {'enum': ['0', '1', '2', '3', '4', '5', '6']}, 'description': 'Dialysis Information: Etiology of ESRD', 'title': 'Etiology of ESRD', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][55] == data_dictionary_55
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_56= {'name': 'subject_comments', 'type': 'string', 'description': 'General Comments: Comments', 'title': 'Comments', 'module': 'demographics'}

    try:
        assert jsontemplate["data_dictionary"][56] == data_dictionary_56
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_57= {'name': 'date_visit_b', 'type': 'date', 'format': 'any', 'description': 'Baseline Measurements: Date of baseline visit', 'title': 'Date of baseline visit', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][57] == data_dictionary_57
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_58= {'name': 'date_blood_b', 'type': 'date', 'format': 'any', 'description': 'Baseline Measurements: Date blood was drawn', 'title': 'Date blood was drawn', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][58] == data_dictionary_58
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_59= {'name': 'alb_b', 'type': 'integer', 'description': 'Baseline Measurements: Serum Albumin (g/dL)', 'title': 'Serum Albumin (g/dL)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][59] == data_dictionary_59
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_60= {'name': 'prealb_b', 'type': 'number', 'description': 'Baseline Measurements: Serum Prealbumin (mg/dL)', 'title': 'Serum Prealbumin (mg/dL)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][60] == data_dictionary_60
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_61= {'name': 'creat_b', 'type': 'number', 'description': 'Baseline Measurements: Creatinine (mg/dL)', 'title': 'Creatinine (mg/dL)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][61] == data_dictionary_61
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_62= {'name': 'npcr_b', 'type': 'number', 'description': 'Baseline Measurements: Normalized Protein Catabolic Rate (g/kg/d)', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][62] == data_dictionary_62
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_63= {'name': 'chol_b', 'type': 'number', 'description': 'Baseline Measurements: Cholesterol (mg/dL)', 'title': 'Cholesterol (mg/dL)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][63] == data_dictionary_63
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_64= {'name': 'transferrin_b', 'type': 'number', 'description': 'Baseline Measurements: Transferrin (mg/dL)', 'title': 'Transferrin (mg/dL)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][64] == data_dictionary_64
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_65= {'name': 'kt_v_b', 'type': 'number', 'description': 'Baseline Measurements: Kt/V', 'title': 'Kt/V', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][65] == data_dictionary_65
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_66= {'name': 'drywt_b', 'type': 'number', 'description': 'Baseline Measurements: Dry weight (kilograms)', 'title': 'Dry weight (kilograms)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][66] == data_dictionary_66
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_67= {'name': 'plasma1_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Plasma 1?', 'title': 'Collected Plasma 1?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][67] == data_dictionary_67
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_68= {'name': 'plasma2_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Plasma 2?', 'title': 'Collected Plasma 2?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][68] == data_dictionary_68
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_69= {'name': 'plasma3_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Plasma 3?', 'title': 'Collected Plasma 3?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][69] == data_dictionary_69
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_70= {'name': 'serum1_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Serum 1?', 'title': 'Collected Serum 1?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][70] == data_dictionary_70
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_71= {'name': 'serum2_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Serum 2?', 'title': 'Collected Serum 2?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][71] == data_dictionary_71
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_72= {'name': 'serum3_b', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Baseline Measurements: Collected Serum 3?', 'title': 'Collected Serum 3?', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][72] == data_dictionary_72
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_73= {'name': 'sga_b', 'type': 'number', 'description': 'Baseline Measurements: Subject Global Assessment (score = 1-7)', 'title': 'Subject Global Assessment (score = 1-7)', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][73] == data_dictionary_73
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_74= {'name': 'date_supplement_dispensed', 'type': 'date', 'format': 'any', 'description': 'Baseline Measurements: Date patient begins supplement', 'title': 'Date patient begins supplement', 'module': 'baseline_data'}

    try:
        assert jsontemplate["data_dictionary"][74] == data_dictionary_74
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_75= {'name': 'date_visit_1', 'type': 'date', 'format': 'any', 'description': 'Month 1: Date of Month 1 visit', 'title': 'Date of Month 1 visit', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][75] == data_dictionary_75
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_76= {'name': 'alb_1', 'type': 'number', 'description': 'Month 1: Serum Albumin (g/dL)', 'title': 'Serum Albumin (g/dL)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][76] == data_dictionary_76
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_77= {'name': 'prealb_1', 'type': 'number', 'description': 'Month 1: Serum Prealbumin (mg/dL)', 'title': 'Serum Prealbumin (mg/dL)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][77] == data_dictionary_77
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_78= {'name': 'creat_1', 'type': 'number', 'description': 'Month 1: Creatinine (mg/dL)', 'title': 'Creatinine (mg/dL)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][78] == data_dictionary_78
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_79= {'name': 'npcr_1', 'type': 'number', 'description': 'Month 1: Normalized Protein Catabolic Rate (g/kg/d)', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][79] == data_dictionary_79
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_80= {'name': 'chol_1', 'type': 'number', 'description': 'Month 1: Cholesterol (mg/dL)', 'title': 'Cholesterol (mg/dL)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][80] == data_dictionary_80
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_81= {'name': 'transferrin_1', 'type': 'number', 'description': 'Month 1: Transferrin (mg/dL)', 'title': 'Transferrin (mg/dL)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][81] == data_dictionary_81
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_82= {'name': 'kt_v_1', 'type': 'number', 'description': 'Month 1: Kt/V', 'title': 'Kt/V', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][82] == data_dictionary_82
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_83= {'name': 'drywt_1', 'type': 'number', 'description': 'Month 1: Dry weight (kilograms)', 'title': 'Dry weight (kilograms)', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][83] == data_dictionary_83
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_84= {'name': 'no_show_1', 'type': 'number', 'description': 'Month 1: Number of treatments missed', 'title': 'Number of treatments missed', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][84] == data_dictionary_84
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_85= {'name': 'compliance_1', 'type': 'integer', 'encodings': {'0': '100 percent', '1': '99-75 percent', '2': '74-50 percent', '3': '49-25 percent', '4': '0-24 percent'}, 'constraints': {'enum': ['0', '1', '2', '3', '4']}, 'description': 'Month 1: How compliant was the patient in drinking the supplement?', 'title': 'How compliant was the patient in drinking the supplement?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][85] == data_dictionary_85
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_86= {'name': 'hospit_1', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'title': 'Was patient hospitalized since last visit?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][86] == data_dictionary_86
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_87= {'name': 'cause_hosp_1', 'type': 'integer', 'encodings': {'1': 'Vascular access related events', '2': 'CVD events', '3': 'Other'}, 'constraints': {'enum': ['1', '2', '3']}, 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'title': 'What was the cause of hospitalization?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][87] == data_dictionary_87
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_88= {'name': 'admission_date_1', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital admission', 'title': 'Date of hospital admission', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][88] == data_dictionary_88
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_89= {'name': 'discharge_date_1', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital discharge', 'title': 'Date of hospital discharge', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][89] == data_dictionary_89
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_90= {'name': 'discharge_summary_1', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'title': 'Discharge summary in patients binder?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][90] == data_dictionary_90
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_91= {'name': 'death_1', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Mortality Data: Has patient died since last visit?', 'title': 'Has patient died since last visit?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][91] == data_dictionary_91
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_92= {'name': 'date_death_1', 'type': 'date', 'format': 'any', 'description': 'Mortality Data: Date of death', 'title': 'Date of death', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][92] == data_dictionary_92
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_93= {'name': 'cause_death_1', 'type': 'integer', 'encodings': {'1': 'All-cause', '2': 'Cardiovascular'}, 'constraints': {'enum': ['1', '2']}, 'description': 'Mortality Data: What was the cause of death?', 'title': 'What was the cause of death?', 'module': 'month_1_data'}

    try:
        assert jsontemplate["data_dictionary"][93] == data_dictionary_93
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_94= {'name': 'date_visit_2', 'type': 'date', 'format': 'any', 'description': 'Month 2: Date of Month 2 visit', 'title': 'Date of Month 2 visit', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][94] == data_dictionary_94
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_95= {'name': 'alb_2', 'type': 'number', 'description': 'Month 2: Serum Albumin (g/dL)', 'title': 'Serum Albumin (g/dL)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][95] == data_dictionary_95
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_96= {'name': 'prealb_2', 'type': 'number', 'description': 'Month 2: Serum Prealbumin (mg/dL)', 'title': 'Serum Prealbumin (mg/dL)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][96] == data_dictionary_96
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_97= {'name': 'creat_2', 'type': 'number', 'description': 'Month 2: Creatinine (mg/dL)', 'title': 'Creatinine (mg/dL)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][97] == data_dictionary_97
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_98= {'name': 'npcr_2', 'type': 'number', 'description': 'Month 2: Normalized Protein Catabolic Rate (g/kg/d)', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][98] == data_dictionary_98
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_99= {'name': 'chol_2', 'type': 'number', 'description': 'Month 2: Cholesterol (mg/dL)', 'title': 'Cholesterol (mg/dL)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][99] == data_dictionary_99
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_100= {'name': 'transferrin_2', 'type': 'number', 'description': 'Month 2: Transferrin (mg/dL)', 'title': 'Transferrin (mg/dL)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][100] == data_dictionary_100
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_101= {'name': 'kt_v_2', 'type': 'number', 'description': 'Month 2: Kt/V', 'title': 'Kt/V', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][101] == data_dictionary_101
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_102= {'name': 'drywt_2', 'type': 'number', 'description': 'Month 2: Dry weight (kilograms)', 'title': 'Dry weight (kilograms)', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][102] == data_dictionary_102
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_103= {'name': 'no_show_2', 'type': 'number', 'description': 'Month 2: Number of treatments missed', 'title': 'Number of treatments missed', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][103] == data_dictionary_103
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_104= {'name': 'compliance_2', 'type': 'integer', 'encodings': {'0': '100 percent', '1': '99-75 percent', '2': '74-50 percent', '3': '49-25 percent', '4': '0-24 percent'}, 'constraints': {'enum': ['0', '1', '2', '3', '4']}, 'description': 'Month 2: How compliant was the patient in drinking the supplement?', 'title': 'How compliant was the patient in drinking the supplement?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][104] == data_dictionary_104
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_105= {'name': 'hospit_2', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'title': 'Was patient hospitalized since last visit?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][105] == data_dictionary_105
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_106= {'name': 'cause_hosp_2', 'type': 'integer', 'encodings': {'1': 'Vascular access related events', '2': 'CVD events', '3': 'Other'}, 'constraints': {'enum': ['1', '2', '3']}, 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'title': 'What was the cause of hospitalization?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][106] == data_dictionary_106
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_107= {'name': 'admission_date_2', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital admission', 'title': 'Date of hospital admission', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][107] == data_dictionary_107
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_108= {'name': 'discharge_date_2', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital discharge', 'title': 'Date of hospital discharge', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][108] == data_dictionary_108
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_109= {'name': 'discharge_summary_2', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'title': 'Discharge summary in patients binder?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][109] == data_dictionary_109
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_110= {'name': 'death_2', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Mortality Data: Has patient died since last visit?', 'title': 'Has patient died since last visit?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][110] == data_dictionary_110
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_111= {'name': 'date_death_2', 'type': 'date', 'format': 'any', 'description': 'Mortality Data: Date of death', 'title': 'Date of death', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][111] == data_dictionary_111
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_112= {'name': 'cause_death_2', 'type': 'integer', 'encodings': {'1': 'All-cause', '2': 'Cardiovascular'}, 'constraints': {'enum': ['1', '2']}, 'description': 'Mortality Data: What was the cause of death?', 'title': 'What was the cause of death?', 'module': 'month_2_data'}

    try:
        assert jsontemplate["data_dictionary"][112] == data_dictionary_112
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_113= {'name': 'date_visit_3', 'type': 'date', 'format': 'any', 'description': 'Month 3: Date of Month 3 visit', 'title': 'Date of Month 3 visit', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][113] == data_dictionary_113
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_114= {'name': 'date_blood_3', 'type': 'date', 'format': 'any', 'description': 'Month 3: Date blood was drawn', 'title': 'Date blood was drawn', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][114] == data_dictionary_114
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_115= {'name': 'alb_3', 'type': 'number', 'description': 'Month 3: Serum Albumin (g/dL)', 'title': 'Serum Albumin (g/dL)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][115] == data_dictionary_115
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_116= {'name': 'prealb_3', 'type': 'number', 'description': 'Month 3: Serum Prealbumin (mg/dL)', 'title': 'Serum Prealbumin (mg/dL)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][116] == data_dictionary_116
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_117= {'name': 'creat_3', 'type': 'number', 'description': 'Month 3: Creatinine (mg/dL)', 'title': 'Creatinine (mg/dL)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][117] == data_dictionary_117
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_118= {'name': 'npcr_3', 'type': 'number', 'description': 'Month 3: Normalized Protein Catabolic Rate (g/kg/d)', 'title': 'Normalized Protein Catabolic Rate (g/kg/d)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][118] == data_dictionary_118
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_119= {'name': 'chol_3', 'type': 'number', 'description': 'Month 3: Cholesterol (mg/dL)', 'title': 'Cholesterol (mg/dL)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][119] == data_dictionary_119
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_120= {'name': 'transferrin_3', 'type': 'number', 'description': 'Month 3: Transferrin (mg/dL)', 'title': 'Transferrin (mg/dL)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][120] == data_dictionary_120
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_121= {'name': 'kt_v_3', 'type': 'number', 'description': 'Month 3: Kt/V', 'title': 'Kt/V', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][121] == data_dictionary_121
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_122= {'name': 'drywt_3', 'type': 'number', 'description': 'Month 3: Dry weight (kilograms)', 'title': 'Dry weight (kilograms)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][122] == data_dictionary_122
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_123= {'name': 'plasma1_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Plasma 1?', 'title': 'Collected Plasma 1?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][123] == data_dictionary_123
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_124= {'name': 'plasma2_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Plasma 2?', 'title': 'Collected Plasma 2?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][124] == data_dictionary_124
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_125= {'name': 'plasma3_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Plasma 3?', 'title': 'Collected Plasma 3?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][125] == data_dictionary_125
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_126= {'name': 'serum1_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Serum 1?', 'title': 'Collected Serum 1?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][126] == data_dictionary_126
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_127= {'name': 'serum2_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Serum 2?', 'title': 'Collected Serum 2?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][127] == data_dictionary_127
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_128= {'name': 'serum3_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Month 3: Collected Serum 3?', 'title': 'Collected Serum 3?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][128] == data_dictionary_128
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_129= {'name': 'sga_3', 'type': 'number', 'description': 'Month 3: Subject Global Assessment (score = 1-7)', 'title': 'Subject Global Assessment (score = 1-7)', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][129] == data_dictionary_129
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_130= {'name': 'no_show_3', 'type': 'number', 'description': 'Month 3: Number of treatments missed', 'title': 'Number of treatments missed', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][130] == data_dictionary_130
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_131= {'name': 'compliance_3', 'type': 'integer', 'encodings': {'0': '100 percent', '1': '99-75 percent', '2': '74-50 percent', '3': '49-25 percent', '4': '0-24 percent'}, 'constraints': {'enum': ['0', '1', '2', '3', '4']}, 'description': 'Month 3: How compliant was the patient in drinking the supplement?', 'title': 'How compliant was the patient in drinking the supplement?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][131] == data_dictionary_131
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_132= {'name': 'hospit_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Was patient hospitalized since last visit?', 'title': 'Was patient hospitalized since last visit?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][132] == data_dictionary_132
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_133= {'name': 'cause_hosp_3', 'type': 'integer', 'encodings': {'1': 'Vascular access related events', '2': 'CVD events', '3': 'Other'}, 'constraints': {'enum': ['1', '2', '3']}, 'description': 'Hospitalization Data: What was the cause of hospitalization?', 'title': 'What was the cause of hospitalization?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][133] == data_dictionary_133
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_134= {'name': 'admission_date_3', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital admission', 'title': 'Date of hospital admission', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][134] == data_dictionary_134
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_135= {'name': 'discharge_date_3', 'type': 'date', 'format': 'any', 'description': 'Hospitalization Data: Date of hospital discharge', 'title': 'Date of hospital discharge', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][135] == data_dictionary_135
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_136= {'name': 'discharge_summary_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Hospitalization Data: Discharge summary in patients binder?', 'title': 'Discharge summary in patients binder?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][136] == data_dictionary_136
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_137= {'name': 'death_3', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Mortality Data: Has patient died since last visit?', 'title': 'Has patient died since last visit?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][137] == data_dictionary_137
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_138= {'name': 'date_death_3', 'type': 'date', 'format': 'any', 'description': 'Mortality Data: Date of death', 'title': 'Date of death', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][138] == data_dictionary_138
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_139= {'name': 'cause_death_3', 'type': 'integer', 'encodings': {'1': 'All-cause', '2': 'Cardiovascular'}, 'constraints': {'enum': ['1', '2']}, 'description': 'Mortality Data: What was the cause of death?', 'title': 'What was the cause of death?', 'module': 'month_3_data'}

    try:
        assert jsontemplate["data_dictionary"][139] == data_dictionary_139
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_140= {'name': 'complete_study', 'type': 'integer', 'encodings': {'0': 'No', '1': 'Yes'}, 'constraints': {'enum': ['0', '1']}, 'description': 'Study Completion Information: Has patient completed study?', 'title': 'Has patient completed study?', 'module': 'completion_data'}

    try:
        assert jsontemplate["data_dictionary"][140] == data_dictionary_140
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_141= {'name': 'withdraw_date', 'type': 'date', 'format': 'any', 'description': 'Study Completion Information: Put a date if patient withdrew study', 'title': 'Put a date if patient withdrew study', 'module': 'completion_data'}

    try:
        assert jsontemplate["data_dictionary"][141] == data_dictionary_141
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_142= {'name': 'withdraw_reason', 'type': 'integer', 'encodings': {'0': 'Non-compliance', '1': 'Did not wish to continue in study', '2': 'Could not tolerate the supplement', '3': 'Hospitalization', '4': 'Other'}, 'constraints': {'enum': ['0', '1', '2', '3', '4']}, 'description': 'Study Completion Information: Reason patient withdrew from study', 'title': 'Reason patient withdrew from study', 'module': 'completion_data'}

    try:
        assert jsontemplate["data_dictionary"][142] == data_dictionary_142
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_143= {'name': 'complete_study_date', 'type': 'date', 'format': 'any', 'description': 'Study Completion Information: Date of study completion', 'title': 'Date of study completion', 'module': 'completion_data'}

    try:
        assert jsontemplate["data_dictionary"][143] == data_dictionary_143
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    data_dictionary_144= {'name': 'study_comments', 'type': 'string', 'description': 'General Comments: Comments', 'title': 'Comments', 'module': 'completion_data'}

    try:
        assert jsontemplate["data_dictionary"][144] == data_dictionary_144
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        assertion_messages+='\nfailure at line: '+ str(line) + ', text: ' + text

    ###regexflagend###

    if assertion_messages != '':
        raise Exception(assertion_messages)

    assert jsontemplate["description"] == data_dictionary_metadata["description"]
    assert jsontemplate["title"] == data_dictionary_metadata["title"]

    assert errors["jsontemplate"] == {"valid": True, "errors": []}
    assert errors["csvtemplate"] == {"valid": True, "errors": []}