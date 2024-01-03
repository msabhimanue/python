from GRAPHICS import rectangle,circle,triangle,square
from GRAPHICS.THREEDGRAPHICS import cuboid,sphere
#using rectangle module
length=5
width=3
print("Area of a rectangle=",rectangle.area(length,width))
print("Perimeter of a rectangle=",rectangle.perimeter(length,width))
#using circle module
radius=4
print("Area of a circle=",circle.area(radius))
print("Perimeter of a circle=",circle.perimeter(radius))
#using cuboid module
length=2
width=3
height=4
print("Surface Area of a cuboid=",cuboid.surfacearea(length,width,height))
print("Volume of a cuboid=",cuboid.volume(length,width,height))
#using sphere module
radius=4
print("Surface Area of a sphere=",sphere.surfacearea(radius))
print("volume of a sphere=",sphere.volume(radius))
#using square module
a=5
print("Area of a square=",square.area(a))
print("Perimeter of a square=",square.perimeter(a))
#using triangle module
b=3
h=2
print("Area of a triangle=",triangle.area(b,h))
print("Perimeter of a triangle=",triangle.perimeter(b,h))

