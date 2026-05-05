#1
# age=int(input("enter your age:"))
# height=float(input("enter your height in cm:"))
# if age>=12 and height>=140:
#     print("You can ride the roller coaster")
# else:
#     print("You cannot ride the roller coaster")


#2
# light=input("Enter the light of traffic light(red,yellow,green):")
# if light=="red":
#     print("Stop")
# elif light=="yellow":
#     print("Get ready")
# elif light=="green":
#     print("Go")
# else:
#     print("Invalid color")
#another method using dictionary
# light=input("Enter the light of traffic light(red,yellow,green):")
# lightcolor={"red":"stop","yellow":"Get ready","green":"Go"}
# if light in lightcolor:
#     print(lightcolor[light])
# else:
#     print("Invalid color")

#3
# season=int(input("enter season (1-4):"))
# match season:
#     case 1:
#         print("Spring")
#     case 2:
#         print("Summer")
#     case 3:
#         print("Autumn")
#     case 4:
#         print("Winter")
#     case _:
#         print("Unknown")

#4
# username=input("Enter username:")
# if username == "admin":
#     password=input("Enter password:")
#     if password == "pass123":
#         print("Login successful")
#     else:
#         print("Password does not match")
# else:
#     print("Username does not match")

#5
# age = int(input("Enter your age: "))
# m_income = int(input("Enter your monthly income: "))
# c_score = int(input("Enter your credit score: "))
# if not (21 <= age <= 60):
#     print("Your age must be between 21 and 60")
# elif m_income < 30000:
#     print("Your monthly income must be at least 30000")
# elif c_score < 700:
#     print("Your credit score must be at least 700")
# else:
#     print("Loan Approved")

#6
# age=int(input("enter your age:"))
# if age<12:
#     print("Ticket is free")
# elif 12<=age<=60:
#     membership=input("Do you have membership card?(yes/no):")
#     if membership=="yes":
#         print("Ticket is Rs.150")
#     else:
#         print("Ticket is Rs.200")
# elif age>60:
#     print("Ticket is Rs.100")

#7
# salary=float(input("enter your salary:"))
# service=int(input("enter your year of service:"))
# if service>5:
#     print(f"You get bonus of {salary*0.05:.2f}")
# else:
#     print("You dont get bonus")

#8
# radius=float(input("enter your radius:"))
# print(f"Area of circle is {3.14*radius**2:.2f}")

#9
# age=int(input("Enter your age:"))
# gender=input("Enter your gender:(M or F):")
# days=int(input("Enter your days:"))
# wage=0
# if 18<=age<30:
#     if gender=="M":
#         wage=700
#     elif gender=="F":
#         wage=750
#     else:
#         print("Enter M or F only")
# elif 30<=age<=40:
#     if gender=="M":
#         wage=800
#     elif gender=="F":
#         wage=850
#     else:
#         print("Enter M or F only")
# else:
#     print("You are not eligible to work")
# if wage!=0:
#     print(f"Your wage is {days * wage}")

#10
# num=int(input("Enter the number:"))
# if num%3==0 and num%5==0:
#     print("Fizz Buzz")
# elif num%3==0 and not(num%5==0):
#     print("Fizz")
# elif num%5==0 and not(num%3==0):
#     print("Buzz")
# else:
#     print(num)