def sumOfEven():
    total = 0
    a, b = 1, 2

    while a <= 4000000:
        if (a % 2 == 0):
            total += a

        a, b = b, a + b

    return total


if __name__ == '__main__':
    print(sumOfEven())
