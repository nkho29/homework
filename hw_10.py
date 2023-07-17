#

letters1 = ['a', 'b', 'c', 'd']
print([int('3' * 2) // 11])

letters = [2, 4, 6, 8, 10]
letters[2] = 'zero'

metering = [3.14, 'inch', 2.54, 'inch', True]
print(metering.index('inch'))

# append() - вставляє елемент у кінець списку
# insert() - вставляє елемент у певну позицію списку

# list - [], змінний тип данних
# tuple - (), незмінний тип данних

list1 = []
print(tuple(list1))

# список це - yпорядкованість об'єктів
# словник - порядок ключ: значення

dict1 = {
    "five": 5,
    "four": 4,
    "three": 3,
    "two": 2,
    "one": 1
}
print(dict1["five"])
print(dict1["four"])
print(dict1["three"])
print(dict1["two"])
print(dict1["one"])

rivers = {
    'Amazon': 'South America',
    'Dnipro': 'Ukraine',
    'Dunai': 'Austria'
}
for river, region in rivers.items():
    message = f"The {river} runs through {region}"
    print(message)



i = 20
if i < 15:
    print("i is smaller than 15")
    print("I'm in if Block")
else:
    print("i is greater than 15")
    print("I'm in else Block")
    print("I'm not in if and not in else Block")




i = 10
if i == 10:

# First if statement if (i<15):

    print("i is smaller than 15")

# Nested-if statement
# it is true if (i<12):

    print("i is smaller than 12 too")
else:
    print("i is greater than 15")


i = 1
while i <= 10:
    print(i**2)
    i+=1


a = int(input())
while a != 0:
    if a < 0:
        print('int-', a)
        break
    a = int(input())
else:
    print('int+', a)

