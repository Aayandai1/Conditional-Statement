#4
print("Student Resource Portal")
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="admin" and password=="ad123":
    print("Access Granted: Faculty Dashboard")
elif username=="student" and password=="st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials.Please try again")

#5
purchase=float(input("enter the purchase amount:"))
member=input("Are you member?(y/n)")
if purchase>1000 and member=="y":
    discount=purchase*0.2
    print(f"Discount amt:{discount}")
    print(f"Final amt:{purchase-discount}")
elif purchase>1000 and member=="n":
    discount=purchase*0.1
    print(f"Discount amt:{discount}")
    print(f"Final amt:{purchase-discount}")
else:
    print(f"Your final price is {purchase}")

#6
print("Welcome to the Magic Forest")
d=input("Go north or south? ")
if d=="north":
    print("Game Over")
else:
    rf=input("Cross the river or follow the path? ")
    if rf=="cross":
        print("Game Over")
    else:
        race=input("Choose Fairy,Ogre or elf? ")
        if race=="elf":
            print("YOU WIN")
        else:
            print("Game Over")

#7
light=input("Enter the light of traffic light(red,yellow,green):")
if light=="red":
    print("Stop")
elif light=="yellow":
    print("Get ready")
elif light=="green":
    print("Go")
else:
    print("Invalid color")

#8
season=int(input("enter season (1-4):"))
match season:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown")

#9
age = int(input("Enter your age: "))
m_income = int(input("Enter your monthly income: "))
c_score = int(input("Enter your credit score: "))
if not (21 <= age <= 60):
    print("Your age must be between 21 and 60")
elif m_income < 30000:
    print("Your monthly income must be at least 30000")
elif c_score < 700:
    print("Your credit score must be at least 700")
else:
    print("Loan Approved")

#10
mass=float(input("enter your body mass:"))
height = float(input("enter your height:"))
bmi = mass/height**2
if bmi<18.5:
    print("you are underweight")
elif 18.5<=bmi<25:
    print("you are normal weight")
elif 25<=bmi<30:
    print("You are overweight")
else:
    print("you are obese")

#11
age=int(input("enter your age:"))
if age<12:
    print("Ticket is free")
elif 12<=age<=60:
    membership=input("Do you have membership card?(yes/no):")
    if membership=="yes":
        print("Ticket is Rs.150")
    else:
        print("Ticket is Rs.200")
elif age>60:
    print("Ticket is Rs.100")

#12
salary=float(input("enter your salary:"))
service=int(input("enter your year of service:"))
if service>5:
    print(f"You get bonus of {salary*0.05:.2f}")
else:
    print("You dont get bonus")

#13
radius=float(input("enter your radius:"))
print(f"Area of circle is {3.14*radius**2:.2f}")

#14
age=int(input("Enter your age:"))
gender=input("Enter your gender:(M or F):")
days=int(input("Enter your days:"))
wage=0
if 18<=age<30:
    if gender=="M":
        wage=700
    elif gender=="F":
        wage=750
    else:
        print("Enter M or F only")
elif 30<=age<=40:
    if gender=="M":
        wage=800
    elif gender=="F":
        wage=850
    else:
        print("Enter M or F only")
else:
    print("You are not eligible to work")
if wage!=0:
    print(f"Your wage is {days * wage}")

#15
num=int(input("Enter the number:"))
if num%3==0 and num%5==0:
    print("Fizz Buzz")
elif num%3==0 and not(num%5==0):
    print("Fizz")
elif num%5==0 and not(num%3==0):
    print("Buzz")
else:
    print(num)

#16
usage=int(input("Electricity usage"))
if usage<100:
    cost=usage*5
elif 100<usage<200:
    cost=100*5+(usage-100)*8
else:
    cost=100*5+200*8+(usage-300)*10
print(f"Your cost is {cost}")

#17
choice1=input("Player 1:Enter rock paper or scissor:")
choice2=input("Player 2:Enter rock paper or scissor:")
game= {"rock","paper","scissor"}
if choice1 not in game or choice2 not in game:
    print("Invalid option")
elif choice1==choice2:
    print("Draw")
elif choice1== "rock" and choice2 =="scissor" or choice1=="paper" and choice2=="rock" or choice1=="scissor" and choice2=="paper":
    print("Player 1 wins")
else:
    print("Player 2 wins")

#18
no=int(input("Enter a number:"))
if no>0:
    if no%2==0:
        print("even")
    else:
        print("odd")
else:
    print("Negative number")

#19
purchase=float(input("enter the purchase amount:"))
member=input("Are you member?(y/n)")
if purchase>1000 and member=="y":
    discount=purchase*0.2
    print(f"Discount amt:{discount}")
    print(f"Final amt:{purchase-discount}")
elif purchase>1000 and member=="n":
    discount=purchase*0.1
    print(f"Discount amt:{discount}")
    print(f"Final amt:{purchase-discount}")
else:
    print(f"Your final price is {purchase}")

#20
e_weight=float(input("Enter your earth's weight:"))
planet=int(input("Enter your planet:(1-7)"))
match planet:
    case 1:
        r=0.38
    case 2:
        r=0.91
    case 3:
        r=0.38
    case 4:
        r=2.53
    case 5:
        r=1.07
    case 6:
        r=0.89
    case 7:
        r=1.14
    case _:
        print("Invalid planet number")
        exit()
d_weight=e_weight*r
print(f"Your weight in destination planet is {d_weight}")

#21
sub1=int(input("Enter marks of 1st subject: "))
sub2=int(input("Enter marks of 2nd subject: "))
sub3=int(input("Enter marks of 3rd subject: "))
sub4=int(input("Enter marks of 4th subject: "))
total = sub1+sub2+sub3+sub4
percentage = total/4
if percentage > 70:
    grade = "distinction"
elif percentage > 60:
    grade = "first"
elif percentage > 40:
    grade = "pass"
else:
    grade = "fail"
print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

#22
balance=20000
correct_pin=3796
print("Welcome to the Global Bank ATM")
is_card_valid=True
if is_card_valid:
    user_pin=int(input("Please enter your pin: "))
    if user_pin == correct_pin:
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")
        choice=int(input("Please enter your choice: "))
        if choice==1:
            print(f"Your balance is {balance}")
        elif choice==2:
            amount=int(input("Please enter your amount: "))
            if amount>0:
                if amount<=balance:
                    balance-=amount
                    print(f"Please collect your cash: Rs.{amount}")
                    print(f"Your balance is {balance}")
                else:
                    print("Error: insufficient funds")
            else:
                print("Amount cannot be negative")
        elif choice==3:
            print("Thank you for visiting. Have a good day!")
        else:
            print("Please enter a valid choice")
    else:
        print("Incorrect Pin")
else:
    print("Invalid card")

#23
floor=int(input("Enter a floor(0-10):"))
if 0<=floor<=10:
    weight=int(input("Enter weight:"))
    if weight<=500:
        door=input("Is door closed(y/n)")
        if door=="y":
            print("Elevator in Motion")
        elif door=="n":
            print("Please close the door")
        else:
            print("Enter y or n")
    else:
        print("Overweight")
else:
    print("Invalid floor number")