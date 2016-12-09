#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventWithFile

class Day9(AdventWithFile):

	def decompress(self, substring, recursion = False):
		index = 0
		totalSize = 0

		while True:
			startMarker = substring.find("(", index)
			if startMarker == -1:
				totalSize += len(substring) - index
				break

			endMarker = substring.find(")", startMarker)
			marker = substring[startMarker + 1: endMarker]
			marker = marker.split("x")
			charLen = int(marker[0])
			repeat = int(marker[1])

			# add skipped characters
			totalSize = totalSize + startMarker - 1 - index
			# add decompressed size
			if recursion:
				endIndex = endMarker + 1 + charLen
				totalSize += repeat * self.decompress(substring[endMarker+1:endIndex], True)
			else:
				totalSize += repeat * charLen
			index = endMarker + charLen

		return totalSize

	def doPart1(self):
		compressedFile = self.sourceFile.readline().strip()
		print "Part 1: File size is %d" % self.decompress(compressedFile)

	def doPart2(self):
		compressedFile = self.sourceFile.readline().strip()
		print "Part 2: File size is %d" % self.decompress(compressedFile, True)

Day9().doPart1()
Day9().doPart2()