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

list10 = [1,2,3]
list10 -= [2]
print(list10)

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
y.index(3)      # return index of first matching argument in the list
y.index(3,0,3)  # limit search to subsequence of the list
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
queue                           # Remaining queue in order of arrival