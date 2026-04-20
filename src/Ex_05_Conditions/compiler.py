#apple

#using
#slicing
#method
word = "Apple"
reversed_word = word[::-1]
print(reversed_word)

word = input("enter a word")
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")