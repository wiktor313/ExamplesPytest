def is_adult(age:int) -> bool:
    return age >= 18
    
def test_is_adult():
    # given
    age = 20
    # when
    result = is_adult(age)
    # then
    assert result, f"Expected True but got {result}"
    assert is_adult(18), "Expected True but got False"

def test_is_not_adult():
    # given
    age = 17
    # when
    result = is_adult(age)
    # then
    assert result == False, f"Expected False but got {result}"