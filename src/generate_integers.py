# Implement a function named generateRange(min, max, step),
# which takes three arguments and generates a range of integers from min to max,
# with the step. The first integer is the minimum value, the second is the maximum
# of the range and the third is the step. (min < max)

def generate_range(min, max, step):
    result = []
    current = min
    while (current <= max):
        result.append(current)
        current += step
    return result

print(generate_range(-10, 1, 1))