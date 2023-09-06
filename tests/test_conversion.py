import shutil
from pathlib import Path
from healdata_utils.conversion import convert_to_vlmd
import json

from conftest import compare_vlmd_tmp_to_output

def test_convert_to_vlmd_with_registered_formats(
    valid_input_params,valid_output_json,valid_output_csv,fields_propname):
    inputtypes = list(valid_input_params.keys())
    outputdir="tmp"

    for inputtype in inputtypes:
   
        # make an empty temporary output directory
        try:
            Path(outputdir).mkdir()
        except FileExistsError:
            shutil.rmtree(outputdir)
            Path(outputdir).mkdir()

        
        _valid_input_params = valid_input_params[inputtype]
        data_dictionaries = convert_to_vlmd(**_valid_input_params)

        _valid_output_json = valid_output_json[inputtype]
        _valid_output_csv = valid_output_csv[inputtype]

        outdir = _valid_input_params["output_filepath"].parent
        compare_vlmd_tmp_to_output(
            tmpdir=outdir,
            csvoutput=_valid_output_csv,
            jsonoutput=_valid_output_json,
            fields_propname=fields_propname
        )


        # clean up
        shutil.rmtree(outputdir)
