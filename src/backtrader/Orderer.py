class Orderer:
	def __init__(self, asset, commission):
		self.asset = asset
		self.commission = commission

		self.holding = 0
    
	def open_long_position(self, price, amount):
		try:
			if self.asset < price * amount * (1 + self.commission):
				raise ValueError('No enough asset.')
			else:
				print('Open long position.')
				self.__buy(price, amount)
				return self.asset, self.holding

		except ValueError as msg:
		  print(msg)

	def close_long_position(self, price, amount):
		try:
			if self.holding < amount:
				raise ValueError('No enough holding.')
			else:
				print('Close long position.')
				self.__sell(price, amount)
				return self.asset, self.holding

		except ValueError as msg:
		  print(msg)

	def open_short_position(self, price, amount):
		try:
			if self.asset + self.holding*price*2 < price * amount * (1 + self.commission):
				raise ValueError('No enough asset.')
			else:
				print('Open short position.')
				self.__sell(price, amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)

	def close_short_position(self, price, amount):
		try:
			if self.holding > -amount:
				raise ValueError('No enough holding.')
			else:
				print('Close short position.')
				self.__buy(price, amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)
  
	def __buy(self, price, amount):
		self.asset -= price * amount * (1 + self.commission)
		self.holding += amount	
  
	def __sell(self, price, amount):
		self.asset += price * amount * (1 - self.commission)
		self.holding -= amount
  
	def log_detail(self, price):
		print('holding:', self.holding)
		print('asset:', self.asset)
		print('weight asset:', self.asset + self.holding*price*2)
  
if __name__ == '__main__':
	orderer = Orderer(100, 0.00001)

	orderer.open_short_position(10, 9)
	orderer.open_short_position(10, 8)
 
	orderer.close_short_position(10, 9)
	orderer.close_short_position(10, 8)