import re
import json
import torch
import parse
import importlib
import numpy as np
from pathlib import Path
from behave import register_type

data_path = Path(__file__).parent.joinpath('data')

@parse.with_pattern(r'\[[\[\]\-\d., ]+\]')
def parse_ndarray(string):
    code = f'ar = np.array({string})'
    d = {'np': np}
    exec(code, d)
    return d['ar']

@parse.with_pattern(r'\[[\[\]\(\)\d\',\w ]*\]')
def parse_array(string):
    d = {}
    exec(f'array = {string}', d)
    return d['array']

@parse.with_pattern(r"\{[0-9a-z\',: ]+\}")
def parse_dict(string):
    d = {}
    exec(f'dictionary = {string}', d)
    return d['dictionary']

@parse.with_pattern(r'(True|False)')
def parse_bool(string):
    return string == 'True'

@parse.with_pattern(r'\[[\[\]\(\)\d\',\.\w\- ]*\]')
def parse_tensor(string):
    d = {'torch': torch}
    exec(f'dictionary = torch.tensor({string})', d)
    return d['dictionary']

@parse.with_pattern(r'[a-zA-Z_0-9]+\.json')
def parse_json_file(string):
    with open(data_path.joinpath(string), 'r') as f:
        return json.load(f)

register_type(NdArray=parse_ndarray)
register_type(Array=parse_array)
register_type(Dict=parse_dict)
register_type(Bool=parse_bool)
register_type(Tensor=parse_tensor)
register_type(json_file=parse_json_file)
