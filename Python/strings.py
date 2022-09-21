s1 = 'single quotes'
s2 = "double quotes"
e1 = 'doesn\'t'
e2 = "doesn't"
e3 = '"Yes," they said'
e4 = "\"Yes,\" they said"
e5 = '"Isn\'t," they said'
e6 = 'First line.\nSecond line.'
r1 = r'C:\some\name' # called raw string
ml1 = """Newline follows\
Beginning of line
    Indented        With tab
"""
ml2 = """\
Correct way of producing
Multi line string
"""
e7 = 'repeat me 3x' * 3 + 'concatenate me'
e8 = 'automatically' 'concatenated' # used to break up long strings (only works with 2 string literals, not with variables or expressions)
char1 = e3[0] # no character type, character is string of size 1
char2 = e3[1]
char3 = e3[-1] # last character
char4 = e3[-2] # second-last character
s3 = e3[0:2] # characters from position 0 (included) to 2 (excluded)
s4 = e3[:2] # character from the beginning to position 2 (excluded)
s5 = e3[4:] # characters from position 4 (included) to the end
e7 = 'Out of range indexes are ok when slicing, but error when called directly'
s6 = e7[2:100]
# stings are immutable and cannot be assigned to
n1 = len(e3) # get length of string
print(n1)