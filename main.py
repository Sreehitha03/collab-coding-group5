from functions.factorial import factorial
from functions.prime import is_prime
from functions.armstrong import is_armstrong   

def main():
    print("Welcome to Collab Project - Math Utilities\n")

    print("Factorial of 5:", factorial(5))
    print("Is 7 prime?:", is_prime(7))
    print("Is 153 Armstrong?:", is_armstrong(153))   

if __name__ == "__main__":
    main()
