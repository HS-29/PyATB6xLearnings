squares = [1, 3, 5, 7, 9]
print(squares)
print(squares.pop())
print(squares)

print(squares.pop(2))
print(squares)

squares.clear()
print(squares)

number = [10, 30, 50, 70, 30]
print(number.index(70))

print(number.count(30))


number.sort()
print(number)

number.sort(reverse=True)
print(number)

# reverse()--> Reverse the list in place
number.reverse()
print(number)

print(max(number))
print(min(number))
print(sum(number))



# Slicing
print(number) #[10, 30, 30, 50, 70]
print(number[1:4]) # from index of 1 to 3
print(number[-1]) # Last element
print(number[-2:]) # Lats two element

print("apple" in number)
print(10 in number)
print(20, 70 not in number)


# list creation and comprehension

# range(1, 5)--> List

l = list(range(1, 5))
print(l)