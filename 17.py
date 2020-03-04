class employee:
	def __init__(self):
		self.ename=""
		self.esalary=0
		self.eage=0
	def get_data(self):
		self.ename=input("enter name: ")
		self.esalary=int(input("enter salary: "))
		self.eage=int(input("enter age: "))
	def put_data(self):
		print(self.ename)
		print(self.esalary)
		print(self.eage)
c1=employee()
print("employee 1")
c1.get_data()
c1.put_data()
print("employee 2")
c1.get_data()
c1.put_data()
print("employee 3")
c1.get_data()
c1.put_data()
