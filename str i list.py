s = "banan je małpę"
# print tylko 3 znak

print(s[2])

# print od 3 do konca

print(s[2:])

# od 3 do 5

print(s[2:5])

# od 5 do poczatku wspak

print(s[4::-1])

#listy

letters = ["a", "b", "c"]

print(letters)

matrix = [[0,12], [6,36]]

print(matrix)

zeros = [0] * 5

combined = zeros + letters + matrix

print(combined)

numbers = list(range(5))

print(numbers)

print(numbers[::-1])

first, second, third, *other = numbers # osobne beda int, *other bedzie lista

print(third)

print(other)

for idx, letter in enumerate(s): #pozwala na dostep do indeksu znaku w liscie
    print(idx, letter)

