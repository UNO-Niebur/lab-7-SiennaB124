#Problem4.py
#Project Euler problem 7

from NumberTests import isPrime, isEven


def findNthPrime(n):
  count = 0
  num = 1

  while count < n:
    num += 1
    if isPrime(num):
      count += 1

  return num
  
def main():
  result = findNthPrime(10001)
  print("The 10001st prime number is:", result)
 

if __name__ == '__main__':
  main()
