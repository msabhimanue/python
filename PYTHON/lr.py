a=inputa=input("enter a string : ")
c=len(a)
b=a[::-1]
d=a[0]
e=d+a[1:].replace(d,'$')
f=input("Enter another string : ")
g=input(a+f)
print("Length of the string is: ",c)
print("Reverse of the string is: ",b)
print("$ : ",e)
print("concatenate : ",g)
