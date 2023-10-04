a = int(input())
a_2 = a
a_3 = a
if a <= 0:
    print("Неверный ввод")
else:
    binary = ''
    octal = ''
    hexadecimal = ''
    while a >0:
        binary = str(a%2)+binary
        a //= 2
    while a_2 > 0:
        octal = str(a_2%8) + octal
        a_2 //= 8
    while a_3 > 0:
        reminder = a_3 % 16
        if reminder < 10:
            hexadecimal = str(reminder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + reminder - 10) + hexadecimal
        a_3 //= 16
    print(binary, octal, hexadecimal, sep=',')

    
