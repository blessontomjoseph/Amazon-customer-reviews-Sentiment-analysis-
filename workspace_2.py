import numpy as np
word='WHAT is THIS'
a=word.split( )
print(a)
for i in a:
    if i.isupper()==True:
        print(i)