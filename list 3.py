list = [1,2,3,4,6]
first, *x = list
output = []
suma = 0

def add():
    for i in range(1, len(list) - 1):
        output[i] = list[i] + list[i-1]
    print(output)

add()