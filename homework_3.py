# power
def power(x, n):
    p = x**n
    return p


def main():
    a, b = 5, 3
    c = power(a, b)
    print(c)


main()

# sigma-----------------------------------------------------------------------------------------------------------------


def factor(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


def my_function(x, n):
    total = 0
    for n in range(1, n+1):
        total += power(x, n)/factor(n)
    return total


def main():
    x, n = eval(input('Input two numbers: '))
    print(my_function(x, n))


main()

# isPrime---------------------------------------------------------------------------------------------------------------


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 'Not prime!'
    else:
        return 'Prime!'


def main():
    n = eval(input('Input number: '))
    print(isPrime(n))


main()

# prime-----------------------------------------------------------------------------------------------------------------


def prime(n):
    a = 2
    b = 1
    c = 3
    while b < n:
        if isPrime(c) == 'Prime!':
            b += 1
            a = c
        c += 1
    return a


def main():
    num = eval(input('Input a number: '))
    print(prime(num))


main()

# mersennePrime---------------------------------------------------------------------------------------------------------


def isMersennePrime(n):
    p = 2
    n = (2**p)-1
    a = 1
    while a <= 5:
        if isPrime(n) == 'Prime!':
            print(n)
            p += 1
            a += 1
            n = (2 ** p) - 1
        else:
            p += 1
            n = (2 ** p) - 1


def main():
    isMersennePrime(5)


main()


# factorialRecursive----------------------------------------------------------------------------------------------------


def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


def main():
    n = eval(input('Input number: '))
    print(factorial(n))


main()
# sumRecursive----------------------------------------------------------------------------------------------------------


def my_sum(n):
    total = 0
    for i in range(1, n+1):
        total += 2 * i
    return total


def main():
    n = eval(input('Input number: '))
    print(my_sum(n))


main()
# convert---------------------------------------------------------------------------------------------------------------



# convertRecursive------------------------------------------------------------------------------------------------------

