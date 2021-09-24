import pytest

def test_parity():
	a = 2
	b = 3
	assert(a % 2 != b % 2)

@pytest.mark.parametrize("value", [-200, -2, 0, 2, 200])
def test_zero(value):
	assert(value * 0 == 0)

def test_negative():
	a = "abc"
	try:
		value = int(a)
		assert value
	except ValueError:
		pass