my_list = [1, 2, 3]
my_list [0] = "Harsh"
my_list [1] = "Sharma"

for item in my_list:
    print(item)

for element in my_list:
    print(element)


# range() IS also returns the List

for i in range(1, 10):
    print(i)


my_list = [1, 2, 3]

print("my_list", my_list)
print("Element at the index 0-->", my_list[0])
print("Element at the index 1-->", my_list[1])
print("Element at the index 2-->", my_list[2])


# append()--> Append object to the end of the list.
my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

# extend()--> Append a new list
my_list.extend([6, 7, 8, 9, 10])
print(my_list)


# insert()--> Is use for particular position
my_list.insert(10, "Sharma")
print(my_list)

my_list.insert(0, "Harsh")
print(my_list)
print(len(my_list))

my_list[5] = "kush"
print(my_list)

my_list.remove(6)
print(my_list)

print("--")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

print("-----")

my_copy_list.remove(1)
#print(my_list)
print(my_copy_list)
