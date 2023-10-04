s = input()
i = input()
count = 0
for char in s:
    if char == i:
        count+=1
    else:
        break
print(count)
