
import sys, pygame, random
from pygame.locals import *

class Write:

	def __init__(self):
		self.sqs = Squares()
		
	def writeIt(self,string):
		self.sqs.add(string)
		
	def getSurfaceOfWords(self, num = [0,0]):
		
		print "self.sqs.getHeight() is: ",self.sqs.getHeight()
		print "self.sqs.getWidth() is: ",self.sqs.getWidth()
		
		tup = (self.sqs.getWidth(),self.sqs.getHeight())
		
		surface = pygame.Surface(tup)
		
		tempTup = [0,0]
		
		height = self.sqs.getHeight()
		
		for sq in self.sqs.getSquares():
			print "sq.getString() is: ", sq.getString()
			surface.blit(sq.getSurface(),tempTup)
			tempTup[1] = tempTup[1] + height
		self.sqs.clear()
			
		return [surface, num]
				
class Squares:

	def __init__(self):
		self.tup = []
		self.height = -1 #greatest height found
		self.width = -1 #greatest width found 
		
	def add(self,string):
	
		square = Square(string)
		
		if self.width < square.getWidth():
			self.width = square.getWidth()
		
		if self.height < square.getHeight():
			self.height = square.getHeight()
	
		self.tup.append(square)
		
	def getHeight(self):
		#print "self.height is: ",self.height
		#print "len(self.tup) is: ",len(self.tup)
		num = self.height * len(self.tup) 
		#print "num is: ",num 
		return num
		
	def getWidth(self):
		return self.width
		
	def getSquares(self):
		return self.tup
		
	def clear(self):
		self.width = -1
		self.height = -1
		self.tup = []
		
		
		
class Square:

	def __init__(self,string = 'default_string',size=20,font='freesansbold.ttf',color='black'):
		BASICFONT = pygame.font.Font(font, size)
		#self.textSurface = BASICFONT.render(str(string), True, Color(color),None)
		self.textSurface = BASICFONT.render(str(string), True, Color(color),Color("white"))
		self.str = string
		
		
	#note: getString is for debug purposes only (nothing actually uses/relies on it) 	
	def getString(self):
		return self.str 
		
	def getSurface(self):
		return self.textSurface
		
	def getWidth(self):
		return self.textSurface.get_width()
	
	def getHeight(self):
		return self.textSurface.get_height()
	
	