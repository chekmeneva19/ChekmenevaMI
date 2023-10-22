numbers = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in numbers]
if all(num == numbers[0] for num in numbers):
    print("Все числа равны")
elif len(set(numbers)) == len(numbers):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")
