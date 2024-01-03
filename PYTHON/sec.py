a=input("Enter a line of text : ")
b=len(a)
print("The total number of characters in the given text is: ",b)
if b>=2:
	c=a[1]
	print("There is second character in the text.",c)
else:
	print("There is no second character in the text.")
