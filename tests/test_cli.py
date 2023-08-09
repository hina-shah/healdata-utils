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

