# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# native modules
from datetime import date
from time import time

# pip
from camelcase import CamelCase
# custom modules
from validator import validate_email

# print(date.today())
# print(time())

# c = CamelCase()
# print(c.hump("hello there!"))

# validate emails
email = "sami123@gmail.com";

if validate_email(email):
    print("Email is valid.")
else:
    print("Email is invalid.")

