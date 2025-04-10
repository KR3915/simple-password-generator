import random
import string
upper = ""
lower = ""
numeral = ""
special = ""
from string import ascii_uppercase
#generate characters
def generate_chars(size, type):
    return "".join(random.choice(type) for i in range(size))
#generate at least 8 characters
while len(upper) + len(lower) + len(numeral) + len(special) < 8:
    upper = generate_chars(random.randint(1,3), string.ascii_uppercase)
    lower = generate_chars(random.randint(1,3), string.ascii_lowercase)
    numeral = generate_chars(random.randint(1,3), string.digits)
    special = generate_chars(1, "!@#$%^&*()_")
#combine letters
combination = upper + lower + numeral + special
print (combination)
#shuffle password
password = "".join(random.sample(combination,len(combination)))
print (password)
