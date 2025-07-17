#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
a=[1,2,3,4,5,6,7,5,8,9,0]
b=[11,223,435,647,859,0,6,7,5,8,9,0]
#print(a)
#print(type(a))
#print(dir(a))


#Append object to the end of the list
#print(help(a.append))
#a.append(999)
#print(a)
#print(help(a))

#Remove all items from list.
#a.clear(2)
#print(a)

#b=a.copy()
#print(b)

#Return number of occurrences of value.
#a.count(5)
#print(a.count(5))

#Extend list by appending elements from the iterable.
#a.extend(b)
#print(a)


#print(a.index(0))

#a.insert(2,909090)
#print(a)

#a.pop()
#print(a.pop())
#print(a)


#a.remove(5)
#print(a)

a.sort(reverse=True)
print(a)


#a.reverse()