# Лабораторная №1 задание № 2 / 5 вариант. Вариант с вводом последовательности
# каждая цифра в отдельной строке, завершается ввод последовательности вводом 0
n = 0
DoIt = False
print("Введите последовательность:\n")
num_n = int(input())
if num_n != 0:
    DoIt = True
while DoIt:
    num_c = int(input())
    if num_c == 0:
        break
    if num_n * num_c < 0:
        n += 1
    num_n = int(input())
    if num_n == 0:
        break
    if num_n * num_c < 0:
        n += 1
print("В заданной последовательности чисел знак меняется " + str(n) + " раз(а)")
