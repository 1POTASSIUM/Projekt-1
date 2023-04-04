#ile razy zmienia znak
with open("Dane.txt", 'r') as file:
    output = file.readline() # readline oznacza zkondensowanie stringu do jednej lini, readlines wypisuje linie po lini
def ile_razy_zmiana():
    ile = 0
    for i in range(len(output) - 1):
        if output[i-1] != output[i]:
            ile + 1
    return ile
#print(output)
print(ile_razy_zmiana())