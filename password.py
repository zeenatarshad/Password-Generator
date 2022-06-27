import random
import string

letters = string.ascii_letters
nums = '0123456789'
spe = '-+*%&$!_'

symbols = letters+ nums+ spe
len = int(input("Enter Password length:"))

password = ''.join(random.sample(symbols,len))
print(password)