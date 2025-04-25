'''
Prepare a test for mean function for a list of numbers.
'''

def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def test_mean():
    # given
    numbers = [1, 2, -3, 4, -5]
    # when
    result = mean(numbers)
    # then
    assert result == -0.2, f"Expected -0.2 but got {result}"