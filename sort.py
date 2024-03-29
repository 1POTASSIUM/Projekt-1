items = [("Product 1", 123,), #to jest lista (zbor wartosci)
         ("Product 2", 12),
         ("Product 3", 34507)]

items.sort(key=lambda item:item[1]) # lambda oznacza ze bedziemy iterowac, return item o indeksie 1 (tworzy nowa liste, która zawiera rzeczy z listy macierzystej o indeksie 1 (cena))
print(items)

students = [{"imie": "Karolina", "wiek": 23}, # to jest slownik (klucz i wartosc)
            {"imie": "Jan", "wiek": 27},
            {"imie": "Brunhilda", "wiek": 2378}]

students.sort(key=lambda student:student["wiek"], reverse=True)

print(students[0])

# map - zmiana elementu

x = list(map(lambda ))#map zwraca obiekt: przyjmuje liste i to jak zmienić każdą zmienną

def myfunc(a, b):
  return a * b

y = map(myfunc, (1, 2, 3), (2, 4, 8))

print(y)

#convert the map into a list, for readability:
print(list(y))
