list1 = ['hallo', 25]
list2 = [1,2,3,4,5,6,7,8,9,10]
list3 = list2[0]
list4 = list2[-3:-1]
list5 = list2[:]
list6 = list4 + list5 # concatenation
print(list6)
list6 += [0,1,2]
print(list6)
list2[9] = 12
list2.append(13) # append takes only 1 argument, more efficient than +
list2[2:5] = [5,7,9]
list2[6:8] = []
len = len(list2) # calculate length
print(len)
list2[:] = [] # clear list

list7 = [1,2,3,4,5]
list8 = [6,7,8,9,10]
list9 = [list7,list8]
print(list9)
print(list9[0])
print(list9[1][3])

# all the methods of list objects:
x = 10
y = [1,2,3]
z = [4,5,6]
y.append(x)
y.extend(z)
y.insert(2,x)   # insert x before given index
y.remove(3)     # remove first matching element
y.pop()         # remove and return last element
y.pop(2)        # remove and return element at given index
z.clear()       # remove all elements from list
y.index(2)      # return index of first matching argument in the list
y.index(2,0,3)  # limit search to subsequence of the list
y.count(3)      # return number of times argument appears in list
y.sort()        # sort list
y.sort(key=None, reverse=False) # sort list in place
y.reverse()     # reverse elements of list in place
y.copy()        # return shallow copy of list
# list usable as a stack with append and pop

from collections import deque   # works faster than pop/insert
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival

# list comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
print (squares)

combinations = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
combinations = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combinations.append((x,y))

vec = [-4,-2,0,2,4]
res = [x*2 for x in vec]
res = [x for x in vec if x >= 0]
res = [abs(x) for x in vec]
freshfruit = [' banana', ' loganberry', 'passion fruit ']
res = [weapon.strip() for weapon in freshfruit]
res = [(x, x**2) for x in range(6)]
vec = [[1,2,3],[4,5,6],[7,8,9]]
res = [num for elem in vec for num in elem]

from math import pi
res = [str(round(pi,n)) for n in range(1,6)]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
transposed = [[row[i] for row in matrix] for i in range(4)]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
list(zip(*matrix))


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]
del a   # delete variable