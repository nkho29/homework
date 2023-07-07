list1 = []
list1.append(12)
list1.append(5.5)
list1.append("something")
list1.append(True)

print(list1)

list1.remove(True)

print(list1)

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = list(range(21))
for num in numbers:
    if num % 2 == 0:
        print(num)

tuple1 = (10, "smthng", 10.5)
print(tuple1)

tuple2 = tuple(list1)
print(tuple2)
last_element = tuple2[-1]
print(last_element)

dict1 = {
    "month1": "june",
    "month2": "july",
    "month3": "august",
    "month4": "september",
    "month5": "october"
}
print(dict1)
dict1["month6"] = "november"
print(dict1)

month_list = list(dict1.values())
print(month_list)

key_to_remove = ["month4", "month6"]
for key in key_to_remove:
    if key in dict1:
        del dict1[key]
print(dict1)

dict2 = {
    "month7": "december",
    "month8": "january",
    "month9": "february"

}
print(dict2)

dict1.update(dict2)
print(dict1)

