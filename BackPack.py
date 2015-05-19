
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
#from itemHolder import itemHolder
import Objs2

class BackPack:

	def __init__(self,width = 100,height = 100):
		self.width = width
		self.height = height
		self.offImage = pygame.Surface((10,10)) #arb values
		self.loc = [20,20] #arb init value of where to place button on menu
		#self.name = "default_name"
		self.surface = pygame.Surface((width,height))
		self.inside = False
		self.diff = ()
		self.buttonHit = "default_name1"
		self.clicked = False
		self.buttonTup = []
		self.inside = False
		self.diff = ()
		#self.itemCol = itemHolder() #itemColumn							

	def setImage_noFile(self,image,dest = (0,0)):
		self.surface.blit(image,dest)
		
	def setImage(self,filename, dest = (0,0),rect= None):
		if rect == None:
			rect = (0,0,self.width,self.height)
			
		sheet = spritesheet.spritesheet(filename)
		self.surface.blit(sheet.image_at(rect),dest)
	
	def fill(self,filename,loc = [0,0]):
		rect =(loc[0],loc[1],self.surface.get_width(),self.surface.get_height())
		sheet = spritesheet.spritesheet(filename)
		self.surface.blit(sheet.image_at(rect),(0,0))	
	
	def setLoc(self,x = 0,y = 0):
		surRect = self.surface.get_rect()
		self.loc =[x,y]
		
		# print "self.surface.get_rect().top is: ", str(self.surface.get_rect().top)		
		# print "self.surface.get_rect().left is: ", str(self.surface.get_rect().left)
		
		# for button in self.buttonTup:
			# rect = button.getLoc()
			# rect[0] += y
			# rect[1] += x
			# button.setRect(rect)
			# print str(button.getRect())
		# self.testMethod(1)
		
	#for testing, not actually used in code
	def testMethod(self,string):
		print "--------------------------",string
		for button in self.buttonTup:
			print str(button.getRect())
				
	#updateLocs is currently not being used				
	def updateLocs(self,tup):
		x = tup[0]
		y = tup[1]
		for clickable in self.buttonTup:
				clickable.sq.top += x
				clickable.sq.left += y				
		
		
	def getLoc(self):
		return self.loc
		
	def addButton(self,filename,onImageRect,offImageRect,loc =(50,50),name = "no_name"):
	
		button = Button()
		button.onImage(filename,onImageRect)
		button.offImage(filename,offImageRect)
		button.setLoc(loc)
		button.setName(name)
		self.buttonTup.append(button)
	
	
	def addPreMadeButton(self,button):
		self.buttonTup.append(button)
		
	def show(self):
		return self.clicked
		
	def clickedOn(self,map):
		coords = map['coords']
		clickedOn = map['button1']
		
		if surRect.collidepoint(coords) and clickedOn:
			return True
		else:
			return False

	def getBackPack(self,map):####IMPORTANT METHOD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
		coords = map['coords']
		clickedOn = map['button1']
		map['inventoryLoc'] = self.loc
		
		surRect = self.surface.get_rect()
		surRect.left = self.loc[0]
		surRect.top = self.loc[1]
		tempSur = self.surface
		
		''' The code in this if statment was to be used to save some calculations. 
		However, it is not working (returning a modified surface) and I don't know why.'''
		# if surRect.collidepoint(coords) == False or clickedOn == False:
			# sentence ="same thing"
			# Objs2.tempSqs.add(sentence)
			# # print "when we're not touching it, tempSur if of type: ", str(type(tempSur))
			# return tempSur
		############
		
		tempSur = self.buttonUpdate(map,tempSur) #so that I can easily break up the individual types of updates 
		#print "out of buttonUpdate, tempSur if of type: ", str(type(tempSur))
		
		tempSur = self.inventoryUpdate(map,tempSur)
		#print "out of inventoryUpdate, tempSur if of type: ", str(type(tempSur))
		
		return tempSur
		
	def buttonUpdate(self,map,tempSur):
		
		for button in self.buttonTup:
		
			if button.getName() == "exit":
				tempSur.blit(button.getImage(map),button.getLoc())
		
			if button.getName() == "userBar":
				map['diff'] = self.diff
				map['inside'] = self.inside
				map = button.moveBox(map)
				
				self.inside = map['inside']
				self.diff = map['diff']
				self.loc = map['inventoryLoc']
				# sentence ="self.diff is now: ", str(self.diff)
				# Objs2.tempSqs.add(sentence)
				
			# if button.getName() == "invBox_down" and button.clickedOn_moved(map):
				# self.invBox.goDown()
				
			# if button.getName() == "invBox_up" and button.clickedOn_moved(map):
				# self.itemCol.goUp()
				
			# tempSur = self.itemCol.itemBox()	
			
			
			
		return tempSur
				
		# sentence ="got through for loop"
		# Objs2.tempSqs.add(sentence)
		print "out of loop"
		
		return tempSur
					
	def inventoryUpdate(self,map,tempSur):
		
		if self.buttonHit == "exit":
			self.clicked = False
			
		# if self.buttonHit == "up":
			# self.itemColumn.goUp()
		# if self.buttonHit == "down":
			# self.itemColumn.goDown()			
		# image = self.itemColumn.getImage()
		# loc = self.itemColumn.getLoc()
		# self.surface.blit(image,loc)
		
		self.buttonHit = "default_name2"
		
		return tempSur
	
	# def translateLoc(self,mouseLoc):
	
		# if self.surface.collidepoint(mouseLoc) == False:
			# return False
	
		# surLoc = self.surface.get_rect().topleft
		# transLoc = [mouseLoc[0] - surLoc[0] , mouseLoc[1] - surLoc[1]]
		
		# for button in self.buttonTup:
			# rect = button.getRect()
			# if rec.collidepoint(transLoc):
				
			
	def makeBasicMenu(self):
		for button in self.buttonTup:			
			self.surface.blit(button.getOffImage(),button.getLoc())
			
		#self.surface.blit(itemCol.getEmptyImage(),itemCol.getLoc())
			
			
		