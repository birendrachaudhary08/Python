
#Slicing
# can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

a="Python is a popular programming language."


print(a[2:5])
#It means that get the characters from the position 2 to position 5(5 is not included)
print("\n")

#Slicing from start
print(a[:5]) #By leaving out the start index, the range will start at the first character:
print("\n")

print(a[5:]) #Get the characters from position 5, and all the way to the end
print("\n")

#Use negative indexes to start the slice from the end of the string
print(a[-5:-2])