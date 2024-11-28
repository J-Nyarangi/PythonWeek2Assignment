# Creating an empty list
my_list = []

# Appending the elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position
my_list.insert(1, 15)

# Extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting the list in ascending order
my_list.sort()

# Finding and printing the index of the value 30
index_30 = my_list.index(30)

# Print the results
print("Final list:", my_list)
print("Index of the value 30:", index_30)
