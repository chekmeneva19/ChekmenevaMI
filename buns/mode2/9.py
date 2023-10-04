string = input()
vowels = 0
consonants = 0
for char in string:
    char = char.lower()
    if char >= 'а' and char <= 'я':
        if char in 'аеёиоуыэюя':
            vowels += 1
        else:
            consonants += 1

print(vowels, consonants)
        
