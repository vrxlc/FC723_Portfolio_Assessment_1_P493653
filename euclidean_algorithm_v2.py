class EuclideanAlgorithm:
    def calculate_gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass


# Requirement 2: Refactoring the code to use user input for GCD calculation
def main():
    print("Euclidean Algorithm - GCD Calculator")
    print("-" * 40)

    # Now fully relies on user input
    num1 = get_valid_input("Enter first positive integer: ")
    num2 = get_valid_input("Enter second positive integer: ")

    gcd_calculator = EuclideanAlgorithm()
    result = gcd_calculator.calculate_gcd(num1, num2)

    print(f"\nGCD of {num1} and {num2} = {result}")


if __name__ == "__main__":
    main()
