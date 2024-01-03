str=input("Enter a string: ")
b = ""
for i in str:
    b = i + b
 
if (str == b):
    print("Entered string is palindrome")
else:
    print("Entered string is Not palindrome")
