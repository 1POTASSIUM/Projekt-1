def FizzBuzz():
    output = ""
    for i in range(1, 101):
        if i % 15 == 0:
            output += "FizzBuzz\n"
        elif i % 3 == 0:
            output += "Fizz\n"
        elif i % 5 == 0:
            output += "Buzz\n"
        else:
            output += str(i) + "\n"
    return output

print(FizzBuzz())
