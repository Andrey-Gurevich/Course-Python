"""
Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
Подсчитать количество символов в последнем слове F2.
Требуемые файлы: F1.txt
"""
with open("F1.txt", "r") as file:
    s = file.readlines()
with open("F2.txt", "w") as file:
    for i in range(3, len(s)):
        file.write(s[i])
with open("F2.txt", "r") as file:
    last = file.readlines()[-1]
    s = last.split()
    print("Количество символов в последнем слове " + str(len(s[len(s)-1])))
