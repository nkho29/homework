def func_data(*args):
    list_int_num = []
    # print(args)
    for arg in args:
        # print(type(arg))
        if type(arg) == int:
            list_int_num.append(arg)
    sum_of_num = sum(list_int_num)
    return sum_of_num



print(func_data(1, 3, 4, 5, "Hello", "Smthn", "Hi"))


# def func_data(*args):
#     sum2 = 0
#     for arg in args:
#         if isinstance(arg, int):
#             sum2 += arg
#     return sum2
#
# print(func_data(1, 3, 4, 5, "7", "5", "8"))


