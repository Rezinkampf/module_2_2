fist = int(input("Введите первое число: "))
second = int(input("Введите первое число: "))
third = int(input("Введите первое число: "))
if fist==second==third:
    print(3)
elif fist==second or second==third or fist==third:
    print(2)
else:
    print(0)