#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventOfCode
import md5

class Day5(AdventOfCode):
	def __init__(self):
		self.doorId = "cxdnnyjw"
		self.password1 = ""
		self.password2 = {}
		self.positionChars = []
		for validPosition in range(0,8):
			self.positionChars.append(str(validPosition))

	def doPart1(self):
		index = 0
		while True:
			code = self.doorId + str(index)
			m = md5.new(code).hexdigest()
			if m[0:5] == "00000":
				self.password1 = self.password1 + m[5]

			if len(self.password1) == 8:
				break
			index += 1
		self.result()

	def doPart2(self):
		index = 0
		while True:
			code = self.doorId + str(index)
			m = md5.new(code).hexdigest()
			if m[0:5] == "00000":
				self.password1 = self.password1 + m[5]

			if m[0:5] == "00000" and m[5] in self.positionChars:
				position = int(m[5])
				if not position in self.password2:
					self.password2[position] = m[6]

			if len(self.password2) == 8:
				break
			index += 1
		self.result()

	def result(self):
		print self.password1[0:8]
		if self.password2:
			passwordTrans2 = ""
			for index in range(0,8):
				passwordTrans2 = passwordTrans2 + self.password2[index]
			print passwordTrans2

Day5().doPart2()