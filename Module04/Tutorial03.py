#Creating and Accessing Dictionaries
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:


Dictionary Methods:
clear()     :	Removes all the elements from the dictionary
copy()      :	Returns a copy of the dictionary
fromkeys()  :	Returns a dictionary with the specified keys and value
get()       :	Returns the value of the specified key
items()     :	Returns a list containing a tuple for each key value pair
keys()      :	Returns a list containing the dictionary's keys
pop()       :	Removes the element with the specified key
popitem()   :	Removes the last inserted key-value pair
setdefault():	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()    :	Updates the dictionary with the specified key-value pairs
values()    :	Returns a list of all the values in the dictionary

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964

}
print(car)
print(len(car))

# Acessing the items in cars
x = car.get("model")
print(x)


#The keys() method will return a list of all the keys in the dictionary.
y = car.keys()
print(y)


#The values() method will return a list of all the values in the dictionary.
z = car.values()
print(z) #before the change
car["year"] = 2020
print(z) #after the change


#The items() method will return each item in a dictionary, as tuples in a list.
a = car.items()
print(a) #before the change
car["color"] = "red"
print(a) #after the change

#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")