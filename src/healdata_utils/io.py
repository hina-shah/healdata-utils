""" 
functions to read and write files in a "smart" way
"""
import pyreadstat
import pandas as pd 
from pathlib import Path
# read pyreadstat files

def read_pyreadstat(file_path,**kwargs):
    ''' 
    reads in a "metadata rich file"
    (dta, sav,b7bdat). Note, xport format not supported
    as it doesnt supply value labels.

    '''
    file_path = Path(file_path)
    ext = file_path.suffix 
    if ext=='.sav':
        read = pyreadstat.read_sav
    elif ext=='.sas7bdat':
        read = pyreadstat.read_sas7bdat
    elif ext=='.dta':
        read = pyreadstat.read_dta
    elif ext=='.por':
        read = pyreadstat.read_por

    return read(file_path,**kwargs)



def detect_file_encoding(file_path):
    """ 
    detects file encoding - necessary to correctly
    read in a file

    #TODO: find fxn that detects encoding - chardet?
    #TODO: assert that it is in list of values taken in by 
    #pandas
    """ 
    with open(file_path) as f:
        file_encoding = f.encoding
    
    return file_encoding.lower()



def read_table():
    """ 
    reads in a file with an io function based on 
    extension. Does not do any casting

    #TODO: put this in all tabular inputs (eg csv )
    """ 
    pass 


