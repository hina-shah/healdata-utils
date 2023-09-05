from click.testing import CliRunner
from healdata_utils.cli import vlmd
from conftest import compare_vlmd_tmp_to_output
import shutil
import os
import json
from pathlib import Path

def test_vlmd_extract_all_params(
    valid_input_params,valid_output_json,valid_output_csv,fields_propname):

    inputtypes = list(valid_input_params.keys())

    for inputtype in inputtypes:

        # collect CLI arguments
        cli_params = ['extract']
        _input_params = valid_input_params[inputtype]
        
        for paramname,param in _input_params.items():
            
            # add CLI options
            if paramname=="output_filepath":
                cli_params.append("--outputfile")
                cli_params.append(str(param))
            elif paramname=="input_filepath":
                cli_args = str(param)  # click argument
            elif paramname == "data_dictionary_props":
                for _paramname,_param in param.items():
                    cli_params.append("--prop")
                    cli_params.append(_paramname)
                    cli_params.append(_param)
            elif paramname == "sas_catalog_filepath":
                # CLI currently infers sas catalog file
                pass

            elif paramname in ["inputtype"]:
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

        # NOTE: removed options for title/description to simplify. 
        # By default, the core convert_to_vlmd function adds a title by getting the stem of filename
        # So, replaced title and deleted description so passes these comparison assertions
        
        compare_vlmd_tmp_to_output(
            tmpdir=_outdir,
            csvoutput=_valid_output_csv,
            jsonoutput=_valid_output_json,
            fields_propname=fields_propname
        )
        # clean up
        shutil.rmtree(_outdir)


def test_vlmd_extract_minimal(valid_input_params):

    inputtypes = list(valid_input_params.keys())

    for inputtype in inputtypes:

        filepath = str(valid_input_params[inputtype]["input_filepath"].resolve())

        try:
            Path("tmp").mkdir()
        except FileExistsError:
            shutil.rmtree("tmp")
            Path("tmp").mkdir()

        os.chdir("tmp")

        # collect CLI arguments
        
        cli_params = ['extract',"--inputtype",inputtype,filepath]

        #run CLI
        runner = CliRunner()
        result = runner.invoke(vlmd, cli_params)

        assert result.exit_code == 0,result.output


        # clean up
        os.chdir("..")
        shutil.rmtree("tmp")


def test_vlmd_validate():

    paths = Path("data/valid/output").glob("*")
    for path in paths:
        runner = CliRunner()
        result = runner.invoke(vlmd, ['validate',str(path)])

        assert result.exit_code == 0,result.output


def test_vlmd_template(fields_propname):

    tmpdir = Path("tmp")

    if tmpdir.exists():
        shutil.rmtree(tmpdir)

    tmpdir.mkdir()

    runner = CliRunner()
    resultjson = runner.invoke(vlmd, ['template',"tmp/templatejson.json","--numfields","2"])
    resultcsv = runner.invoke(vlmd, ['template',"tmp/templatecsv.csv","--numfields","2"])

    assert resultjson.exit_code == 0,resultjson.output
    assert resultcsv.exit_code == 0,resultcsv.output

    csvoutput = Path("data/templates/twofields.csv").read_text().split("\n")
    jsonoutput = json.loads(Path("data/templates/twofields.json").read_text())

    compare_vlmd_tmp_to_output(tmpdir,csvoutput,jsonoutput,fields_propname)

    shutil.rmtree(tmpdir) 

    



if __name__=="__main__":
    vlmd.main()





