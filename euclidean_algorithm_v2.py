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
        
        Parameters:
            a (int): First positive integer
            b (int): Second positive integer
        
        Returns:
            int: The GCD of a and b
        """
        # Keeps looping until b becomes 0
        while b != 0:
            temp = b        # Store current b
            b = a % b       # Update b to remainder
            a = temp        # Update a to previous b
        
        return a
