a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
d=int(input("Enter the fourth number : "))
smallest=a
if b<smallest:
	smallest=b
if c<smallest:
	smallest=c
if d<smallest:
	smallest=d
	
print("The smallest number is : ",smallest)
