#Creating and manipulating lists


"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.

Lists are created using square brackets
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

List Method 
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""
cars= ["BMW","THAR","Range Rover", "Audi", "Porsche","Lamborghini"]

#       0       1       2              3        4           5


print("First Car: ", cars[0])
print("Fourth Car: ",cars[3])

cars[1]="Bugatti"
print("Modified List: ", cars)

cars.append("Ferrari")
print("List after adding a car: ",cars)

cars.remove("BMW")
print("List after removing a car: ",cars)


