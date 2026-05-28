#set is a collection of unique items
#unorderd ,mutable(edit,add, remove)
#set is {}
#methods
#add, remove(or)discard,pop,clear,union,intersection(commom elements),difference(first set elements only)
#issubset,issuperset
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}
a = {1, 2, 3}
b = {2, 3}
print(a.issuperset(b))  # True
s = {1, 2, 3}
s.discard(5)  # No error
print(s)
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}
s = {1, 2, 3}
s.pop()
print(s)
s = {1, 2, 3}
s.clear()
print(s)  # set()
a = {1, 2}
b = {3, 4}
print(a.union(b))  # {1, 2, 3, 4}
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True


#list compression
#list compresssion means create  python code in short , single line of code
numbers = [1, 2, 3, 4]
squares = []
for i in numbers:
    squares.append(i * i)
print(squares)

numbers = [1, 2, 3, 4]
squares = [i * i for i in numbers]
print(squares)

names = ["ram", "sita", "krishna"]
upper_names = [name.upper() for name in names]
print(upper_names)