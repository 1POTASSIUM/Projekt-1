import random
import time
col = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']

def colour(x):
    return random.choice(col) + f"{x}" # generuje losowy kolor i pisze x

def count(x):
    time.sleep(1)
    if x == 1:
        print(colour(x))
    else:
        print(colour(x))
        if x>1:
            count(x-1)
x = int(input("podaj liczbę "))
colour(x)
print(count(x))

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

print(list(zip(names, ages))) # zip takes iterable containers and returns a single iterator object, having mapped values from all the containers.