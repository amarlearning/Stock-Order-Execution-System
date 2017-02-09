#!/usr/bin/env python
# @Author: @amarlearning
# @Date:   2017-02-08
# @Email:  amar.om1994@gmail.com


class ImportData:

	""" This is to import data form the cvs file. """

	def __init__(self, Name):

		self.__name = Name

	def getDataInList(self):

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

	def __updateQuantity(self, DataOne, DataTwo):

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

		for k in xrange(1, 3):
			for i in xrange(1, len(self.__data)):
				
				self.__data[i].append(self.__data[i][self.__quantity])


	def __updateStatusValue(self):

		for i in xrange(1, len(self.__data)):
			
			if self.__data[i][4] == str(0):
				self.__data[i][5] = str("Closed")

			else:
				self.__data[i][5] = str("Open")


	def CalculateStatus(self):

		""" This will return the status of following orders. """

		self.__makeSpace()

		for i in xrange(1, len(self.__data)):
			
			or j in xrange(1, int(self.__data[i][0])):
				
				if self.__data[i][self.__CI] == self.__data[j][self.__CI]:
					if self.__data[i][self.__Side] != self.__data[j][self.__Side]:

						self.__data[i][4] , self.__data[j][4] = self.__updateQuantity(self.__data[i][4], self.__data[j][4])
				
		self.__updateStatusValue()
		return self.__data


class QualityStateOutputter:

	""" This will prints the result in the desired format. """

	def __init__(self, data):
		self.__data = data

	def PrintOutput(self):

		print self.__data[0][0] + "," + self.__data[0][1] + "," + self.__data[0][2] + "," + self.__data[0][3]
		
		for i in xrange(1,len(self.__data)):

			self.__line = self.__data[i][0] + "," + self.__data[i][1] + "," + self.__data[i][2] + "," + self.__data[i][3] 
			self.__line = self.__line + "," + self.__data[i][4] + "," + self.__data[i][5]

			print self.__line


def main():
	inputData = ImportData('SOES - Input.csv').getDataInList()
	outputData = CoreLogic(inputData).CalculateStatus()
	QualityStateOutputter(outputData).PrintOutput()

if __name__ == '__main__':
	main()