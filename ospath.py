import os.path
filename='getmail.py'
#print(os.path.abspath(filename))
bc=os.path.abspath(filename)
b=os.path.dirname(bc)
c=len(filename)
d = b[:-c]
print(b)