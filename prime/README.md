# Challenge-python

# Prime numbers

This code defines a function is_prime that takes a number n as input and checks whether it is prime or not. It then uses a for loop to generate a list of all prime numbers between 0 and 100 by checking each number in the range using the is_prime function. The list of prime numbers is stored in the variable primes and then printed to the console using the print() function.

The is_prime function uses the following logic to check if a number is prime:

If the number is less than 2, it is not prime.
If the number is 2, it is the only even prime number and is therefore prime.
If the number is even, it is not prime.
If the number is odd, we only need to check for factors up to the square root of the number, since any factors larger than the square root must have a corresponding factor smaller than the square root that has already been checked. There is only need to check odd numbers as well, since if a number has a factor other than 1 and itself, then it must have at least one factor less than or equal to the square root of the number that we have already checked

The code: 

def primeNumbers (n):
    if n < 2:
        return False
    
    elif n == 2:
        return True
    
    elif n % 2 == 0:
        return False
    
    else:
        for i in range (3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
            
        return True

primes = []

for n in range(0, 101):
    if primeNumbers(n):
        primes.append(n)

print(primes)