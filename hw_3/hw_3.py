list1 = []
list2 = (["winter", "spring", "summer"])
list2.append("autumn")
list3 = ([1, 2, 3, 4, 5])
print(list3)
all_list = list1, list2
print(type(all_list), list1, list2)
# f-string
birthday = '05/10/1985'.split('/')
print(birthday)
print(f"Im born on {birthday[0]} october {birthday[2]} year")

print(list2[2])