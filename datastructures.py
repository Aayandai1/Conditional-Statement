#1
items=[3,5,7,9,11,13]
removed_item=items.pop(4)
items.insert(2,removed_item)
items.append(removed_item)
print(items)

#2
first_set={23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}
common=first_set&second_set
first_set-=common
print(first_set)

#3
first_set={27,43,34}
second_set={34,93,22,27,43,53,48}
if first_set.issubset(second_set):
    first_set.clear()
    print("first_set was subset and has been cleared")
elif first_set.issuperset(second_set):
    second_set.clear()
    print("second_set was subset and has been cleared")
else:
    print("No subset/superset relationship found")
print(f"first_set: {first_set}")
print(f"second_set: {second_set}")

#4
month={'jan':47,'feb':52,'march':47,'April':44,'May':52,'June':53,'july':54,'Aug':44,'Sept':54}
unique_values=list(set(month.values()))
print(unique_values)

#5
sample_list=[87,45,41,65,94,41,99,94]
unique_list=list(set(sample_list))
unique_tuple=tuple(unique_list)
min_value=min(unique_tuple)
max_value=max(unique_tuple)
print(f"Tuple: {unique_tuple}")
print(f"Minimum: {min_value}, Maximum: {max_value}")

#6
club_A={"ram","hari","shyam"}
club_B={"ram","gita","hari"}
common_members=club_A&club_B
if common_members:
    print(f"{common_members} members exist in both groups")
else:
    print("no overlapping members found between groups")

#7
required_tasks={"Email","Report","Meeting"}
completed_tasks={"Email","Report"}
if required_tasks.issubset(completed_tasks):
    print("all tasks done")
else:
    pending=required_tasks-completed_tasks
    print(f"some tasks pending: {pending}")

#8
student_emails={"ram":"ram@example.com","sita":"sita@example.com","laxman":"laxman@example.com"}
name=input("Enter student name: ")
if name in student_emails:
    print(f"Email: {student_emails[name]}")
else:
    print("contact not found")

#9
shopping_list={"Milk","Bread","Eggs"}
bought={"Bread","Eggs"}
unbought=shopping_list-bought
if unbought:
    print(f"Unbought items: {unbought}")
else:
    print("Shopping complete")

#10
class_list=["ram","sita","laxman"]
new_student=input("Enter student name to add: ")
if new_student not in class_list:
    class_list.append(new_student)
    print(f"{new_student} added to the list")
else:
    print(f"{new_student} already present")

#11
votes=["Blue","Red","Blue","Green","Blue"]
blue_count=votes.count("Blue")
if blue_count>=3:
    print("Blue wins")
else:
    print("Blue did not win")

#12
grades={"Ram":92,"Sita":88}
student_name=input("Enter student name: ")
if student_name in grades:
    print(f"Grade: {grades[student_name]}")
else:
    print("Grade is not available")

#13
applicant={"name":"Priya","skills":["Java","SQL"],"experience_years":1}
required_skills={"Python","Java"}
has_skill=False
for skill in applicant["skills"]:
    if skill in required_skills:
        has_skill=True
        break
has_experience=applicant["experience_years"]>=2
if has_skill and has_experience:
    print("priya qualifies")
else:
    print("priya does not qualify")

#14
weight=float(input("Enter baggage weight: "))
item=input("Enter item name: ").lower()
banned_items={"scissors","knife","lighter"}
if weight<=7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")

#15
sample_dict={
    'emp1':{'name':'Jhon','salary':7500},
    'emp2':{'name':'Emma','salary':8000},
    'emp3':{'name':'Shyam','salary':500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)

#16
ram_items={"apple","banana","orange"}
laxman_items={"grape","mango","apple"}
if ram_items.isdisjoint(laxman_items):
    print("they picked completely different items")
else:
    common=ram_items&laxman_items
    print(f"they have some common items: {common}")