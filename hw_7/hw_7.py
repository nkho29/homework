dict1 = {"oranges": "15", "apples": "10", "strawberries": "20"}
print(dict1)

# new_fruit = "banana"
# new_price = "13"
# dict1[new_fruit] = new_price
# print(dict1)

new_element = {"banana": "13"}
dict1.update(new_element)
print(dict1)

# remowed_element = dict1.pop("banana")
# print(dict1)
# print(remowed_element)

del dict1["strawberries"]
print(dict1)

list1 = [1, 2, 3, 5, 0]
print(list1)

list1.append(29)
print(list1)

tuple1 = ("something", "write", "there" )
print(tuple1)
# tuple незмінний тип данних

set1 = {1, 2, 2, 3, 3, 4, 4, 555, 6, 6, 6}
print(set1)

a = 1
b = 100

if b > a:
    print("Умова виконується!!!")
if b < a:
    print("Умова не виконується!!!")
if b != a:
    print("Умова не виконується!!!")
