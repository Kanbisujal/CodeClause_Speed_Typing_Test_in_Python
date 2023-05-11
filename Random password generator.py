import random
import string

# define the length of the password
length = 10

# define the character set to generate the password from
characters = string.ascii_letters + string.digits + string.punctuation

# generate the password
password = ''.join(random.choice(characters) for i in range(length))

# print the password
print("Your randomly generated password is:", password)