import pytest
from my_methods import add_it

def test_add_it():
	assert add_it(2, 4) == 6
	assert add_it(-2, 4) == 2