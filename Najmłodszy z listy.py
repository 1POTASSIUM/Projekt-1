# - function to find youngest student from a set
students = [
    {"imie": "Tomek", "wiek": 20}, # to jest 0
    {"imie": "Karolina", "wiek": 18} # to jest 1
]
students.sort(key=lambda item:item["wiek"]) # jeśli chcę sortować po wieku, podaje dokładny parametr, bo 0, 1, ... oznacza słowniki w liście
print(students[0])



