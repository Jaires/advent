#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventWithFile

class Day2(AdventWithFile):
	@staticmethod
	def move(position, direction):
		if direction == "U":
			if position - 3 < 0:
				return position
			else:
				return position - 3
		if direction == "D":
			if position + 3 > 9:
				return position
			else:
				return position + 3
		if direction == "L":
			if position % 3 == 1:
				return position
			else:
				return position - 1
		if direction == "R":
			if position % 3 == 0:
				return position
			else:
				return position + 1

	@staticmethod
	def move2(position, direction):
		uMove = {"D": "B", "A": "6", "B": "7", "C": "8", "6": "2", "7": "3", "8": "4", "3": "1"}
		dMove = {"1": "3", "2": "6", "B": "D", "4": "8", "6": "A", "7": "B", "8": "C", "3": "7"}
		lMove = {"9": "8", "4": "3", "8": "7", "C": "B", "3": "2", "7": "6", "B": "A", "6": "5"}
		rMove = {"5": "6", "2": "3", "6": "7", "A": "B", "3": "4", "7": "8", "B": "C", "8": "9"}

		if direction == "U":
			if position in ("5","2","1","4","9"):
				return position
			else:
				return uMove[position]

		if direction == "D":
			if position in ("5","A","D","C","9"):
				return position
			else:
				return dMove[position]

		if direction == "R":
			if position in ("1","4","9","C","D"):
				return position
			else:
				return rMove[position]

		if direction == "L":
			if position in ("1","2","5","A","D"):
				return position
			else:
				return lMove[position]

	def __init__(self):
		AdventWithFile.__init__(self)
		self.code1 = ""
		self.code2 = ""

	def doStep1(self, line):
		self.position = 5
		for character in line.strip():
			self.position = Day2.move(self.position, character)
		self.code1 = self.code1 + str(self.position)

	def doStep2(self, line):
		self.position2 = "5"
		for character in line.strip():
			self.position2 = Day2.move2(self.position2, character)
		self.code2 = self.code2 + self.position2

	def result(self):
		if self.code1:
			print self.code1
		if self.code2:
			print self.code2

Day2().doPart1()
Day2().doPart2()