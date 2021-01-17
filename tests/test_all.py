import re

def test_steve():
    v1 = 'steve'
    assert re.match('steve', v1, re.I)

def test_nonsteve():
    v1 = 'joe'
    assert not re.match('steve', v1, re.I)
