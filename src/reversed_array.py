# Convert number to reversed array of digits.

def digitize(n):
    converted_string = str(n)
    reversed = converted_string[::-1]
    result = []
    for i in reversed:
        result.append(int(i))
    return result


print(digitize(35231))