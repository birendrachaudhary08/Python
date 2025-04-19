# Working With For Loop

#range(5)         #single parameter
#start = 0
#condition < 5
#increment +1

#range(1,6)
#start =1
#condition <6
#increment +1

#range(1,6,2)
#start =1
#condition <6
#increment 2

"""
for n in range(6):
    print(n)

print()
for n in range(1,6):
    print(n)
print()

for n in range(1,6,2):
    print(n) 
"""

#Exercise:

a=int(input("Enter a number: "))

for n in range(1,11):
    print(a," * ",n,"= ",a*n)


print()
for n in range(10,0,-1):
    print(a," * ",n," = ",a*n)