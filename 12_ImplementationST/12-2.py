import re

data = input()

p1 = "[A-Z]"
p2 = "\d"

alphabet = re.findall(p1, data)
integer = re.findall(p2, data)
integer = list(map(int, integer))

alphabet.sort()
alphabet.append(str(sum(integer)))
result = "".join(alphabet)

print(result)