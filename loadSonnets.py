import json

class Word():
	def genRhymeNum():
		return

	def __init__(self, word):
		self.word = word
		self.rhymeNum = self.genRhymeNum()


class Line():
	def getLastWord():
		return
		"[\s||\-||\"||\(][A-Z'è]*[.!?\,\-;:\"—\)\s]*$"

	def __init__(self, title, author, lineNum, line):
		self.lineNum = lineNum
		self.line = line
		self.lastWord = self.getLastWord()

class Sonnet():
	def breakLines(text):
		return

	def __init__(self, title, author, text):
		self.title = title
		self.author = author
		self.lines = breakLines(text)

def divideSonnets(filename):
	sonnetFile = open(filename, 'r')
	print(sonnetFile)

divideSonnets('Misc_Sonnets.txt')

