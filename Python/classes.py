def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
MyClass.f
MyClass.i
x = MyClass()
x.f()
xf = x.f
print(xf())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind), print(e.kind)
print(d.name), print(e.name)


class Dog:
    tricks = []     # class variable shared by all instances

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over'), e.add_trick('play dead')
print(d.tricks)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # instance variable for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks), print(e.tricks)


class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)    # with same name, instance variable has precedence over class variable


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:    # f, g and h are valid/usable attributes/functions to instances of C
    f = f1

    def g(self):
        return 'hello world'

    h = g


# how to use self
class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)         # self as a parameter can be omitted
        self.add(x)


# object.__class__ refers to the class/type of an object


class DerivedClassName(BaseClassName):
    pass
class DerivedClassName(modulename.BaseClassName):
    pass
# names are first looked up in derived class, then in base class
# derived classes can override methods from it's base class(es). This also overrides them in/for the (methods in the) base class (who call the overridden method)
# BaseClassName.methodname(self, arguments) calls a method in a base class (this is the way to reach it when it is overridden)

# isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int
# issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int


class DerivedClassName(Base1, Base2, Base3):
    pass
# attributes are first searched for in derivedclass, then in Base1 and it's parents, then Base2 and it's parents and so forth