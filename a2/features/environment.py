import numpy as np
import parse
from behave import register_type

@parse.with_pattern(r'\[[\[\]\-\d., ]+\]')
def parse_ndarray(string):
    code = f'ar = np.array({string})'
    d = {'np': np}
    exec(code, d)
    return d['ar']

register_type(NdArray=parse_ndarray)
