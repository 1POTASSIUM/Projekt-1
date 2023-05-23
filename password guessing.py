import random
import string
import datetime
password_length = 3
password = ""
for i in range(0, password_length):
    letter = random.choice(string.ascii_letters)
    password += letter
print(password + "\n")

attempt = ""
while attempt != password:
    atnr = 0 #number of atempts
    #time = 0
    if attempt == password:
        print(f"Congratulations! You won nothing! And it only took {atnr} attempts!")
        break
    for a in string.ascii_letters:
        charA = random.choice(string.ascii_letters)
        for b in string.ascii_letters:
            charB = random.choice(string.ascii_letters)
            for c in string.ascii_letters:
                charC = random.choice(string.ascii_letters)
                attempt = charA + charB + charC
                atnr += 1

