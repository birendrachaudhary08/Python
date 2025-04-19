#Creating and manipulating lists
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


"""List operation and method
    1.append : use to add single element
    2.extend : use to add multiple element
    3.insert : use to add element with their address  .insert(1,"Element")
    4.remove : use to delete the element from list
    4.pop : use to delete the element from list 

"""