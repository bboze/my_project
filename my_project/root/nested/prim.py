import math

    
class PrimNum:
    
   empCount = 0

   def __init__(self, name, salary):
      pass

   def is_prime(self, number):
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0: 
                    return False
                return True
            return False    

    
   def get_primes(self, number):
    while True:
        if PrimNum.is_prime(self, number):
            number = yield number
        number += 1

        
   def print_successive_primes(self, iterations, base=10):
    prime_generator = PrimNum.get_primes(self, base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))  
