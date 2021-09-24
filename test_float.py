import pytest

def test_division():
	a = 1
	b = 2
	assert(abs(a / b - 0.5) < 1e10)

@pytest.mark.parametrize("value", [-1e10, -1e-10, 0.0, 1e-10, 1e10])
def test_inf(value):
	a = float("inf")
	assert(a > value)

def test_negative():
	a = "123.4g"
	try:
		value = float(a)
		assert value
	except ValueError:
		pass