numbers = input().split()
result = any(numbers.count(num) > 1 for num in numbers)
print(result)
