t = 12345, 54321, 'hello!'  # parentheses optional on input, called tuple packing
t[0]
u = t, (1, 2, 3, 4, 5)
v = ([1, 2, 3], [3, 2, 1])  # tuples are immutable but they can contain mutable objects
print(u)

empty = ()
singleton = 'hello',    # <-- note trailing comma: ('hello') doesn't work
len(empty)
len(singleton)
print(singleton)

x, y, z = t # called sequence unpacking (t must contain 3 values)