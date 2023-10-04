barcode = input()
odd = 0
even = 0

for digit in range(len(barcode)):
    if digit % 2 == 0:
        odd += int(barcode[digit])
    else:
        even += int(barcode[digit])

if (odd + even*3)%10 ==0:
    print("Yes")
else:
    print("No")
