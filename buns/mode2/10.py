string = input()
word_list = []
current_word = ""
for char in string:
    if char != " ":
        current_word += char
    else:
        if current_word:
            word_list.append(current_word)
            current_word = ""
if current_word:
    word_list.append(current_word)
new_word = ""
for word in word_list:
    if word:
        last_char = word[-1]
        new_word += last_char
print(new_word)
