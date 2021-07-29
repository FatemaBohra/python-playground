# Your task is to create a function
# that does four basic mathematical operations.

def basic_op(operator, value1, value2):
    switch={
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2,
    }
    return switch.get(operator,"Invalid input")


print(basic_op('+', 4, 7))
