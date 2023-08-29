from click.testing import CliRunner
from healdata_utils.cli import vlmd
from conftest import compare_vlmd_tmp_to_output
import shutil
from pathlib import Path

def test_vlmd_extract(
    valid_input_params,valid_output_json,valid_output_csv,fields_propname):

    inputtypes = list(valid_input_params.keys())

    for inputtype in inputtypes:

        # collect CLI arguments
        cli_params = ['extract']
        _input_params = valid_input_params[inputtype]
        
        for paramname,param in _input_params.items():
            
            # add CLI options
            if paramname=="output_filepath":
                cli_params.append("--outfile")
                cli_params.append(str(param))
            elif paramname=="input_filepath":
                cli_args = str(param)  # click argument
            elif paramname == "data_dictionary_props":
                for _paramname,_param in param.items():
                    cli_params.append(f"--{_paramname.replace('_','-')}")
                    cli_params.append(str(_param))
            elif paramname == "sas_catalog_filepath":
                # CLI currently infers sas catalog file
                pass
            else:
                cli_params.append(f"--{paramname.replace('_','-')}")
                cli_params.append(str(param))

        # make an empty temporary output directory
        _outdir = _input_params["output_filepath"].parent
        try:
            Path(_outdir).mkdir()
        except FileExistsError:
            shutil.rmtree(_outdir)
            Path(_outdir).mkdir()

        # add click arguments at end
        cli_params.append(cli_args)

        #run CLI
        runner = CliRunner()
        result = runner.invoke(vlmd, cli_params)

        assert result.exit_code == 0

        # test CLI output to existing output
        _valid_output_json = valid_output_json[inputtype]
        _valid_output_csv = valid_output_csv[inputtype]

        compare_vlmd_tmp_to_output(
            tmpdir=_outdir,
            csvoutput=_valid_output_csv,
            jsonoutput=_valid_output_json,
            fields_propname=fields_propname
        )
        # clean up
        shutil.rmtree(_outdir)


def test_vlmd_validate():

    args = ["validate"]


    runner = CliRunner()
    result = runner.invoke(vlmd, ['validate', ''])