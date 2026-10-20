import random
import string
def generate_password(length):
    password=""
   
    characters = string.ascii_letters + string.digits
    for _ in range(length):
     cha=random.choice(characters)
     password+= cha
    print("Your generated password is:", password)

us = int(input("Enter password length: "))
generate_password(us)