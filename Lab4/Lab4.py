import re


regex = "(a|b)(c|d)E+G?"
tokens = re.split("/", regex)
print(list(regex))