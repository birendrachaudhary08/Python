#creating and blocking passwords

password="Learn@123"
your_answer=""
number_of_try=0
number_max_of_try =3
Max_try="Password not reached"


while your_answer!=password and Max_try!="Reached":
     if number_of_try<number_max_of_try:
        your_answer=input("Enter your Password: ")
       
        number_of_try=number_of_try+1
     else:
        Max_try="Reached"



if Max_try=="Reached":
    print("Account is Blocked")
else:
    print("Access Granted")