number = input()
new_number = ""
valid_symbs = "0123456789+"
for symb in number:
    if symb in valid_symbs:
        new_number += symb
print(new_number)
