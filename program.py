import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Podaj długość hasła:"))

password = ""

for i in range(length):
    password += random.choice(elements)

print(password)
