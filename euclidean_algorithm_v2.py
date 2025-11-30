"""
FC723 Portfolio Assessment 1  - Euclidean Algorithm Implementation
Version 2: Interactive version with user input and validation
Student ID: P493653
Tutor: Sophie Norman

Description: 
This program calculates the Greatest Common Divisor (GCD) of two positive integers
using the Euclidean Algorithm. The program now accepts user input and validates 
it to ensure the numbers are positive integers. Encapsulation is demonstrated 
by using a class for the GCD calculation.

"""

class EuclideanAlgorithm:
    """
    A class to calculate the GCD using the Euclidean Algorithm.
    """
    
    def calculate_gcd(self, a, b):
        """
        Calculate the GCD of two positive integers.
        """
        # Repeats until remainder becomes 0
        while b != 0:
            temp = b        # Stores current value of b
            b = a % b       # Computes remainder
            a = temp        # Updates a to previous b
        
        return a


def get_valid_input(prompt):
    """
    Prompt the user to enter a positive integer.
    Continues asking until valid input is given.
    """
    while True:
        try:
            value = int(input(prompt))  # Attempts conversion to integer
            
            if value > 0:               # Checks for positive number
                return value
            else:
                print("Error: Please enter a positive number (greater than 0).")
        
        except ValueError:
            print("Error: Please enter a valid integer.")  # Non-integer error


def main():
    """
    Runs the interactive GCD calculator.
    """
    print("Euclidean Algorithm - GCD Calculator")
    print("-" * 40)
    
    # This prompts user for two valid positive integers
    num1 = get_valid_input("Enter first positive integer: ")
    num2 = get_valid_input("Enter second positive integer: ")
    
    # Instantiate class and compute GCD
    gcd_calculator = EuclideanAlgorithm()
    result = gcd_calculator.calculate_gcd(num1, num2)
    
    # Display result
    print(f"\nGCD of {num1} and {num2} = {result}")


# Ensures program only runs when executed directly
if __name__ == "__main__":
    main()
