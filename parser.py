import re


def parse_polynomial(equation):
    """Parse polynomial equation and return coefficients dictionary"""

    left, right = equation.split('=')

    left_coeffs = parse_side(left)
    right_coeffs = parse_side(right)

    coefficients = {}

    for power, coeff in left_coeffs.items():
        coefficients[power] = coefficients.get(power, 0) + coeff

    for power, coeff in right_coeffs.items():
        coefficients[power] = coefficients.get(power, 0) - coeff

    return coefficients


def parse_side(side_str):
    """Parse one side of equation and return coefficients dictionary"""
    coefficients = {}

    side_str = side_str.replace(' ', '')

    pattern = r'([+-]?)(\d*\.?\d*)\*X\^(\d+)'
    matches = re.findall(pattern, side_str)

    if side_str and side_str[0] not in ['+', '-']:
        side_str = '+' + side_str

    matches = re.findall(pattern, side_str)

    for sign, coeff_str, power_str in matches:

        if coeff_str == '':
            coeff = 1.0
        else:
            coeff = float(coeff_str)

        if sign == '-':
            coeff = -coeff
        elif sign == '' and coeff > 0:
            pass

        power = int(power_str)

        if power in coefficients:
            coefficients[power] += coeff
        else:
            coefficients[power] = coeff

    return coefficients


def format_coefficient(coeff):
    """Format coefficient to match expected output"""
    if coeff == int(coeff):
        return str(int(coeff))
    else:
        return str(coeff)


def format_polynomial(coefficients):
    """Format coefficients dictionary back to polynomial string"""
    if not coefficients:
        return "0 * X^0"

    max_power = max(coefficients.keys())

    terms = []
    for power in range(max_power + 1):
        coeff = coefficients.get(power, 0)
        coeff_str = format_coefficient(coeff)

        if power == 0:
            if coeff >= 0:
                terms.append(f"{coeff_str} * X^{power}")
            else:
                terms.append(f"{coeff_str} * X^{power}")
        else:
            if coeff > 0:
                terms.append(f" + {coeff_str} * X^{power}")
            elif coeff < 0:
                terms.append(f" - {format_coefficient(abs(coeff))} * X^{power}")
            else:
                terms.append(f" + 0 * X^{power}")

    result = ''.join(terms)

    if result.startswith(' + '):
        result = result[3:]

    return result + " = 0"


def get_coefficients_array(coefficients):
    """Convert coefficients dictionary to array format expected by solver"""
    if not coefficients:
        return ["0"]

    max_power = max(coefficients.keys())
    result = []

    for power in range(max_power + 1):
        coeff = coefficients.get(power, 0)
        result.append(str(coeff))

    return result


def get_polynomial_degree(coefficients):
    """Get the degree of the polynomial"""
    if not coefficients:
        return 0

    max_degree = 0
    for power, coeff in coefficients.items():
        if coeff != 0:
            max_degree = max(max_degree, power)

    return max_degree
