
list1=[1, 3, 2, 5, 7, 10, 6]
list1.sort(reverse=True)
list1.reverse()
print(list1)
list1.extend(3)
print(list1)

list1.append(tuple([3, 4, 5]))
print(list1)
print(list1[7])
list1[7]=1
print(list1)

tuple1=(3, 4, 5, [1, 1, 1, 2])
print(tuple1)
tuple1[3][0]=66
print(tuple1[3])
print(tuple1)

list2=['a', 'b', 'A', 'B', '1', '2', '가', '나']
list2.sort()
print(list2)
