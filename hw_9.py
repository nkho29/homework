dict1 = {
    "fruit1": "banana",
    "fruit2": "apple"
}
print(dict1)

dict1["fruit3"] = "orange"
print(dict1)

del dict1["fruit1"]
print(dict1)


list1 = [1, 2, 4, 5, 6]
print(list1)

list1.append(3)
print(list1)


tuple1 = (1, 4.5, "word")
print(tuple1)

set1 = {"a", "b", "c", 1, 2, 3}
print(set1)


a = 1
b = 100
if a < b:
    print("Умова виконується!!!")
elif a > b:
    print("Умова не виконується!!!")
elif a != b:
    print("Умова не виконується!!!")
