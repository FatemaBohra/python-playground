def sum_even_numbers(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return sum


print(sum_even_numbers([2, 4, 5, 4, 9, 10]))
