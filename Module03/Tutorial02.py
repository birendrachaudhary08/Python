#Local and Global Variable

#y=50


z=60
def message():
    global z
    z=40
    print("The value of z inside Function: ",z)
print("Before Function, z: ",z)
message()
print("The value of z ouside the function: ",z)

"""This mean there's a completed using for a global keyword
This function is modified for the global variable z and 
the change is a variable outside the function as well
"""
