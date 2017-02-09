#!/usr/bin/env python
# @Author: @amarlearning
# @Date:   2017-02-08
# @Email:  amar.om1994@gmail.com


class ImportData:

	""" This is to import data form the cvs file. """

	def __init__(self, Name):

		self.__name = Name

	def getDataInList(self):

		""" Public method to import data form the cvs file. """

		with open(self.__name, 'r') as data:

			self.__data = []
			for line in data:
				words = line.rstrip().split(',')
				self.__data.append(words)

		return self.__data


class CoreLogic:

	""" This is to find the status and remaining quantity of all the orders. """

	def __init__(self, result):

		self.__data = result
		self.__CI = self.__data[0].index("Company")
		self.__Side = self.__data[0].index("Side")
		self.__quantity = self.__data[0].index("Quantity")
		self.__old = len(self.__data[0])


	def __updateQuantity(self, DataOne, DataTwo):

		""" Private method to update quantity based on stock exchange orders. """

		DataOne = int(DataOne)
		DataTwo = int(DataTwo)

		if DataOne == DataTwo:
			DataOne = DataTwo = 0

		elif DataOne > DataTwo:
			DataOne = DataOne - DataTwo
			DataTwo = 0

		else:
			DataTwo = DataTwo - DataOne
			DataOne = 0

		return str(DataOne) , str(DataTwo)

	def __makeSpace(self):

		""" Private method to add extra two coloums for remaining and state """

		for i in xrange(1, len(self.__data)):
			
			self.__data[i].append(self.__data[i][self.__quantity])
			self.__data[i].append(self.__data[i][self.__quantity])


	def __updateStatusValue(self):

		""" Private method to find the order status """

		for i in xrange(1, len(self.__data)):
			
			if self.__data[i][self.__old] == str(0):
				self.__data[i][self.__old + 1] = str("Closed")

			else:
				self.__data[i][self.__old + 1] = str("Open")


	def CalculateStatus(self):

		""" Public method that will return the status of following orders. """

		self.__makeSpace()

		for i in xrange(1, len(self.__data)):
			
			for j in xrange(1, int(self.__data[i][0])):
				
				if self.__data[i][self.__CI] == self.__data[j][self.__CI]:
					if self.__data[i][self.__Side] != self.__data[j][self.__Side]:

						self.__data[i][self.__old] , self.__data[j][self.__old] = self.__updateQuantity(self.__data[i][self.__old], self.__data[j][self.__old])
				
		self.__updateStatusValue()

		return self.__data


class QualityStateOutputter:

	""" This will prints the result in the desired format. """

	def __init__(self, data):
		self.__data = data

	def PrintOutput(self):

		""" Public method responsible for printing data as mentioned in output file. """

		print self.__data[0][0] + "," + self.__data[0][1] + "," + self.__data[0][2] + "," + self.__data[0][3]
		
		for i in xrange(1,len(self.__data)):

			self.__line = self.__data[i][0] + "," + self.__data[i][1] + "," + self.__data[i][2] + "," + self.__data[i][3] 
			self.__line = self.__line + "," + self.__data[i][4] + "," + self.__data[i][5]

			print self.__line


def main():

	""" Function to find the remaining and status of various stock orders. """


	"""
		If name of Input file is same as sample give, no change required!
	"""
	InputData = ImportData('SOES - Input.csv').getDataInList()


	""" 
		If the name of Input file might be diff, then uncomment the below code  
		and comment the above code!
	"""
	
	# InputFileName = raw_input("Name of CSV file : ")
	# InputData = ImportData(InputFileName).getDataInList()


	OutputData = CoreLogic(InputData).CalculateStatus()
	QualityStateOutputter(OutputData).PrintOutput()

if __name__ == '__main__':
	main()
