class Investment:
	def __init__(self,balance):
		self.balance=balance

	def one(self,month=1):
		for i in range(1,month+1):
			shoushu=self.balance//3000*0.01
			profit=shoushu*20000
			self.balance+=profit
		return self.balance

	
	

my_investment=Investment(20000)
print(my_investment.one(6))

