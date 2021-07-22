def separate_digits(number):
    digits_str = str(number)
    result = []
    for i in digits_str:
        result.append(int(i))
    return result


print(separate_digits(234))
