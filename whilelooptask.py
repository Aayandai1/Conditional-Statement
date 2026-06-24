# #1
# a=list()
# while True:
#    n=int(input("Enter a number:"))
#    if n in a:
#        print("Duplicate number!")
#        break
#    a.append(n)
#print(f"Numbers entered:{a}")


# #2
# n=int(input("Enter a positive number:"))
# m=1
# f=1
# while m<=n:
#     f=f*m
#     m=m+1
# print("Factorial={}".format(f))

# #3
# n=int(input("Enter a number: "))
# s=0
# i=0
# while s<=n:
#     s=s+i
#     i+=1
# print(f"Sum:{s}")

# #4
# l=[1,2,2,2,3,4,4,5,5,6,7,7,1,10,10,10,10]
# i=0
# c=0
# n = int(input("Enter number to find how many time it is repeated:"))
# while i<len(l):
#     if n == l[i]:
#         c+=1
#     i+=1
# print("The number is repeated {} times.".format(c))

# #5
# s=input("Enter a sentence:")
# i=0
# v=0
# c=0
# while i<len(s):
#     if s[i].isalpha():
#         if s[i] in 'aeiou':
#             v+=1
#         else:
#             c+=1
#     i+=1
# print(f"vowels:{v} Consonants:{c}")

# #6
# n=int(input("Enter number:"))
# c=0
# while n!=0:
#     c+=1
#     n//=10
# print("No of digits={}".format(c))

# #7
# n=int(input("Enter a number:"))
# s=[n]
# while n!=1:
#     if n%2==0:
#         n//=2
#     else:
#         n=n*3+1
#     s.append(n)
# print(s)

# #8
# n=ord('A')
# while n<=ord('Z'):
#     print(f"{chr(n)}",end=" ")
#     n=n+1

# #9
# s=int(input("Enter starting number:"))
# e=int(input("Enter ending number:"))
# while s<=e:
#     print(s,end=" ")
#     s=s+1

# #10
# n=50
# while n>0:
#     if n%2!=0:
#         print(n,end=" ")
#     n-=1

# #11
# n=7
# i=2
# m=7
# while m<=100:
#     print(m,end=' ')
#     m=n*i
#     i+=1

# #12
# s=0
# while True:
#     n=int(input("Enter number:"))
#     if n==0:
#         break
#     s=s+n
# print("Sum={}".format(s))

# #13
# while True:
#     age=int(input("Enter your age:"))
#     if 0<age<120:
#         print("Age valid")
#         break
#     print("Invalid age!!")

# #14
# c=0
# a=0
# while (n:=int(input("Enter score:")))>=0:
#     c+=1
#     a=a+n
# print(f"Average = {a/c}")

# #15
# c=0
# correct_pass='secret123'
# while c<3:
#     try_password=input("enter your password:")
#     if try_password==correct_pass:
#         print("Access granted")
#         break
#     else:
#         print("Access denied")
#     c+=1

# #16
# n=int(input("enter the number:"))
# r=0
# while n!=0:
#     a=n%10
#     r=r*10+a
#     n=n//10
# print(f"Reverse:{r}")

# #17
# n=int(input("enter the number of terms:"))
# a=0
# b=1
# while n>0:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     n-=1

# #18
# s=input("Enter a string:")
# i=0
# r=""
# while i<len(s):
#     if s[i].lower() not in "aeiou":
#        r+=s[i]
#     i+=1
# print(r)

# #19
# s=input("Enter a string:")
# i=0
# c=0
# while i<len(s)-1:
#     if s[i]+s[i+1]=='hi':
#         c+=1
#     i+=1
# print(f"hi is repeated {c} times")

# #20
# numbers = [12, 25, 7, 30, 18, 40, 55, 9]
# i=0
# while i<len(numbers):
#     if numbers[i]%5==0:
#         print(numbers[i],end=" ")
#     i+=1

# #21
# s=input("Enter a string:")
# i=0
# r=''
# while i<len(s):
#     if s[i].islower():
#         r+=s[i].upper()
#     elif s[i].isupper():
#         r+=s[i].lower()
#     else:
#         r+=s[i]
#     i+=1
# print(r)

#22
#The inner loop runs 4 times

#23
#The value of variable j is assigned above the loop, because of which once the value of j is 2 it is not reseted and The inner loop does not run after running 2 times

#24
#The value of x is 5

#25
#No,when the user inputs -1 the loop is terminated and the total value 4+7=10 is printed

#26
#The word loop is not printed even once. The final value of x is 20

#27
#The variable x evaluates to false when its value becomes 0 after the loop executes 3 times

#28
#Fibonnaci series is printed

# #29
# sample_string='The quick Brow Fox'
# i=0
# u=0
# l=0
# while i<len(sample_string):
#     if sample_string[i].isupper():
#         u+=1
#     elif sample_string[i].islower():
#         l+=1
#     i+=1
# print(f"Uppercase characters:{u} Lowercase characters:{l}")

# #30
# while 0<(c:=int(input("Enter action(1 to find sum, 2 to find difference,3 to find product and 4 to exit the loop:"))) <4:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     if c==1:
#         print(a+b)
#     elif c==2:
#         print(a-b)
#     elif c==3:
#         print(a*b)

# #31
# p=0
# ne=0
# while (n:=int(input("Enter a no:"))) !=0:
#     if n>0:
#         p+=1
#     else:
#         ne+=1
# print(f"Positive numbers:{p} Negative numbers:{ne}")

# #32
# s=int(input("Enter starting number:"))
# e=int(input("Enter ending number:"))
# while s<e:
#     i=1
#     c=0
#     while i<=s:
#         if s%i==0:
#             c=c+1
#         i+=1
#     if c==2:
#         print(s,end=" ")
#     s+=1

# #33
# numbers = [12, 40, 21, 31, 10, 7, 5]
# i=0
# while i<len(numbers):
#     if numbers[i]<20:
#         print(numbers[i],end=" ")
#     i+=1

# #34
# numbers = [45, 60, 12, 75, 30, 55, 8, 90]
# new_numbers = []
# i=0
# while i < len(numbers):
#     if numbers[i] > 50:
#         new_numbers.append(0)
#     else:
#         new_numbers.append(numbers[i])
#     i+=1
# print(new_numbers)

# #35
# numbers = [15, 25, 30, 45, 60, 12, 90, 7]
# i=0
# c=0
# while i<len(numbers):
#     if numbers[i]%3==0 and numbers[i]%5==0:
#         c+=1
#     i=i+1
# print(f"The number of numbers divisible by 3 and 5 is {c}")

# #36
# numbers = [10, 15, 25, 30, 45]
# i=0
# sortedd="Sorted"
# while i<len(numbers)-1:
#     if numbers[i] > numbers[i+1]:
#         sortedd="Not sorted"
#         break
#     i+=1
# print(sortedd)

# #37
# s=ord('a')
# while s<=ord('z'):
#     print(chr(s),end=" ")
#     s=s+1

# #38
# page_counts=[45, 30, 50,40]
# c=0
# while c<len(page_counts):
#     print(f"Chapter {page_counts[c]} has {c+1} pages")
#     c+=1

# #39
# n1=[1,2,3,4,5]
# n2=[3,4,5,6,7]
# a=[]
# i=0
# while i<len(n1):
#     if n1[i] in n2:
#         a.append(n1[i])
#     i+=1
# print(f"Repeated numbers: {a}")

# #40
# n=2
# while n<=8:
#     i=1
#     if n in [2,4,6,7,8]:
#         while i<=10:
#             print(f"{n}*{i}={i*n}")
#             i+=1
#     n+=1

# #41
# num= [45, 60, 12, 75, 30, 55, 8, 90]
# i=0
# dup="No duplicate"
# while i < len(num)-1:
#     j=i+1
#     while j < len(num):
#         if num[i]==num[j]:
#             dup="Duplicate"
#             break
#         j+=1
#     if dup == "Duplicate":
#         break
#     i+=1
# print(dup)
