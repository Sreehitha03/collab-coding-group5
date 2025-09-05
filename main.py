from functions.factorial import factorial
from functions.fibonacci import fibonacci
from functions.prime import is_prime

def main():
    print("Welcome to Collab Project - Math Utilities\n")

    print("Factorial of 5:", factorial(5))
    print("Is 7 prime?:", is_prime(7))
    print("5th number in fibonacci series is :",fibonacci(5))

if __name__ == "__main__":
    main()
