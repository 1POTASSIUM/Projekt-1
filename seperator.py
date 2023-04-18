tup = ('w', 'o', 'n', 's', 'z') # tuple to niezmienna lista
word = ''.join(tup) # między cudzysłowiem swadzamy znak który odziela znaki z tup w word
print(word) # . join = przyłącza tup do word

Dict = {"name": "Brunhilda", "country": "Zabrze"}

separator = ":::"

DictText = ""

DictText = separator.join(Dict.values())

print(DictText)

CarDict = {"car": "koń", "napęd": "nogi", "rok": "-10000"}

DefaultCar = CarDict.setdefault("napęd", "koła")
print(CarDict)