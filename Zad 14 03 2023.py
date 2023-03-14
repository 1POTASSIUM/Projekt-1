print("A oto liczy parzyste od 1 do 20:")
ile = 0
for x in range (1, 21):
    if x % 2 == 0:
        ile+=1
        print(x)

print(f"jest {ile} liczb parzystych w tym zakresie")# f przed "" pozwala na uzycie innych typow zmiennych

#funkcja drukujaca tekst:

def greet(name):
    return f"Hi {name}"
print("twoje imie:")
name = input()
print(greet(name))

#function with unlimited input data

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1,2,3,4))