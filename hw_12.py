list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

converted_list = []
for num in range(10):
    if num % 2 == 0:
        converted_list.append(num // 2)
    else:
        converted_list.append(num * 10)
print(converted_list)


d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num
print(d)

dict_comprehension = {num: num for num in range(1,11) if num % 2 == 1}
print(dict_comprehension)


d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num
    else:
        d[num] = num // 0.5
print(d)

dict_comprehension2 = {num: num if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension2)


dict_comprehension3 = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension3)

converted_dict = {}
for x in range(10):
    if x**3 % 4 == 0:
        converted_dict[x] = x**3
print(converted_dict)


dict_comprehension4 = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension4)

converted_dict2 = {}
for x in range(10):
    if x**3 % 4 == 0:
        converted_dict2[x] = x**3
    else:
        converted_dict2[x] = x
print(converted_dict2)