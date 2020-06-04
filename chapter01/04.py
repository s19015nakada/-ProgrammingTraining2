import re
A = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

B = re.split(", |\. |\.| ",A)
B.pop()
C={}

for x, y in enumerate(B):
    # print(x,y)
    if x==0 or 4<=x<=9 or x==14 or x==15 or x==18:
        C[y[0]]=x
    else:
        C[y[0:2]]=x


print(C)
