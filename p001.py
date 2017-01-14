def sumOfMultiples(n):
    li = []

    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            li.append(i)

    for elements in li:
        total = sum(li)

    return total

if __name__ == '__main__':
    print(sumOfMultiples(1000))
