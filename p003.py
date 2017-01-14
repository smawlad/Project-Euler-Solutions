#checks if number is a prime number
def pf(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return False
        else:
            return True

#returns prime factor
def f(n):
    for i in range(1, n + 1):
        if (n % i == 0):
            if (pf(i)):
                print(i)



if __name__ == '__main__':
    f(600851475143)
