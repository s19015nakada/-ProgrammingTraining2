import re
A="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

B = re.split(", |\.| ",A)
B.pop()
C=[]
for x in B:
    C.append(len(x))
print(C)
