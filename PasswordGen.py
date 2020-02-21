print ('Password generator')

import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789&@#?!*%'

number = input('Number of passwords? - ')
number = int(number)

length = input('Length of password/s? - ')
length = int(length)

for p in range (number):
    password = ''
    for c in range (length):
        password += random.choice(chars)
    print (password)

#Made by kostimiiil
