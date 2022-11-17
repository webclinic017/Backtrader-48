import pandas as pd

class Analyzer:
	def __init__(self, dataframe):
		self.dataframe = dataframe
  
	def log(self):
		print(self.dataframe)
     
if __name__ == '__main__':
	df = [1, 2, 3]
	df = pd.DataFrame(df)
	analyzer = Analyzer(df)

	analyzer.log()
 