#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

coins = int(input("Введите число монеток: "))
side = input("Введите поочерёдно стороны монет, где орёл - 1, а решка - 0: ")
heads = 0
tails = 0

if len(side) == coins:
    for i in side:
        if i == "1":
            heads += 1
        else:
            tails += 1
        
    if heads > tails:
        print(tails)
    else:
        print(heads)
else:
    print("Неверный ввод данных")



