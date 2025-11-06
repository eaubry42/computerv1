import sys
from parser import (parse_polynomial, format_polynomial,
                    get_coefficients_array, get_polynomial_degree)

# Δ=b2−4ac
# x1=−b−√Δ−−2a
#  et x2=−b+√Δ−−2a


def calculateDelta(a, b, c):
    return round((float(b) * float(b)) - (4 * float(a) * float(c)), 6)


def sqrt(x):
    return x**0.5


def solve_degree_0(reducedf):
    """Solve degree 0 polynomial: c = 0"""
    c = float(reducedf[0])
    if c == 0:
        print("Any real number is a solution.")
    else:
        print("No solution.")


def solve_degree_1(reducedf):
    """Solve degree 1 polynomial: bx + c = 0"""
    b = float(reducedf[1])
    c = float(reducedf[0])

    if b == 0:
        if c == 0:
            print("Any real number is a solution.")
        else:
            print("No solution.")
    else:
        x = -c / b
        print("The solution is:")
        print(f"{x}")


def solve_degree_2(reducedf):
    """Solve degree 2 polynomial using quadratic formula"""
    a = float(reducedf[2])  # X^2 coefficient
    b = float(reducedf[1]) if len(reducedf) > 1 else 0  # X^1 coefficient
    c = float(reducedf[0])  # X^0 coefficient

    delta = calculateDelta(a, b, c)

    if delta > 0:
        x1 = round(((-1 * b) - sqrt(delta)) / (2 * a), 6)
        x2 = round(((-1 * b) + sqrt(delta)) / (2 * a), 6)
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"{x1}")
        print(f"{x2}")
    elif delta == 0:
        x = round((-b) / (2 * a), 6)
        print("Discriminant is zero, the solution is:")
        print(f"{x}")
    else:
        real_part = (-b) / (2 * a)
        imag_part = sqrt(abs(delta)) / (2 * a)

        from fractions import Fraction
        real_frac = Fraction(real_part).limit_denominator(100)
        imag_frac = Fraction(imag_part).limit_denominator(100)

        print("Discriminant is strictly negative, " +
              "the two complex solutions are:")

        if real_frac.denominator == 1:
            if real_frac.numerator == 0:
                real_str = ""
            else:
                real_str = str(real_frac.numerator)
        else:
            real_str = f"{real_frac.numerator}/{real_frac.denominator}"

        if imag_frac.denominator == 1:
            imag_str = f"{imag_frac.numerator}i"
        else:
            imag_str = f"{imag_frac.numerator}i/{imag_frac.denominator}"

        if real_frac.numerator == 0:
            print(f"{imag_str}")
            print(f"-{imag_str}")
        else:
            print(f"{real_str} + {imag_str}")
            print(f"{real_str} - {imag_str}")


def main(argv):
    # Get equation from command line argument or STDIN
    if len(argv) == 2:
        equation = argv[1]
    elif len(argv) == 1:
        # No argument provided, read from STDIN
        try:
            equation = input().strip()
            if not equation:
                print("Error: Empty equation provided")
                return 1
        except EOFError:
            print("Error: No input provided")
            return 1
        except KeyboardInterrupt:
            print("\nProgram interrupted")
            return 1
    else:
        print("Usage: python main.py [equation]")
        print("If no equation is provided, it will be read from STDIN")
        return 1
    coefficients = parse_polynomial(equation)
    reduced_form = format_polynomial(coefficients)
    print(f"Reduced form: {reduced_form}")
    degree = get_polynomial_degree(coefficients)
    coeff_array = get_coefficients_array(coefficients)
    if degree > 0:
        print(f"Polynomial degree: {degree}")
    if degree == 0:
        solve_degree_0(coeff_array)
    elif degree == 1:
        solve_degree_1(coeff_array)
    elif degree == 2:
        solve_degree_2(coeff_array)
    elif degree > 2:
        print("The polynomial degree is strictly greater than 2, " +
              "I can't solve.")


if __name__ == "__main__":
    main(sys.argv)
