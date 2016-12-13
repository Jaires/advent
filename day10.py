#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventWithFile
import re
from abc import ABCMeta, abstractmethod

class Robot:

	def __init__(self, microchip, botNumber):
		if not isinstance(microchip, list):
			microchip = [microchip]
		self.microchip = microchip or []
		self.botNumber = botNumber

	def isAvailable(self):
		return len(self.microchip) == 2

	def resetMicrochip(self):
		self.microchip = []

	def setMicrochip(self, value):
		if not value:
			raise
		self.microchip.append(value)

	def getMicrochip(self):
		return self.microchip

	def getBotNumber(self):
		return self.botNumber

	def __str__(self):
		return "Robot(%s)" % str(self.microchip)

class Command:
	__metaclass__ = ABCMeta

	def hasRequirements(self):
		return False

	@abstractmethod
	def apply(self, robots):
		pass

	@abstractmethod
	def getRelatedBots(self):
		pass

class ValueCommand(Command):

	def __init__(self, value, botNumber):
		self.value = value
		self.botNumber = botNumber

	def __str__(self):
		return "ValueCommand(%s,%s)" % (self.value, self.botNumber)

	def apply(self, robots):
		if self.botNumber in robots:
			robots[self.botNumber].setMicrochip(self.value)
		else:
			robots[self.botNumber] = Robot([self.value], self.botNumber)
		return True

	def getRelatedBots(self):
		return [self.botNumber]

class BotCommand(Command):

	def hasRequirements(self):
		return True

	def __init__(self, botNumber, lowBot, highBot, comparedMicrochips):
		self.botNumber = botNumber
		self.lowBot = lowBot
		self.highBot = highBot
		self.comparedMicrochips = comparedMicrochips

	def __str__(self):
		return "BotCommand(%s=>(%s,%s))" % (self.botNumber, self.lowBot, self.highBot)

	def apply(self, robots):
		if not self.botNumber in robots:
			return False

		microchips = robots[self.botNumber].getMicrochip()

		if len(microchips) < 2:
			return False

		robots[self.botNumber].resetMicrochip()
		if self.lowBot in robots:
			robots[self.lowBot].setMicrochip(min(microchips))
		else:
			robots[self.lowBot] = Robot(min(microchips), self.lowBot)
		if self.highBot in robots:
			robots[self.highBot].setMicrochip(max(microchips))
		else:
			robots[self.highBot] = Robot(max(microchips), self.highBot)

		if self.comparedMicrochips and not [ microchip for microchip in self.comparedMicrochips if microchip not in microchips]:
			print "Bot %s is comparing %s" % (self.botNumber, str(microchips))

		return True

	def getRelatedBots(self):
		return [self.lowBot, self.highBot]

class Day10(AdventWithFile):

	def __init__(self, comparedMicrochips=[], resultOutputs=[]):
		AdventWithFile.__init__(self)
		self.robots = {}
		self.commands = {}
		self.outputs = {}
		self.comparedMicrochips = comparedMicrochips
		self.resultOutputs = resultOutputs

	def parseLine(self, line):
		"""
		bot 37 gives low to bot 114 and high to bot 150
		value 2 goes to bot 156
		"""
		command = re.search(
			"(?P<botNumber>bot [0-9]+) gives low to (?P<lowBot>[a-z]+ [0-9]+) and high to (?P<highBot>[a-z]+ [0-9]+)",
			line)
		if command:
			return BotCommand((command.group("botNumber")), (command.group("lowBot")), (command.group("highBot")), self.comparedMicrochips)

		command = re.search("value (?P<value>[0-9]+) goes to (?P<botNumber>bot [0-9]+)", line)
		if command:
			return ValueCommand(int(command.group("value")), (command.group("botNumber")))

		raise Exception("Invalid command")

	def doCommand(self, command):
		# do single command
		if command.apply(self.robots):
			# check each affected robot
			for robot in command.getRelatedBots():
				if robot in self.robots and self.robots[robot].isAvailable() and robot in self.commands:
					if command.hasRequirements() and command.botNumber in self.commands:
						del self.commands[command.botNumber]
					self.doCommand(self.commands[robot])
			return True
		return False

	def loadData(self):
		for line in self.sourceFile.readlines():
			# parse command
			command = self.parseLine(line.strip())
			# is value command
			if command.hasRequirements():
				self.commands[command.botNumber] = command
			# do all commands available
			self.doCommand(command)

	def doPart1(self, ):
		self.loadData()

	def doPart2(self):
		self.loadData()
		result = 1
		for robot in self.robots:
			if robot in self.resultOutputs:
				result *= self.robots[robot].microchip[0]
		print result

Day10(comparedMicrochips=[61,17]).doPart1()
Day10(resultOutputs=["output 0", "output 1", "output 2"]).doPart2()