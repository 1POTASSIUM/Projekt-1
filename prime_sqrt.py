import math
dane=[]
with open("liczby.txt","r") as plik:
    for i in plik:
        dane.append(int(i.strip()))
def is_natural(n):
    x = int(n)
    if (x == n):
        return True
    else:
        return False

def is_prime(n):
  if (n > 2):
      for i in range(2, n):
          if (n % i) == 0:
              return False
      return True
  elif (n == 2):
      return True
  else:
      return False

output = ""

for i in dane:
    n = math.sqrt(i)
    if (is_natural(n)):
        if (is_prime(int(n))):
            output += str(i) + "\n"

print(output)
