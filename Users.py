dict = {}
x = 0

print("klucz:\n"
      "1: Dodaj użytkownika\n"
      "2: Zobacz dane użytkownika\n"
      "3: Wyświetl imiona wszystkich użytkowników\n")
while (x == 0):
    x = input("Prosze wybrac opcje: ")
    if x == "1":

        name = input("podaj imie ")
        email = input("podaj email ")
        age = int(input("podaj wiek "))
        dict[name] = {"email": email, "age": age} # dla każdego "name" przypisuje własny słownik
        print(f"Użytkownik dodany! Witaj {name}!")
        #print(dict)
        x = 0
    elif x == "2":
        name = input("podaj imie użytkownika: ")
        print(dict[name])
        x = 0
    elif x == "3":
        print(dict.keys())
        x = 0


#print(dict)
