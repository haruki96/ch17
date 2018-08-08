import re

###p211
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)
