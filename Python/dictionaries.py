# keys can be any immutable type, numbers or strings
# tuples can be keys if they contain strings, numbers or other tuples
# keys must be unique within 1 dictionary

dictionary = {} # empty dictionary
dictionary = {'jack': 4098, 'sape': 4139}
dictionary['guido'] = 4127
print(dictionary)
val = dictionary['jack']
print(val)
del dictionary['sape']
dictionary['irv'] = 4127
print(dictionary)   # printed in insertion order
val = list(dictionary)  # keys (not values) added to list in insertion order
print(val)
val = sorted(dictionary)
print(val)
print('guido' in dictionary)
print('jack' not in dictionary)

dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dictionary)

dictionary = {x: x**2 for x in (2,4,6)} # dictionary comprehension
print(dictionary)

dictionary = dict(sape=4139, guido=4127, jack=4098) # keyword arguments
print(dictionary)