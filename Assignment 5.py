#Task 1
dict = {'Mark': 100,
        'Steve': 65,
        'Adrain': 45,
        'Martin': 35,
        'Alice': 77}
check_Name = input("Enter student's name:")

marks = dict.get(check_Name)

if marks == None:
    print(check_Name," is not present")
else:
    print(check_Name,"marks are", marks)

#Task 2
lst1 = []
for i in range(10):
    z = i + 1
    lst1.append(z)
lst2 = lst1[0:5]
lst3 = lst2.reverse()
print(lst1)
print(lst2)
print(lst3)