def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

def find_palindrome(word):
    if is_palindrome(word):
        print(f"Можно составить палиндром: '{word}'")
    else:
        print(f"Нельзя составить палиндром.")
word = input("Введите слово: ")
find_palindrome(word)
