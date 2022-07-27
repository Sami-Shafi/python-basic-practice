# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# native modules
from datetime import date
from time import time

# pip
from camelcase import CamelCase

# print(date.today())
# print(time())

c = CamelCase()
print(c.hump("hello there!"))