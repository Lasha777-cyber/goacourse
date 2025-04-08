def filter_positive(numbers):
    negative_numbers = []

    for number in numbers:
        if number > 0:
            negative_numbers.append(number)
    
    return negative_numbers

filter_positive([1,6,3,-5,-8,-10,7,-3])