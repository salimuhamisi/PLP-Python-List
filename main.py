# create empty list
my_list = []

# append items
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at the second position (index 1)
my_list.insert(1, 15)

#extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

#remove last item
my_list.pop()

#sort list in ascending order
my_list.sort()

#find and print index of 30
indexOf_30 = my_list.index(30)

# Display final list and index
print("Final List:", my_list)
print("Index of 30:", indexOf_30)