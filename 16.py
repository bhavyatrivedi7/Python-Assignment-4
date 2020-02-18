class shape:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def area(self):
		print(x*y)
	def perimeter(self):
		print((2*x)+(2*y))
x=int(input("enter x: "))
y=int(input("enter y: "))
c1=shape(x,y)
print("area is: ",end=" ")
c1.area()
print("perimeter is: ",end=" ")
c1.perimeter()
