"""
->94 characters#
->52 alphabets
->0-25 lowercase
->26 - 51 uppercase
->52 - 61 digits
->62 - 93 punctuations
-> append to a random position
"""
import string as sr
import random as ra

x = sr.ascii_letters
a = sr.digits
c = sr.punctuation
password = ""
characters = 8
while characters > 0:
    d = x + a + c
    e = ra.randint(1, 94)
    password += d[e]
    characters -= 1
print(password)

