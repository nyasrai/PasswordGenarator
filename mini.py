import random
import itertools


name=input("what is your name")
print(name)
print("hello  "+name+"!!!,welcome to the password generator")

x=int(input("how many numbers you want in your password: "))
num=[i for i in range (10)]
a=random.sample(num,x)
y=int(input("how many letters you want in your password: "))
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=random.sample(alp,y)
z=int(input("how many symbols you want in your password: "))
symb="!@#$%^&*"
c=random.sample(symb,z)
print("this is your password as per your requirement: ")
var=list(itertools.chain(a,b,c))
final=random.sample(var,len(var))
for i in range(len(final)):
    print(final[i],end="")
