def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = euclidean_gcd(num1, num2)
print(result)
