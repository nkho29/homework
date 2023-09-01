for i in 1,2,3,'one','two','three':
    print(i)


for i in range(4):
    print(i)
    print(i**2)
print("End...")


sum = 0
n = 5
for i in range(1, n+1):
    sum +=i
print(sum)


numbers = [12, 25, 98, 156, 36, 87]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print(sum_of_numbers)


names = ["Lewis", "Max", "Logan", "Alex", "George"]
for name in enumerate(names,1):
    print(name)


x = int(input("Number:"))
squares = []

for num in range(1,x):
    if num > 0:
        squares.append(num ** 2)

print("Квадрати додатних чисел менших за", x, ":", squares)


for num in range(15, 0, -1):
    print(num, end=" ")

