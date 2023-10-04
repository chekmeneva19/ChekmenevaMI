def dublicates(sequence):
    string = str(sequence)
    numbs = []
    for symb in string:
        if symb in numbs:
            return True
        numbs.append(symb)
    return False
sequence = input()
res = dublicates(sequence)
print(res)

