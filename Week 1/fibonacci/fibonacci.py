
def fibonacci (limit):

    a, b = 0, 1
    fib = []

    while a <= limit:
        fib.append(a)

        a, b = b, a + b 

    return fib
    
fibSequence = fibonacci(100)

print (fibSequence)
    