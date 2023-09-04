def func_Pr(x,y,d):
    sum_pr = x + y + d
    return sum_pr
print(func_Pr(3,4,5))


def func_add(x, y):
    sum_args = x + y
    return sum_args
print(func_add(8,10))


def func_min(x, y):
    dif_args = x - y
    return dif_args
print(func_min(5,4))


def func_name(name="Nazar"):
    return name
print(f"Hello, my name is {func_name()}")


def func_S(x, y):
    ar_result = x * y
    return ar_result
print(func_S(8, 10))


def func_prsn(age, name, surname):
    return age, name, surname

print(func_prsn(15, "Nazar", "Khomych"))


def func_racecar(**kwargs):
    for key, item in kwargs.items():
        print(f"{key}: {item}")
func_racecar(name="Porshe", model="911", bhp=550, weight=1100, price=200000)


def func_list(*args):
    first_elem = args[0]
    last_elem = args[4]
    second_elem = [1]
    if first_elem == 2:
        return first_elem, last_elem
    else:
        return second_elem + first_elem

print(func_list(2, 4.4, True, "text", [0, 21, False]))


def func_divis(*args):
    div_result = args[0] / args[1] / args[2]
    return div_result

print(func_divis(4, 2, 0.5))


def func_multi(a, b):
    multi_result = a * b
    return multi_result

print("Result will be:", func_multi(99, 200))


# def func_imp(a, b):
#     num = input("Number: ")
#     return num
# print(f"number: {func_imp()}")