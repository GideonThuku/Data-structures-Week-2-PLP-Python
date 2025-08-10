# 1. Create an empty list
my_list = []
print("Step 1 - Empty list:", my_list)

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2 - After appending 10, 20, 30, 40:", my_list)

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("Step 3 - After inserting 15 at index 1:", my_list)

# 4. Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("Step 4 - After extending with [50, 60, 70]:", my_list)

# 5. Remove the last element
my_list.pop()
print("Step 5 - After removing the last element:", my_list)

# 6. Sort in ascending order
my_list.sort()
print("Step 6 - After sorting:", my_list)

# 7. Find and print the index of 30
index_30 = my_list.index(30)
print("Step 7 - Index of 30 is:", index_30)

# Final list
print("Final list:", my_list)
