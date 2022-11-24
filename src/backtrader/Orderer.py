class Orderer:
	def __init__(self, asset, commission, leverage):
		self.asset = asset
		self.commission = commission
		self.leverage = leverage
  
		self.holding = 0
    
	def open_long_position(self, price, percentage):
		try:
			_amount = self.__get_actual_amount(price, percentage)
			if self.asset < price * _amount * (1 + self.commission):
				raise ValueError('No enough asset.')
			else:
				#print('Open long position.')
				self.__buy(price, _amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)
			return None, None

	def close_long_position(self, price, percentage):
		try:
			_amount = self.holding * percentage
			if self.holding < _amount:
				raise ValueError('No enough holding.')
			else:
				#print('Close long position.')
				self.__sell(price, _amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)
			return None, None

	def open_short_position(self, price, percentage):
		try:
			_amount = self.__get_actual_amount(price, percentage)
			if self.asset + self.holding*price*2 < price * _amount * (1 + self.commission):
				raise ValueError('No enough asset.')
			else:
				#print('Open short position.')
				self.__sell(price, _amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)
			return None, None

	def close_short_position(self, price, percentage):
		try:
			_amount = self.holding * percentage * -1
			if self.holding > _amount:
				raise ValueError('No enough holding.')
			else:
				#print('Close short position.')
				self.__buy(price, _amount)
				return self.asset, self.holding

		except ValueError as msg:
			print(msg)
			return None, None

	def log(self):
		print('asset:', self.asset)
		print('holding:', self.holding)
		print()

	def __buy(self, price, amount):  
		self.asset -= price * amount * (1 + self.commission)
		self.holding += amount	
  
	def __sell(self, price, amount):
		self.asset += price * amount * (1 - self.commission)
		self.holding -= amount
  
	def __get_actual_amount(self, price, percentage):
		return round((self.asset * percentage) / (price * (1 + self.commission * self.leverage)), 8)

if __name__ == '__main__':
    orderer = Orderer(100, 0.01, 2)
    
    print('test starting')
    
    orderer.open_long_position(5, 0.99)
    orderer.log()
    
    orderer.close_long_position(10, 1)
    orderer.log()
    
    orderer.open_short_position(10, 0.99)
    orderer.log()
    
    orderer.close_short_position(5, 1)
    orderer.log()