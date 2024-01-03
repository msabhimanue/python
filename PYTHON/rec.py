class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return (self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
print("first rectangle")
length=int(input("Enter the length : "))
breadth=int(input("Enter the breadth : "))
rectangle1=Rectangle(length,breadth)
b=rectangle1.area()
print("Area of rectangle1 is : ",b)
print("Perimeter of rectangle1 is : ",rectangle1.perimeter())

class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return (self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
print("second rectangle")
length=int(input("Enter the length "))
breadth=int(input("Enter the breadth "))
rectangle2=Rectangle(length,breadth)
a=rectangle2.area()
print("area of rectangle2",a)
print("Perimeter of rectangle2",rectangle2.perimeter())
if(b==a):
       print("same")
else:
       print("different")
