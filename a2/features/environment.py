import re
import parse
import importlib
import numpy as np
from behave import register_type

@parse.with_pattern(r'\[[\[\]\-\d., ]+\]')
def parse_ndarray(string):
    code = f'ar = np.array({string})'
    d = {'np': np}
    exec(code, d)
    return d['ar']

@parse.with_pattern(r'\[[\d\',\w ]+\]')
def parse_array(string):
    return re.split(r'[,\s\']+', string.strip(r'\'|[|]'))

@parse.with_pattern(r"\{[0-9a-z\',: ]+\}")
def parse_dict(string):
    d = {}
    exec(f'dictionary = {string}', d)
    return d['dictionary']

register_type(NdArray=parse_ndarray)
register_type(Array=parse_array)
register_type(Dict=parse_dict)
