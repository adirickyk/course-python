#cara mengakses list dalam python


list1 = ['fisika', 'matematika', 1990, 1991]
list2 = [1, 2, 3, 4, 5, 6]

print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])


#update value

print("Current Conditions List 1: ", list1)

list1[3] = 9;
print("After update list 1 :", list1)


#delete item on list
print("item yang akan di delete index ke 4 dari list 2", list2)
del list2[4]

#after delete
print("item yang setelah di delete index ke 4 dari list 2", list2)
