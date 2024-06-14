import random
import itertools
num = "1234567890"
ahpa="abcdefghijklmnopqrustuvwxyz"
spcl="!@#$%^&*"
print(len(num))
var=int(input("size of password"))
nu= int(input("No of number needed"))
alp= int(input("No of alpabet"))
spcl1= int(input("No of spcl char"))
str1=""
new = random.sample(num,nu%len(num))
al = random.sample(ahpa,alp%len(ahpa))
spc = random.sample(spcl,spcl1%len(spcl))
new=new+al+spc
passwor=random.sample(new,len(new))
str1 =""
for i in passwor:
    str1 = str1+str(i)
print(str1)