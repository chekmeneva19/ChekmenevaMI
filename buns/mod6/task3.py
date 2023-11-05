def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

def armstrong_numbers_generator():
    for number in range(10, 10**6):
        if is_armstrong_number(number):
            yield number
for armstrong_number in armstrong_numbers_generator():
    print(armstrong_number, end=' ')




