"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
A Sets are written with curly brackets.


Set Method:

add()                   :	 	Adds an element to the set
clear()                 :	 	Removes all the elements from the set
copy()                  :	 	Returns a copy of the set
difference()            :   -	Returns a set containing the difference between two or more sets
difference_update()     :   -= 	Removes the items in this set that are also included in another, specified set
discard()               :	 	Remove the specified item
intersection()          :	&	Returns a set, that is the intersection of two other sets
intersection_update()   :	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()            :	 	Returns whether two sets have a intersection or not
issubset()              :	<=	Returns whether another set contains this set or not
 	                    :    <	Returns whether all items in this set is present in other, specified set(s)
issuperset()            :	>=	Returns whether this set contains another set or not
 	                    :   >	Returns whether all items in other, specified set(s) is present in this set
pop()                   :	 	Removes an element from the set
remove()                :	 	Removes the specified element
symmetric_difference()  :	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()   :	^=	Inserts the symmetric differences from this set and another
union()	                :    |	Return a set containing the union of sets
update()                :	|=	Update the set with the union of this set and others

"""

#my_set ={1,2,3,4,5}
#print("The entire set: ",my_set)

#my_set.add(6)
#print("After Adding the element: ",my_set)

#my_set.remove(2)
#print("After removing an element: ",my_set)


A={1,2,3,4,5,7,8,9}
B={2,4,6,8}

union_set=A.union(B)
print("Union of A and B: ",union_set)

intesection_set =A.intersection(B)
print("Intersection of A and B: ",intesection_set)

difference_set = B.difference(A)
print("Difference of A and B: ",difference_set)

