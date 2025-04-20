
#Basics String operation 
# 
# String is a collection of alphabets, words or other characters
#Strings in python are surrounded by either single quotation marks, or double quotation marks.


greeting ="Hello"
name="Friends"

welocme_message = greeting + ","+name+"!"
print(welocme_message)

repeat_word= "Python\n" *3
print(repeat_word)

a = """Python string is on going to your learning"""
print(a)

#String as Array
print(a[3])

#loop for string 
for x in a:
    print(x)

#checking string
print("going" in a)

#lenght of string
print(len(a))
