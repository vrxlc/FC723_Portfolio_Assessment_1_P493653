class ExtendedEuclideanAlgorithm:
    def extended_gcd(self, a, b):
        if b == 0:
            return (a, 1, 0)

        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1

        while r != 0:
            quotient = old_r // r

            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return (old_r, old_s, old_t)


# Adds user input & validation
def main():
    print("Extended Euclidean Algorithm")
    print("-" * 40)

    try:
        num1 = int(input("Enter first positive integer: "))
        num2 = int(input("Enter second positive integer: "))

        if num1 <= 0 or num2 <= 0:
            print("Error: Numbers must be positive")
            return

        calculator = ExtendedEuclideanAlgorithm()
        gcd, x, y = calculator.extended_gcd(num1, num2)

        print(f"\nGCD of {num1} and {num2} = {gcd}")
        print(f"Bézout coefficients: x = {x}, y = {y}")
        print(f"Verification: {num1}*({x}) + {num2}*({y}) = {gcd}")

    except ValueError:
        print("Error: Please enter valid integers")


if __name__ == "__main__":
    main()
