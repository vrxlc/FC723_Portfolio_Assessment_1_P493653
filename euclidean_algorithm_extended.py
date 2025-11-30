class ExtendedEuclideanAlgorithm:
    def extended_gcd(self, a, b):
        # If b is zero, return gcd and coefficients
        if b == 0:
            return (a, 1, 0)

        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1

        # Algorithm loop
        while r != 0:
            quotient = old_r // r

            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return (old_r, old_s, old_t)


# Minimal driver to test functionality (not yet validated)
def main():
    calculator = ExtendedEuclideanAlgorithm()
    gcd, x, y = calculator.extended_gcd(30, 12)
    print(gcd, x, y)

if __name__ == "__main__":
    main()
