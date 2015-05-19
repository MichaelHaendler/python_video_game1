
import pygame
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
from sprite_strip_anim import SpriteStripAnim
#import spritesheet
from spritesheet import spritesheet

class GunImage:

	def __init__(self,rect,filename,shapeTup,name):
		self.countName = name #ranges from 0 to 7 
		self.rect = rect
		count = 1
		colorkey = -1
		loop = False
		self.shape = shapeTup
		FPS = 120
		speed = 14
		frames = FPS / speed
		# temp = SpriteStripAnim(filename, rect, count, colorkey, loop, frames)
		# self.image = temp.next(0)
		
		tempRect = pygame.Rect(rect)
		#print"and the square we have in GunImage is: ",tempRect, "11111111111"
		#self.image = SpriteStripAnim(filename, tempRect, count, colorkey, loop, frames)
		pic = spritesheet(filename)
		self.image = pic.image_at(tempRect,colorkey)
		self.filename = filename
		
	def getImage(self):
		return self.image
		
	def getX(self):
		return self.rect.left
		
	def getY(self):
		return self.rect.top		
		
	def shape_And_Filename(self):
		return (self.shape,self.filename)
		
	def getCountName(self):
		return self.countName # 0 to 7 
		
	def containsPerson(self,personRect, fakeSurface = (0,0)):
		width=1
		colorkey = -1
		tempSurface = pygame.display.set_mode(fakeSurface)
		tempShape = pygame.draw.lines(tempSurface,colorkey,True, self.shape,width)
		
		if tempShape.collidepoint(personRect.center):
			return True
		else:
			return False
	
	def centerOfBarrel(self):
		bufferX = 10
		bufferY = 10
		tup = self.rect.midright
		# tup[0] += bufferX
		# tup[1] += bufferY
		return tup
		
	def getRect(self):
		return self.rect
		
	def setRect(self,rect):
		self.rect = rect
		