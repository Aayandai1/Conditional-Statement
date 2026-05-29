#1
# for i in range(1,6):
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

#2
# total=0
# li = [10,20,30,40]
# for i in li:
#     total+=i
# print(f"Total sum {total}")

#3
# student_names = ["Ram", "Hari", "Sita"]
# print("Email Greetings Generated")
# for Name in student_names:
#     print(f'Hi {Name}, your course approval is ready!')

#4
# ch= [45, 30, 50, 40]
# Number=0
# print("Book Chapter Summary")
# for Pages in ch:
#     Number +=1
#     print(f'Chapter {Number} has {Pages} pages.')

#5
# mlt=[4,5,3,2]
# pr=1
# for i in mlt:
#     pr*=i
# print(pr)

#6
# number=11
# for i in range(1,11):
#     print(f"{number}*{i}={i*number}")

#7
# lst=[3,2,1,4,5]
# newlst=list()
# for i in range(len(lst),0,-1):
#     newlst.append(i)
# print(newlst)

#8
# n1= [1,2,3,4,5]
# n2= [3,4,5,6,7]
# common=list()
# for i in range(len(n1)):
#     if n1[i] in n2:
#         common.append(i)
# print("Common numbers=",common)

#9
# lst = [1, 2, 3, 4]
# for i in lst:
#     if i==1 or i==4:
#         print(i)

#10
# v=['a', 'e', 'i', 'o', 'u']
# st=input("Enter a string:")
# nst=str()
# for i in range(len(st)):
#     if st[i] not in v:
#         nst+=st[i]
# print(nst)

#11
# sen=input("Enter a sentence")
# v=['a', 'e', 'i', 'o', 'u']
# vowel=0
# consonant=0
# for i in range(len(sen)):
#     if sen[i].isalnum():
#         if sen[i] in v:
#             vowel+=1
#         else:
#             consonant+=1
# print(f"Vowel={vowel} Consonant={consonant}")

#12
# lst= [1,2,3,4,5]
# odd=[]
# even=[]
# for i in lst:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even={even} Odd={odd}")

#13
# n=int(input("Enter a number:"))
# f=0
# for i in range(1,n+1):
#    if n%i==0:
#        f=f+1
# if f==2:
#     print("Prime")
# else:
#     print("Not prime")

#14
# lst= [1,2,3,4,"a","b"]
# num=list()
# st=list()
# for i in range (len(lst)):
#     if isinstance(lst[i],str):
#         st.append(lst[i])
#     if isinstance(lst[i],int):
#         num.append(lst[i])
# print(f"String={st} and Integer={num}")

#15
# st=input("Enter a string:")
# s=0
# n=0
# for i in st:
#     if i.isalpha():
#         s+=1
#     elif i.isnumeric():
#         n+=1
# print(f"Digits={n} Letters={s}")

# #16
# username=input("Enter a username:")
# if not username.isalpha:
#     print("Invalid username")
#     exit()
# password=input("Enter a password:")
# if not password.isalnum :
#     print("Invalid password")
#     exit()
# print("Valid username and Password")

#17
# n=int(input("Enter a number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

#18
# n=int(input("Enter a :"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f"Factorial={f}")

#19
# mlt=[1,2,3,4,5,6,7,8 ]
# for i in mlt:
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")

#20
# lst=[1,2,3,4]
# for i in lst:
#     if i==1 and i==2:
#         print(i)

#21
# n=int(input("Enter a number:"))
# s=0
# for i in range(1,n+1):
#     if i%2!=0:
#         s+=i
# print(f"Sum={s}")

#22
# n=int(input("Enter a number:"))
# s=0
# for i in range(1,n+1):
#     if i%2==0:
#         s+=i
# print(f"Sum={s}")

#23
# st=input("Enter a string")
# sp=0
# for i in st:
#     if i==" ":
#         sp+=1
# print(f"Space={sp}")

#24
# n= [1,2,3,4]
# r=list()
# for i in n:
#     r.append(i**3)
# print(r)

#25
# a="programming"
# rev=""
# for i in range (len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)

#26
# for i in range(50):
#     print(i)
#     if i==7:
#         break

#27
# st=input("Enter a string:")
# for i in st:
#     print(i)

#28
# a= ["ram","shyam",1,2]
# for i in a:
#     if i.isalpha():
#         print(f"Hello!,{i}")

#29
# a=["ram","shyam",1,2]
# new=[]
# for i in a:
#     b="Dr."+ str(i)
#     new.append(b)
# print(new)

#30
# a=input("Enter a list of numbers:")
# a=list((a.replace(" ","")))
# new=[]
# for i in a:
#     s=int(i)**2
#     new.append(s)
# print(new)

#31
# lst1=[111, 32, -9, -45, -17, 9, 85, -10]
# p=[]
# for i in lst1:
#     if i>0:
#         p.append(i)
# print(f"Positive={p}")

#32
# lst=[0,1,2,3,4,5,6]
# for i in lst:
#     if i!=3 and i!=6:
#         print(i)

#33 & 34
# first = [1, "hello", 3.14, True, None]
# second = []
# for x in first:
#     second.append(type(x).__name__)
# else:
#     print("Done")
# print(second)

#35
# for i in range(105,6,-7):
#     print(i,end=" ")

#36
# bad_chars = [';', ':', '!', '*']
# string = "py;th* o:n ! ;py * t*h:o !n"
# result = ""
# for ch in string:
#     if ch not in bad_chars and ch != ' ':
#         result += ch
# print(result)

#37
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = 0
# odd = 0
# for n in numbers:
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"Even={even}")
# print(f"Odd={odd}")

#38
# r=int(input("Enter the range(3-99):"))
# s=0
# for i in range(1,r):
#    if i%3==0 or i%5==0:
#        s+=i
# print(f"Sum={s}")

#39
# even=0
# odd=0
# for i in range(1,100):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Even={even} Odd={odd}")

#40
# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count=0
# for i in list1:
#     if i == target:
#         count+=1
# print(f"{target} appears {count} times")
