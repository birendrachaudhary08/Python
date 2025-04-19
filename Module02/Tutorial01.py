# IF, Elif, Else condtion

# WAP to find the greatest of 3 numbers entered by the user

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third  number: "))

if a>b and a>c:
    print("First number is greater")
elif b>a and b>c:
        print("Second number is greater")
else:
          print("Third number is greater")
