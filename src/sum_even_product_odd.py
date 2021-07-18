def sum_even_product_odd(numbers):
    sum = 0
    product = 1
    for i in numbers:
        if i % 2 == 0:
            sum += i
        else:
            product *= i

    return sum, product


print(sum_even_product_odd([2, 4, 3, 6, 8, 7, 5]))
