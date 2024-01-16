from mapper import Layouts
import pytest


@pytest.fixture
def q2c():
    return Layouts.Q2C

@pytest.fixture
def c2d():
    return Layouts.C2D

@pytest.fixture
def q2d():
    return Layouts.Q2D

def test_no_symbols(q2c, c2d, q2d):
    assert '[' not in q2c
    assert '[' not in c2d
    assert '[' not in q2d

def test_qwerty2colemak(q2c):
    assert q2c['a'] == 'a'
    assert q2c['r'] == 'p'
    assert q2c['j'] == 'n'

def test_colemak2dvorak(c2d):
    assert c2d['l'] == 'g'
    assert c2d['n'] == 'h'
    assert c2d['t'] == 'u'

def test_qwerty2dvorak(q2d):
    assert q2d['f'] == 'u'
    assert q2d['j'] == 'h'
    assert q2d['b'] == 'x'
