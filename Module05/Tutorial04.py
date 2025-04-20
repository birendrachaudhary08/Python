
#concatenate and format string

#concatenate
a="Hello\t"
b="World"

c=a+b
print(c)


#format() String

name="Jonny"
age=50
salary=50000000

"""F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, 
and add curly brackets {} as placeholders for variables and other operations.
"""

txt=f"Name:{name}\t Age:{age}\t Salary:{salary}"
print(txt)



#A placeholder can contain variables, operations, functions, and modifiers to format the value.
placeholder = "Name: {} Age: {} and Salary: {}".format(name,age,salary)
print(placeholder)
#A placeholder can include a modifier to format the value.

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f 
# which means fixed point number with 2 decimals:
intro = "Name: {} Age: {} and Salary: {:.2f}".format(name,age,salary)
print(intro)