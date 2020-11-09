# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fibonachi():
    fib1 = fib2 = 1

    n = int(input("Номер элемента ряда Фибоначчи: ")) - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    print(fib2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fibonachi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
