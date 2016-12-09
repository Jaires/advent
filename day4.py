#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventWithFile

def distributionComparator(x, y):
	if x[1] == y[1]:
		return ord(y[0]) - ord(x[0])
	else:
		return x[1] - y[1]

class Day4(AdventWithFile):
	@staticmethod
	def getCheckSum(part):
		part = part.replace("-","")
		charDict = {}
		for char in part:
			if char in charDict:
				charDict[char] += 1
			else:
				charDict[char] = 1

		sortedChars = sorted(charDict.items(), cmp=distributionComparator)

		out = ""
		for char in sortedChars:
			out = char[0] + out
		return out

	@staticmethod
	def decrypt(string, shift):
		output = ""
		for char in string:
			if char == "-":
				output += " "
			else:
				output += chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
		return output

	def __init__(self):
		AdventWithFile.__init__(self)
		self.total = 0
		self.northPoleNumber = 0

	def doStep1(self, line):
		self.doStep2(line)

	def doStep2(self, line):
		#aaaaa-bbb-z-y-x-123[abxyz]
		lineParts = line.strip().rsplit("-", 1)
		computedChecksum = self.getCheckSum(lineParts[0])
		checksumParts = lineParts[1].split("[")
		checksum = checksumParts[1][:-1]
		sectorId = int(checksumParts[0])
		if computedChecksum[0:5] == checksum:
			roomName = self.decrypt(lineParts[0], sectorId)
			if "pole" in roomName:
				self.northPoleNumber = sectorId
			self.total += sectorId

	def result(self):
		if self.total:
			print "Part 1: Total sum is %s" % self.total
		if self.northPoleNumber:
			print "Part 2: Room number is %s" % self.northPoleNumber

#Day4().doPart1()
Day4().doPart2()