from collections import Counter

def count_and_write_letter_stats(input_file, output_file):
    
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    
    text = ''.join(filter(str.isalpha, text)).lower()

    letter_counts = Counter(text)

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as output:
        for letter, count in sorted_letter_counts:
            output.write(f"{letter}: {count}\n")

if __name__ == "__main__":
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя файла для записи результата: ")

    count_and_write_letter_stats(input_file, output_file)

print("Статистика по буквам успешно записана в файл.")
