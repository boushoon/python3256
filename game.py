from random import randint
countStones = randint(4, 30)

winPlayer = False
winComp = False

while countStones > 1:
    print("---------------------------------")
    print(f"Осталось камней - {countStones}")
    print("---------------------------------")

    if countStones >= 4:
        movePlayer = int(input("Сколько камней заберешь? (1, 2 или 3): "))
    elif countStones == 3:
        movePlayer = int(input("Сколько камней заберешь? (1 или 2): "))
    else:
        movePlayer = int(input("Ты можешь взять только 1 камень!: "))

    countStones -= movePlayer
    print("---------------------------------")
    print(f"Осталось камней - {countStones}")
    print("---------------------------------")

    if countStones == 1:
        winPlayer = True
        break

    if countStones >= 4:
        moveComp = randint(1, 3)
        print(f"Компьютер взял {moveComp} камня!")
    elif countStones == 3:
        moveComp = randint(1, 2)
        print(f"Компьютер взял {moveComp} камня!")
    else:
        moveComp = 1
        print(f"Компьютер взял {moveComp} камень!")
    countStones -= moveComp
else:
    winComp = True
print("---------------------------------\n")
print("В кучке остался 1 камень! Игра окончена!\n")
if winPlayer:
    print("Ты победил!")
elif winComp:
    print("Победил компьютер!")