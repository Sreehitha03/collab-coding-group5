from functions.factorial import factorial
from functions.fibonacci import fibonacci
from functions.prime import is_prime
from functions.reverse_number import reverse_number
from functions.gcd import gcd
from functions.armstrong import is_armstrong   

def main():
    print("Welcome to Collab Project - Math Utilities\n")
    
    print("Factorial of 5:", factorial(5))
    
    print("Is 7 prime?:", is_prime(7))
    
    print("reverse of 140 is ?:", reverse_number(140))
    
    print("GCD of 10 and 15 is:", gcd(10,15))

if __name__ == "__main__":
    main()
