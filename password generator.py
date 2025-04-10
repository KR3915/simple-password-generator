import random
import string

from string import ascii_uppercase
def generate_chars(size, type):
    return "".join(random.choice(type) for i in range(size))
upper = generate_chars(random.randint(1,3), string.ascii_uppercase)
lower = generate_chars(random.randint(1,3), string.ascii_lowercase)
numeral = generate_chars(random.randint(1,3), string.digits)
special = generate_chars(1, "!@#$%^&*()_")

print(upper, lower, numeral, special)
    