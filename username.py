import string
import random

def generate_username():
    characters = string.ascii_letters + string.digits + '._-'
    username = ''.join(random.choice(characters) for _ in range(random.randint(5, 32)))
    return username

print(generate_username())
