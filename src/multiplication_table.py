# Your goal is to return multiplication table for
# number that is always an integer from 1 to 10.

def multi_table(number):
    result = ''
    for i in range(1, 10):
        result += (str(i) + ' * ' + str(number) +
                   " = " + str(i * number) + "\n")
    return result + (str(10) + ' * ' + str(number) +
                     " = " + str(10 * number))

print(multi_table(5))