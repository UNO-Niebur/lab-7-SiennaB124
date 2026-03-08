#Problem3.py
#Project Euler problem 3

from NumberTests import isPrime
from NumberTests import getFactors

def main():
    number = 600851475143
    factors = getFactors(number)
    largestPrime = 0
    

    for f in factors:
        if isPrime(f):
            if f > largestPrime:
                largestPrime = f

    print("Largest prime factor:", largestPrime)


if __name__ == '__main__':
  main()
