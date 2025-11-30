"""
FC723 Portfolio Assessment 1 base - Extended Euclidean Algorithm
Version 3: Extended version with Bézout coefficients
Student ID: P493653
Tutor: Sophie Norman

Description: 
This program implements the Extended Euclidean Algorithm to calculate:
1. The Greatest Common Divisor (GCD) of two positive integers
2. Bézout coefficients (x, y) such that a*x + b*y = gcd(a, b)
The program demonstrates encapsulation with a class and includes basic input validation.

"""

class ExtendedEuclideanAlgorithm:
    """
    A class to calculate GCD and Bézout coefficients using the Extended Euclidean Algorithm.
    """
    
    def extended_gcd(self, a, b):
        """
        Calculate GCD and Bézout coefficients.
        
        Parameters:
            a (int): First positive integer
            b (int): Second positive integer
        
        Returns:
            tuple: (gcd, x, y) where a*x + b*y = gcd
        """
        # Base case: if b is 0, gcd is a
        if b == 0:
            return (a, 1, 0)
        
        # Initialize variables
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        
        # Main algorithm loop
        while r != 0:
            quotient = old_r // r
            
            # Update remainders
            old_r, r = r, old_r - quotient * r
            
            # Update x coefficients
            old_s, s = s, old_s - quotient * s
            
            # Update y coefficients
            old_t, t = t, old_t - quotient * t
        
        # Return GCD and coefficients
        return (old_r, old_s, old_t)


# Main program
def main():
    """
    Runs the Extended Euclidean Algorithm program with user input.
    """
    print("Extended Euclidean Algorithm")
    print("-" * 40)
    
    try:
        # Gets user input
        num1 = int(input("Enter first positive integer: "))
        num2 = int(input("Enter second positive integer: "))
        
        # Checks for positive input
        if num1 <= 0 or num2 <= 0:
            print("Error: Numbers must be positive")
            return
        
        # Calculates GCD and Bézout coefficients
        calculator = ExtendedEuclideanAlgorithm()
        gcd, x, y = calculator.extended_gcd(num1, num2)
        
        # Display results
        print(f"\nGCD of {num1} and {num2} = {gcd}")
        print(f"Bézout coefficients: x = {x}, y = {y}")
        print(f"Verification: {num1}*({x}) + {num2}*({y}) = {gcd}")
        
    except ValueError:
        # Handle invalid input
        print("Error: Please enter valid integers")


# This line makes sure the code only runs when this file is executed directly
if __name__ == "__main__":
    main()
