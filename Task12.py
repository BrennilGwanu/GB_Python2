#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа i и j (i,j≤1000), а Катя
#должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
x, y = 0, 0
for i in range(s):
    for j in range(s):
        if i + j == s and i * j == p:
            x = i
            y = j

if x != 0 and y != 0:
    print(x, y)
else: 
    print("Нет подходящих значений")
