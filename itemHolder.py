'''
plan: 

get ItemHolder up and running

take StartScreen code, and combine 
with ItemHolder for backpack

use move method from item to allow
you to move the item List around

use button to close menu? need to fix
button code!!! 
'''
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
from Item import Item
import Objs2

class ItemHolder:

	def __init__(self):
		self.itemWidth = 60
		self.itemHeight = 40
		self.maxNumOfItems = 15
		self.leastNumOfItems = 4 # value to be changed in order to change the actual item holder seen on screen	
		self.surface = pygame.Surface((self.itemWidth , self.itemHeight * self.maxNumOfItems))
		self.surSeg = pygame.Rect((0,0),(self.itemWidth,self.itemHeight * self.leastNumOfItems))#surSeg aka surface segment
		self.itemTup = []
		#speed at which you go up and down the menu
		self.moveSpeed = 3 
		self.filename = "no_value"
		self.locOnScreen = [0,0]
		self.surfaceLoc = [0,0]
		#"hadBeen" proper conditions, meaning that the mouse had dragged the object completely into the itemColumn
		self.hadBeen = False  
		

	def add(self,item):
		self.itemTup.append(item)
		
	def setBackground_noFileName(self,image):
		self.surface.blit(image,(0,0))
	
	def setBackground_fileName(self,filename):
		sheet = spritesheet.spritesheet(filename)
		image = sheet.image_at(self.surface.get_rect())
		self.surface.blit(image,(0,0))
		
	def setLoc(self,x,y):
		self.locOnScreen[0] = x
		self.locOnScreen[1] = y 
	
	def getLoc(self):
		return self.locOnScreen
	
#to go up, you need to subtract in order to get as close to 'zero' as possible
	def goUp(self):
		if self.surface.get_rect().top <= self.surSeg.top - self.moveSpeed:
			self.surSeg.top -= self.moveSpeed
				
				
	'''remember that the bottom value will actually be the biggest value. 
	and so to get there, you need to add to the "top" value of the square in order
	to get the squar to go down'''	

	def goDown(self):
		if self.surface.get_rect().bottom >= self.surSeg.bottom + self.moveSpeed:
			self.surSeg.top += self.moveSpeed
				
	def getInventoryImage(self):
		tempSur = pygame.Surface(self.surSeg.size).convert()
		
		sentence ="self.surSeg is: ", str(self.surSeg)
		Objs2.tempSqs.add(sentence)			
		
		tempSur.blit(self.surface,(0,0),self.surSeg)
		return tempSur
	
		# loc = self.surSeg.topleft;default_loc = (0,0)
		# tempSur = pygame.Surface((self.surSeg.w,self.surSeg.h))
		# tempSur.blit(self.surface,default_loc,self.surSeg)
		# return tempSur
		
		
		
	def makeBasicInventory(self):
		
		self.setBackground_fileName("item_column_background.png")
		
		width = 10 #standard width 
		topBuffer = 2 #buffer between object
		sideBuffer = 2 #buffer between 
		
		currentLoc = [sideBuffer,topBuffer] # for initial image
		
		for num in range(len(self.itemTup)):
			self.surface.blit(self.itemTup[num].image,currentLoc)		
			currentLoc[0] = self.itemTup[num].sq.left + sideBuffer
			currentLoc[1] = self.itemTup[num].sq.top + topBuffer
	
	
	def holding(self,obj,map):
		
		columnRect = self.rectOnSur()
		rect = obj.getRect()
		upORdown = map['button']
		mouse = map['coords']
		
		if self.hadBeen and upORdown != "down" and columnRect.collidepoint(mouse):
			if obj not in self.itemTup:
				#print "inserted object into itemTup" 
				self.itemTup.append(obj)
				self.makeBasicInventory()
				
			self.hadBeen = False
		
		sentence ="self.completelyContainsRect(rect) is: ", str(self.completelyContainsRect(rect))
		Objs2.tempSqs.add(sentence)			
		
		if self.completelyContainsRect(rect) and upORdown == "down" and columnRect.collidepoint(mouse):
			self.hadBeen = True	
		
		
	#this was done to break up a very long and crazy if statement	
	def	completelyContainsRect(self,rect):
	
		columnRect = self.rectOnSur()
		
		# sentence ="columnRect is: ", str(columnRect)
		# Objs2.tempSqs.add(sentence)		
		# sentence ="columnRect.collidepoint(rect.bottomleft) is: ", str(columnRect.collidepoint(rect.bottomleft))
		# Objs2.tempSqs.add(sentence)
		# sentence ="columnRect.collidepoint(rect.bottomright) is: ", str(columnRect.collidepoint(rect.bottomright))
		# Objs2.tempSqs.add(sentence)		
		# sentence ="columnRect.collidepoint(rect.topleft) is: ", str(columnRect.collidepoint(rect.topleft))
		# Objs2.tempSqs.add(sentence)		
		# sentence ="columnRect.collidepoint(rect.topright) is: ", str(columnRect.collidepoint(rect.topright))
		# Objs2.tempSqs.add(sentence)				
	
	#indented to save a few calcuations. I am checking all of these because
	#I want the object to be entirely inside of the itemColumn when it is inserted into the itemColumn
		if columnRect.collidepoint(rect.bottomleft):
			if columnRect.collidepoint(rect.bottomright):
				if columnRect.collidepoint(rect.topleft):
					if columnRect.collidepoint(rect.topright): 
						return True
					else:
						return False
				else:
					return False						
			else:
				return False
		else:
			return False

			
	def rectOnSur(self):
	
		columnRect = pygame.Rect(self.surSeg)
		columnRect.left = self.locOnScreen[0]
		columnRect.top = self.locOnScreen[1]
		return columnRect	
		