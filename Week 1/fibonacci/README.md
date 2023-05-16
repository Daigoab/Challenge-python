# Challenge-python
# Fibonacci Sequence 

The code defines a function fibonacci that takes a limit parameter as input and generates the Fibonacci sequence up to that limit. It then calls this function with a limit of 100 and stores the resulting sequence in the variable fib_sequence. It then prints out the Fibonacci sequence.

A variable is first created that assigns 'a' and 'b' to '0' and '1'. An empty list called 'fib' is then created to store the generated sequence. A 'while' loop is created that runs from 'a' and ends when the limit is reached.

The 'append' function then adds a number to the end of the sequence.  Each number is the sum of the two preceding ones. So, in the generator function, the variables a and b are used to keep track of the last two numbers in the sequence.

In each iteration of the loop, the next Fibonacci number is calculated by adding a and b, and store it in the variable fib_next. a is then updated to be b, and b to be fib_next, so that in the next iteration of the loop, a and b represent the last two numbers in the sequence.

The code:


def fibonacci (limit):

    a, b = 0, 1
    fib = []

    while a <= limit:
        fib.append(a)

        a, b = b, a + b 

    return fib
    
fibSequence = fibonacci(100)

print (fibSequence)