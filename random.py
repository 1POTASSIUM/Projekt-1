import random

for i in range(5):
    print(random.random()) # podaj losową liczbę od 0 do 1

print("\n")

for i in range(5):
    print(random.randrange(0,20)) # podaj losową liczbę od a do b

print("\n")

for i in range(5):
    print(random.randint(0,20)) # podaj losową liczbę od a do b włącznie

print("\n")

ss = 0
licznik = 0
while ss != 77:
    ss = random.randrange(0,101)
    licznik += 1

print(licznik)

print("\n")

liczba = random.randrange(0,7)
zgad = 0
licznik_zgad = 1
while zgad != liczba:
    zgad = int(input("ile? "))
    if zgad != liczba:
        print("nie, ty kokoszambonello")
        licznik_zgad += 1
    else:
        print(f"gratulacje! wygrałeś nic! i to za {licznik_zgad} razem!")

uczniowie = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numerek = 0
dalej = "t"
ile_pod_rzad = 1
ostatni = 0
while dalej == "t":
    numerek = random.choice(uczniowie)
    print(numerek)
    #uczniowie.remove(numerek)
    if ostatni != numerek:
        ostatni = numerek
    else:
        ile_pod_rzad += 1
    dalej = input("continue? t/n")

print(f"jednego ucznia wylosowano {ile_pod_rzad} razy pod rząd")