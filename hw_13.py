import time

current_time = time.localtime()
print(f"Зараз: {current_time}")

start_time = time.time


list_iter = [False, 2, 3, "hello", 50]
str_iter = "Hello world"
for i in str_iter:
    print(i)

end_time = time.time()
print(f"Час виконання: {end_time} секунд")



list_compreh1 = [i for i in str_iter]
print(list_compreh1)


for i in range(4):
    print(i)

list_compreh2 = [i for i in range(4)]
print(list_compreh2)

list_4 = []
for i in range(0,20,2):
    list_4.append(i)
print(list_4)

list_compreh3 = [item for item in range(0,20,2)]
print(list_compreh3)

