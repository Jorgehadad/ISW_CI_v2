'''test.py'''

from app import index

def test_index():
    '''
    This is a docstring
    '''
    assert index()=="<h1>hello continuos world</h1>"
