numbers = [3, 7, 9, 12]

first, second, third, fourth = numbers

combined = first + second + third + fourth

def najmniejsza (list):
    min = 999
    for n in list:
        if n<min:
            min = n
    return min

print(combined)

print(najmniejsza(numbers))

numbers.sort(reverse=True)
print(numbers)