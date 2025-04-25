'''
Prepare a function to sort a given list of name:
-in alphabetical order first letter
-in alphabetical order last letter
- According to the length of the name
'''

def sort_by(names, first_letter=False, last_letter=False, length=False) -> list:
    if first_letter:
        names.sort()
        return names
    if last_letter:
        names.sort(key=lambda name: name[-1])
        return names
    if length:
        names.sort(key=len)
        return names  

class TestSort:
    def test_sort(self):
        #given
        names = ['John', 'Alice', 'Bob', 'Charlie']

        #when
        sorted_names = sort_by(names, first_letter=True)
        #then
        assert sorted_names == ['Alice', 'Bob', 'Charlie', 'John'], f"Expected ['Alice', 'Bob', 'Charlie', 'John'] but got {sorted_names}"
    
    def test_sort_by_last_letter(self):
        #given
        names = ['John', 'Alice', 'Bob', 'Charlie']
        #when
        sorted_names = sort_by(names, last_letter=True)
        #then
        assert sorted_names == ['Bob', 'Alice', 'Charlie', 'John'], f"Expected ['Bob', 'Alice', 'Charlie', 'John'] but got {sorted_names}"

    def test_sort_by_length(self):
        #given
        names = ['John', 'Alice', 'Bob', 'Charlie']
        #when
        sorted_names = sort_by(names, length=True)
        #then
        assert sorted_names == ['Bob', 'John', 'Alice', 'Charlie'], f"Expected ['Bob', 'John', 'Alice', 'Charlie'] but got {sorted_names}"