'''
Prepare a test checking if word are palindrome or not.
'''
def is_palindrome(word:str) -> bool:
    return word == word[::-1]

class Test_palindrome:
    def test_is_palindrome(self):
        # given
        word = "racecar"
        # when
        result = is_palindrome(word)
        # then
        assert result, f"Expected True but got {result}"
    def test_is_not_palindrome(self):
        # given
        word = "hello"
        # when
        result = is_palindrome(word)
        # then
        assert result == False, f"Expected False but got {result}"
