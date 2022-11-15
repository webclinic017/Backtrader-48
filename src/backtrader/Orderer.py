class Orderer:
	def buy(self):
		print('Buy')
  
	def sell(self):
		print('Sell')
     
if __name__ == '__main__':
	orderer = Orderer()
 
	orderer.buy()
	orderer.sell()