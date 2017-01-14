def product():
    li = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            if(str(product) == str(product)[::-1]):
                li.append(product)

    return max(li)

if __name__ == '__main__':
    print(product())
