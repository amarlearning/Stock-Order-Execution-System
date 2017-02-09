# !/usr/bin/env python

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

	def CalculateStatus(self):

		""" This will return the status of following orders. """

		print self.__data




def main():
	result = ImportData('SOES - Input.csv').getDataInList()
	Object = CoreLogic(result).CalculateStatus()




if __name__ == '__main__':
	main()















# self.__getCountryValue()

# def __getCountryValue(self):
# 	self.__country = {}
# 	for line in range(1, len(self.__results)):
# 		self.__country.update({ self.__results[line][2] : 0 })
# 	print self.__country