import random
from collections import deque
from array import array
col = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']
queue = deque([]) # deque pozwala na większą manipulacją listą
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
first = queue.popleft()
print(first)
print(list(queue))
x = "dupa"
def colour(x):
    return random.choice(col) + f"{x}" # generuje losowy kolor i pisze wszystko w tym kolorze
print(colour(x))

arr = array("i", [1,1,2,3,4]) # array chce wartości okeślonego typu, i = signed intiger
unique = set(arr) # set zwraca unikatowe wartości listy (usuwa duplikaty)
print(unique) # set jest typem zmiennej, listą nieposortowanych unikalych wartości



