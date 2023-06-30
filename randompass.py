import string
import random

len = int(input("Enter the Length of password:"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

str = lower+upper+digits+symbols

pwd = random.sample(str, len)
password = "".join(pwd)

print(password)
