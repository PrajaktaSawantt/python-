# declaring the class circle
class Circle():
def __init__(self, r):
self.radius = r
# area() for calculating the area of circle
def area(self):
return self.radius**2*3.14
# perimeter() for calculating the perimeter of circle
def perimeter(self):
return 2*self.radius*3.14
NewCircle = Circle(8)
print("Area of the circle : ", end =" ")
print(NewCircle.area())
print("Perimeter of the circle : ", end =" ")
print(NewCircle.perimeter())
