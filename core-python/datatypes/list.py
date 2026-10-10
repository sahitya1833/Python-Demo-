lst1 = [10,30,50,40,20,60,90,100,20,40,110]
print(lst1)

lst2 = [1,3,2,5,9,8,7,5,4,3,2]
print (lst2)

lst1.append(200)
print("list after append " , lst1)

lst2.append(18)
print("list a fter append", lst2)


print("element occurs",lst1.count(20))
print("element occurs",lst2.count(18))


print("index of the element..", lst1.index(40))

print("index of the element..",lst2.index(18))


lst3= lst1[4:8]
lst4= lst2[2:]

print(lst3)
print(lst4)

merged = lst3 + lst4
print("merged list are..", merged)

del merged

del lst3[2]

print(lst3)

print(len(lst1) ,len(lst2), len(lst3), len(lst4))


lst1.insert(3,550)
print("list after insertin thhe element ", lst1)

lst1.remove(100)
print("lst after remove",lst1 )

#lst2.reverse()
print("list after reserve", lst2)

lst1.sort()
print('list after sorting',lst1)


print(max(lst1))
print(min(lst2))


