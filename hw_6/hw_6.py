print('and:')
print(False and False)
print(True and True)

print('or:')
print(False or False)
print(True or True)

print('not:')
print(not True)

# Логічні вирази
a = True;b = False;c = True
f = a and not b or c or (a and(b or c))
print(f)

a = 2; b = 5
print(a < b)       # менше
print(b > 3)       # більше
print(a <= 2)      # менше дорівнює
print(b >= 7)      # більше дорівнює
print(a < 3 < b)   # подвійне порівняння
print(a == b)      # рівність
print(a != b)      # нерівність
print(a is b)      # ідентичність об'єктів
print(a is not b)  # a і b - різні об'єкти
# (хоча їхні значення можуть бути однаковими - рівними)