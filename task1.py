def main():
    n = int(input())
    res = 1
    if n < 0:
        print("Введите неотрицательное число!")
        return 0
    for i in range (2, n + 1):
        res *= i
    print(f"{n}! = {res}")

main()