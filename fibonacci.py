## primes in fibonacci
from test import test


def is_prime(number):
    if number <= 0:
        return False
    if number == 2:
        return True
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

def s_primes():
    begin = True
    fib_member = 1
    while begin:
        if is_prime(fibonacci(fib_member)):
            print(fibonacci(fib_member), fib_member)
            ask = input("procurar por mais primos em fibonacci? y/n \n")
            if ask != "y":
                begin = False
        fib_member += 1
        
## questao de harvard
def harvard_question():
    control = True
    i = 1
    while control:
        a = (100 + i ** 0.5) ** 0.5
        b = (100 - i ** 0.5) ** 0.5
        c = int(a + b)
        if c == a + b:
            print(i)
            control = False
        i += 1
    
harvard_question()

