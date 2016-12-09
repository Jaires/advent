from abc import ABCMeta, abstractmethod

class AdventOfCode:
	__metaclass__ = ABCMeta

	@abstractmethod
	def doPart1(self):
		pass

	@abstractmethod
	def doPart2(self):
		pass

	def result(self):
		pass

class AdventWithFile(AdventOfCode):
	__metaclass__ = ABCMeta

	def __init__(self):
		AdventOfCode.__init__(self)
		self.sourceFile = open(self.getSourceFile(), 'r')

	def getSourceFile(self):
		return self.__class__.__name__.lower() + ".txt"

	def doPart1(self):
		for line in self.sourceFile.readlines():
			self.doStep1(line)
		self.result()

	def doPart2(self):
		for line in self.sourceFile.readlines():
			self.doStep2(line)
		self.result()

	def doStep1(self, line):
		pass

	def doStep2(self, line):
		pass
