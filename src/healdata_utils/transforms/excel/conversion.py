from healdata_utils.io import read_excel


def convert_dataexcel():
    
    dfs = read_excel(file_path)
    dfs_concat = pd.concat(dfs.values())
    data_dictionary = data_dictionary_props.copy()
    fields = typesets.infer_frictionless_fields(dfs_concat)
    data_dictionary['data_dictionary'] = fields


    package = convert_templatejson(data_dictionary)
    return package
