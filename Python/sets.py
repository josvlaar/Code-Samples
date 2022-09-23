basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}   # create set
print(basket)   # unordered, no duplicates
print('orange' in basket)
print('crabgrass' in basket)
empty = set()   # must be set(), not {}, {} is empty dictionary

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both

# set comprehensions:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)