def findchar(s, c):
    i = 0
    for i in s:
        if i == c:
            return True
    return False


def getSideDigits(s):
    equal_pos = s.find('=')
    digits = []
    digitsAfterEqual = {}

    left_side = s[:equal_pos]
    right_side = s[equal_pos + 1:]

    i = 0
    while i < len(left_side):
        if left_side[i].isspace():
            i += 1
            continue
        if i >= 2 and left_side[i-2:i] == 'X^':
            i += 1
            continue
        if left_side[i].isdigit() or left_side[i] in '-':
            num = ''
            if left_side[i] in '-':
                num = left_side[i]
                i += 1
            while i < len(left_side) and left_side[i].isspace():
                i += 1
            while i < len(left_side) and left_side[i].isdigit():
                num += left_side[i]
                i += 1
            if i < len(left_side) and left_side[i] == '.':
                num += '.'
                i += 1
                while i < len(left_side) and left_side[i].isdigit():
                    num += left_side[i]
                    i += 1
            if num and num != '+' and num != '-':
                digits.append(num)
        i += 1

    i = 0
    count = 0
    while i < len(right_side):
        if right_side[i].isspace():
            i += 1
            continue
        if i >= 2 and right_side[i-2:i] == 'X^':
            i += 1
            continue
        if right_side[i].isdigit() or right_side[i] in '-':
            num = ''
            if right_side[i] in '-':
                num = right_side[i]
                i += 1
            while i < len(right_side) and right_side[i].isspace():
                i += 1
            while i < len(right_side) and right_side[i].isdigit():
                num += right_side[i]
                i += 1
            if i < len(right_side) and right_side[i] == '.':
                num += '.'
                i += 1
                while i < len(right_side) and right_side[i].isdigit():
                    num += right_side[i]
                    i += 1
            if num and num != '+' and num != '-':
                digitsAfterEqual[count] = num
                count += 1
        i += 1

    return digits, digitsAfterEqual


def calculateType(x, x1):
    if x.find('.') != -1 and x1.find('.') != -1:
        return round(float(x) - float(x1), 1)
    elif x.find('.') != -1:
        return round(float(x) - int(x1), 1)
    elif x1.find('.') != -1:
        return round(int(x) - float(x1), 1)
    else:
        return int(x) - int(x1)


def reduceFunct(s):
    sideDigits = getSideDigits(s)
    left_side = sideDigits[0]
    right_side = sideDigits[1]

    reduced_form = {}

    for i, coef in enumerate(left_side):
        reduced_form[i] = coef

    for power, coef in right_side.items():
        if power in reduced_form:
            reduced_form[power] = str(calculateType(reduced_form[power], coef))
        else:
            reduced_form[power] = str(calculateType("0", coef))

    max_power = max(reduced_form.keys())
    result = []

    for i in range(max_power + 1):
        if i in reduced_form:
            result.append(reduced_form[i])
        else:
            result.append("0")

    return result


def changeSign(s):
    if '.' in s:
        return float(s) * -1
    else:
        return int(s) * -1


def printReduced(reducedf):
    sign = {}
    s = ""
    i = 0
    while i < len(reducedf):
        if str(reducedf[i]).startswith('-'):
            sign[i] = "-"
            reducedf[i] = str(abs(float(reducedf[i])))
        else:
            sign[i] = "+"

        if i == 0:
            s += f"{reducedf[i]} * X^{i}"
        else:
            s += f" {sign[i]} {reducedf[i]} * X^{i}"
        i += 1

    s += " = 0"
    print("Reduced form:", s)
    return i - 1
