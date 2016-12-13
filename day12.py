#!/usr/bin/python
# coding=utf8

from adventOfCode import AdventWithFile
import re
from abc import ABCMeta, abstractmethod

class Instruction:
	__metaclass__ = ABCMeta

	@abstractmethod
	def run(self, register, position):
		pass

class CopyInstruction(Instruction):

	def __init__(self, source, target):
		try:
			self.source = int(source)
		except:
			self.source = source

		self.target = target

	def run(self, register, position):
		if isinstance(self.source, str):
			register[self.target] = register[self.source]
		else:
			register[self.target] = self.source
		return position + 1

	def __str__(self):
		return "cpy %s %s" % (str(self.source), str(self.target))

class MathInstruction(Instruction):
	def __init__(self, source, difference):
		self.source = source
		self.difference = difference

	def run(self, register, position):
		register[self.source] = register[self.source] + self.difference
		return position + 1

	def __str__(self):
		return "math %s %d" % (self.source, self.difference)

class DecInstruction(MathInstruction):
	def __init__(self, source):
		MathInstruction.__init__(self, source, -1)

class IncInstruction(MathInstruction):
	def __init__(self, source):
		MathInstruction.__init__(self, source, 1)

class JumpInstruction(Instruction):
	def __init__(self, source, offset):
		try:
			self.source = int(source)
		except:
			self.source = source
		self.offset = offset

	def run(self, register, position):
		if isinstance(self.source, str) and register[self.source]:
			return position + self.offset
		elif isinstance(self.source, int) and self.source != 0:
			return position + self.offset
		return position + 1

	def __str__(self):
		return "jnz %s %d" % (self.source, self.offset)

class InstructionFactory:

	CPY = "cpy"
	JNZ = "jnz"
	INC = "inc"
	DEC = "dec"

	@staticmethod
	def createInstruction(line):
		"""
		cpy 1 a
		jnz c 2
		inc d
		dec c
		:return:
		"""

		command = re.search(
			"(?P<instruction>[a-z]{3}) (?P<param1>[a-z0-9]+)( (?P<param2>-?[a-z0-9]+))?",
			line.strip())
		if command:
			if command.group("instruction") == InstructionFactory.CPY:
				return CopyInstruction(command.group("param1"), command.group("param2"))
			elif command.group("instruction") == InstructionFactory.JNZ:
				return JumpInstruction(command.group("param1"), int(command.group("param2")))
			elif command.group("instruction") == InstructionFactory.INC:
				return IncInstruction(command.group("param1"))
			elif command.group("instruction") == InstructionFactory.DEC:
				return DecInstruction(command.group("param1"))
			else:
				raise Exception("Invalid instruction " + line)
		else:
			raise Exception("Invalid syntax " + line)

class Day12(AdventWithFile):

	def __init__(self):
		AdventWithFile.__init__(self)
		self.program = []

	def run(self, register):
		position = 0
		instruction = self.program[position]
		while True:
			position = instruction.run(register, position)
			if len(self.program) > position:
				instruction = self.program[position]
			else:
				break

	def doPart1(self):
		for line in self.sourceFile.readlines():
			instruction = InstructionFactory.createInstruction(line.strip())
			self.program.append(instruction)
		register = { "a": 0, "b": 0, "c": 0, "d": 0}
		self.run(register)
		print str(register)

	def doPart2(self):
		for line in self.sourceFile.readlines():
			instruction = InstructionFactory.createInstruction(line.strip())
			self.program.append(instruction)
		register = {"a": 0, "b": 0, "c": 1, "d": 0}
		self.run(register)
		print str(register)

Day12().doPart1()
Day12().doPart2()