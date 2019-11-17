import os
from numpy import array

def dbprint(*args, **kwargs):
    if os.getenv('DEBUG') is None or os.getenv('DEBUG').lower() != 't':
        return
    for _k, _v in kwargs.items():
        try:
            exec(f'{_k} = {repr(_v)}')
        except SyntaxError:
            pass
    for _string in args:
        try:
            print(f"{_string} =", eval(_string))
        except NameError:
            print(f"{_string} = None")
