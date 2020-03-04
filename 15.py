class a:
	def __init__(self):
		self._stu_name=""
		self._subject=""
		self._basic=0
		self._da=0
		self._hra=0
		self._salary=0
	def get_data(self):
		self._stu_name=input("enter name: ")
		self._subject=input("enter sub: ")
		self._basic=int(input("enter salary: "))
	def put_data(self):
		self._da=(5*self._basic)//100
		self._hra=(10*self._basic)//100
		self._salary=self._basic+self._da+self._hra
		print(self._salary)
c1=a()
c1.get_data()
c1.put_data()
