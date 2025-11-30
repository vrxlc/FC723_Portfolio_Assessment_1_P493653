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
            value = int(input(prompt))  # convert input to integer

            if value > 0:  # validate input
                return value
            else:
                print("Error: Please enter a positive number (greater than 0).")

        except ValueError:
            print("Error: Please enter a valid integer.")


# Requirement 3: validation messages added
def main():
    print("Euclidean Algorithm - GCD Calculator")
    print("-" * 40)

    num1 = get_valid_input("Enter first positive integer: ")
    num2 = get_valid_input("Enter second positive integer: ")

    gcd_calculator = EuclideanAlgorithm()
    result = gcd_calculator.calculate_gcd(num1, num2)

    print(f"\nGCD of {num1} and {num2} = {result}")


if __name__ == "__main__":
    main()
