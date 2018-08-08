import re

line = "Arizona 479, 501, 870. California 209, 213, 650."
match = re.findall("\d", line, re.IGNORECASE)
print(match)

###
test = "the ghost that says boo haunts the loo"
m = re.findall("[bl]oo", test, re.IGNORECASE)
print(m)