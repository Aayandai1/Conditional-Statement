# #1
# items = ['sql', '123', 'python']
# r=list(filter(lambda x: x.isalpha(), items))
# print(r)

# #2
# products=[
#     {'id':1,'name':'laptop','category':'electronic','price':1200,'instock':True},
#     {'id':2,'name':'smartphone','category':'electronic','price':800,'instock':False},
#     {'id':3,'name':'TV','category':'electronic','price':100,'instock':True},
# ]
# a=list(filter(lambda x:x['instock']==True,products))
# for i in a:
#     print(i['name'])

# #3
# s=lambda x,y:x+y
# diff=lambda x,y:x-y
# m=lambda x,y:x*y
# div=lambda x,y:x/y
# while (c:=int(input("Enter number to perform action(sum=1,difference=2,multiply=3,divide=4,exit=5):")))!=5:
#     a=int(input("enter number:"))
#     b=int(input("enter another number:"))
#     match c:
#         case 1:
#             print(f"Sum:{s(a,b)}")
#         case 2:
#             print(f"difference={diff(a,b)}")
#         case 3:
#             print(f"Multiply:{m(a,b)}")
#         case 4:
#             print(f"Divide:{div(a,b)}")
#         case 5:
#             break
#         case _:
#             print("Invalid operation")

# #4
# def remove_at_idx(l,i):
#     if i<len(l):
#         r=l.pop(i)
#         return l
#     else:
#         return "Invalid index"
# lst=[12,32,3425,1243,14,21]
# i=int(input("Enter index:"))
# print(remove_at_idx(lst,i))

# #5
# r=list(map(lambda x:x**2,range(1,21)))
# for i in range(5):
#     print(r[i])

# #6
# course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate Finance', 'genre': 'commerce'},
#            {'title':'Modern World History', 'genre': 'history'}
#            ]
# r=list(filter(lambda x:x['genre']=='history',course))
# print(r)

# #7
# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net','shyam.kumar@workcorp.com']
# blacklist = ('@hooya.com', '@malware.net')
# r=list(filter(lambda x:x.endswith(blacklist),emails))
# print(r)

# #8
# price = [100, 50, 200, 75]
# r=list(map(lambda x: x*0.8, price))
# print(r)