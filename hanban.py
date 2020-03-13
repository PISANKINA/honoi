import sys


sys.setrecursionlimit(100)


def move(n, start, finish):
    if n == 0:
        print("Я ИЗВИНЯЮСЬ, а что вы хотите переносить?")
    elif n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = 6-start-finish
        move(n-1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n-1, temp, finish)


def move_main():
    print('добро пожаловать, сейчас мы вам поможем решить головоломку "Ханойские острава"')
    n = int(input("Введите количество дисков, которые хотите переложить: "))
    start = int(input("введите с какого стержня хотите перенести: "))
    finish = int(input("введите на какой стержень хотите перенести: "))
    move(n, start, finish)


if __name__ == '__main__':
    move_main()
