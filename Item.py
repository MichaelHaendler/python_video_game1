
import Objs2
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from Menu import Menu

class Item:

	def __init__(self,x = 100,y = 330):
		
		self.sq = pygame.Rect(x,y,50,50)
		self.red = Color('red')
		self.green = Color('green')
		self.color = self.red
		self.thickness = 2 #arbitrary value
		self.image = pygame.Surface((25,25))
		#self.image.fill(Color("black"))
		self.name = "default_name"
		self.type = "default_type"
		self.diff = (0,0)
		self.inside = False
		self.menu = Menu()
		self.beenBlited = False
		
		
	def setType(self,type,itemMap):
	
		#note: itemMap is used to tell what items you 
		# have (and in the case of ammo and the like) how much you have. 
		
		if type == "gun":
			menu.add("shoot")
			menu.add("reload")
			menu.add("repair")
		
		if type == "health":
			menu.add("use")
				
				
	def getWidth(self):
		return self.sq.width 
		
	def getHeight(self):
		return self.sq.height
		
	def setImage(self,filename,rect):
		tempSheet = spritesheet.spritesheet(filename)
		self.image = tempSheet.image_at(rect)
		tempRect = self.image.get_rect()
		self.sq.width = tempRect.width
		self.sq.height = tempRect.height
	
	def collideChanges(self,tup):
		if self.sq.collidepoint(tup):
			self.color = self.green
			return True
		else:
			self.color = self.red
			return False
			
	def collides(self,tup):
		if self.sq.collidepoint(tup):
			return True
		else:
			return False
		
	def change(self,map):
		loc = map['coords']
		
		if self.sq.collidepoint(loc):
			print "here"
			self.move(map)
			
		
	def move(self,map):

		currLoc = map['coords']
		
		#the reason for the need of the "self.inside" is because, as the code
		#currently is, "down" is only detected as input a handful of times before
		# it stops being seen. The 2 if statements immediately below deal with that issue. 
		
		if map['button'] == "down" and self.sq.collidepoint(currLoc):
			self.inside = True
		if map['button'] == "up":
			self.inside = False
			self.diff = ()
			
		if self.inside:
			
			if len(self.diff) == 0:
				self.diff = currLoc
			else:
				adjXBy = currLoc[0] - self.diff[0]
				adjYBy = currLoc[1] - self.diff[1]
				self.sq.left = self.sq.left + adjXBy
				self.sq.top = self.sq.top + adjYBy
				self.diff = currLoc

			
	
	def getLoc(self):
		return self.sq.topleft
		
	def getRect(self):
		return self.sq
	
	
	############################
	# def setUpDownDisVal(self):
		
	# def setLeftRightDisVal(self):
		
		
	

		
	