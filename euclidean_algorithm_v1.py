"""
FC723 Portfolio Assessment 1  - Euclidean Algorithm Implementation
Version 1: Basic implementation with encapsulation
Student ID: P493653
Module: Programming Theory (FC723)
Tutor: Sophie Norman

Description: 
This program implements the Euclidean Algorithm to calculate the Greatest Common 
Divisor (GCD) of two positive integers. It demonstrates basic encapsulation by 
using a class to make the code reusable. The program tests the algorithm with 
a few sample numbers.

"""

class EuclideanAlgorithm:
    """
    A class to calculate the GCD using the Euclidean Algorithm.
    Encapsulation is demonstrated by placing the calculation inside the class.
    """
    
    def calculate_gcd(self, a, b):
        """
        Calculate the GCD of two positive integers using the Euclidean Algorithm.
        
        How it works:
        - Keep dividing the larger number by the smaller number
        - Replace the larger with the remainder
        - Continue until remainder is 0
        - The last non-zero number is the GCD
        
        Parameters:
            a (int): First positive integer
            b (int): Second positive integer
        
        Returns:
            int: The GCD of a and b
            
        """
        # Keep looping until b becomes 0
        while b != 0:
            # Store the current value of b
            temp = b
            # Update b to be the remainder of a divided by b
            b = a % b
            # Update a to the old value of b
            a = temp
        
        # When b is 0, a contains the GCD
        return a


# Main program
def main():
    """
    Runs test cases to demonstrate the Euclidean Algorithm.
    """
    # Create an instance of the EuclideanAlgorithm class
    gcd_calculator = EuclideanAlgorithm()
    
    # Print program header
    print("Euclidean Algorithm - GCD Calculator")
    print("-" * 40)
    
    # Test case 1: numbers with a common factor
    num1 = 48
    num2 = 18
    result = gcd_calculator.calculate_gcd(num1, num2)
    print(f"GCD of {num1} and {num2} = {result}")
    
    # Test case 2: one number divides the other
    num1 = 100
    num2 = 25
    result = gcd_calculator.calculate_gcd(num1, num2)
    print(f"GCD of {num1} and {num2} = {result}")
    
    
# This line makes sure the code only runs when this file is executed directly
if __name__ == "__main__":
    main()