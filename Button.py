
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
import Objs2

class Button:

	def __init__(self):
		self.offColor = Color('red')
		self.onColor = Color('green')
		self.thickness = 2 #arbitrary value
		self.onImage = pygame.Surface((10,10)) #arb values
		self.offImage = pygame.Surface((10,10)) #arb values
		self.loc = [20,20] #arb init value of where to place button on menu
		self.name = "default_name"
		self.perform = False
		self.sq = pygame.Rect((0,0),(30,30)) # is used to say where an image goes on a surface
		self.movedAmount = [0,0]
		self.otherSq = pygame.Rect((0,0),(30,30))
		
	def setRect(self,rect):
		self.sq = rect
		
	def getRect(self,rect):
		return self.sq
		
	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name
		
	def runAction(self):
		return self.perform 
		
	def performAction(self):
		self.perform = True
		
	def stopPerforming(self):
		self.perform = False
		
	def collideChanges(self,tup):
		if self.sq.collidepoint(tup):
			self.color = self.onColor
			return True
		else:
			self.color = self.offColor
			return False
			
	def collides(self,tup):
		if self.sq.collidepoint(tup):
			return True
		else:
			return False
			
	def getRect(self):
		return self.sq
		
	def setThickness(self,num):
		self.thickness = num
		
	def getThickness(self):
		return self.thickness
			
	def getColor(self):
		return self.color
		
	def setOffColor(self,the_color):
		self.offColor = Color(the_color)
		
	def setOnColor(self,color):
		self.onColor = Color(the_color)
			
		
	#potentially for things like moving the button up and down (can be modified for other useage) 
	def moveAnywhere(self,map):

		currLoc = map['coords']
		
		#the reason for the need of the "self.inside" is because, as the code
		#currently is, "down" is only detected as input a handful of times before
		# it stops being seen. The two if statements immediately below deal with that issue. 
		
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
			
	def getImage(self,map):
		#buttonDown = map['button1']
		# string ="44buttonDown is: ", str(buttonDown)
		# Objs2.tempSqs.add(string)	
			
		if self.clickedOn_moved(map):
			return self.onImage
		else:
			return self.offImage
			
	# def clickedOn(self,map):
		
		# coords = map['coords']
		# buttonDown = map['button1']
		
		# string ="button's name is: ", str(self.name)
		# Objs2.tempSqs.add(string)
		
		# string ="buttonDown is: ", str(buttonDown)
		# Objs2.tempSqs.add(string)
	
		# string ="square is: ", str(self.sq)
		# Objs2.tempSqs.add(string)	
		
		
		# sameLoc = self.sq.collidepoint(coords)
		
		# string ="sameLoc is: ", str(sameLoc)
		# Objs2.tempSqs.add(string)
		
		# if sameLoc and buttonDown:
			# return True
		# else: 
			# return False
	
	def setOnImage_noFile(self,image):
		self.onImage = image
		
	def setOffImage_noFile(self,image):
		self.offImage = image
		self.sq = self.offImage.get_rect()
		
	def setOnImage(self,filename,rect):
		sheet = spritesheet.spritesheet(filename)
		self.onImage = sheet.image_at(rect)
		 
	def setOffImage(self,filename,rect):
		sheet = spritesheet.spritesheet(filename)
		self.offImage = sheet.image_at(rect)
		
		self.sq = self.offImage.get_rect()
		
	def getOffImage(self):
		return self.offImage
		
	def getOnImage(self):
		return self.onImage
	
	def getLoc(self):
		return self.sq.topleft
		
	def setLoc(self,x,y):
		self.sq.top = y
		self.sq.left = x
		
	# def setMovedAmount(self,loc):
		# self.movedAmount[0] = loc[0]
		# self.movedAmount[1] = loc[1]
		
		
	#self.sq and setLoc/getLoc are used for placing
	#the image. self.otherSq is used for defining 
	#where on the main surface the image lies 
	def setOtherSq(self,loc):
		self.otherSq = pygame.Rect(self.sq)
		self.otherSq.left += loc[0]		
		self.otherSq.top += loc[1]
		
	def getOtherSq(self):
		return self.otherSq
		
	def incOtherSq(self,loc):
		self.otherSq.left += loc[0]		
		self.otherSq.top += loc[1]
	
	def clickedOn_moved(self,map):
	
		# string ="here3"
		# Objs2.tempSqs.add(string)		
	
		invLoc = map['inventoryLoc']
		coords = map['coords']
		buttonDown = map['button1']
		# adjXby = invLoc[0] + self.loc[0]
		# adjYby = invLoc[1] + self.loc[1]
		tempSq = pygame.Rect(self.sq)
		
		# string ="invLoc is: ", str(invLoc)
		# Objs2.tempSqs.add(string)	
		
		# string ="self.loc is: ", str(self.loc)
		# Objs2.tempSqs.add(string)
		
		# string ="before, tempSq is: ", str(tempSq)
		# Objs2.tempSqs.add(string)	
		
		tempSq.left += invLoc[0] #adjust X by (amount in adjXby) 
		tempSq.top += invLoc[1] #adjust Y by (amount in adjYby)

		# string ="after, tempSq is: ", str(tempSq)
		# Objs2.tempSqs.add(string)	
		
		# string ="33button's name is: ", str(self.name)
		# Objs2.tempSqs.add(string)
		
		# string ="33buttonDown is: ", str(buttonDown)
		# Objs2.tempSqs.add(string)	
		
		sameLoc = tempSq.collidepoint(coords)
	
		# string ="33sameLoc is: ", str(sameLoc)
		# Objs2.tempSqs.add(string)
		
		if sameLoc and buttonDown:
			return True
		else: 
			return False
		
		
	def moveBox(self,map):

		currLoc = map['coords']
		currentState = map['button']	
		inside = map['inside']
		diff = map['diff']
		loc = map['inventoryLoc']
		
		# sentence ="here?"
		# Objs2.tempSqs.add(sentence)
		
		# sentence ="buttonState is: ",str(map['button1'])
		# Objs2.tempSqs.add(sentence)		
		
		#the reason for the need of the "self.inside" is because, as the code
		#currently is, "down" is only detected as input a handful of times before
		# it stops being seen. The 2 if statements immediately below deal with that issue. 
		
		if  currentState == "down" and self.clickedOn_moved(map):
			inside = True
			#sentence ="inside is: ", str(inside)
			#Objs2.tempSqs.add(sentence)
			
		if currentState == "up":
			inside = False
			diff = ()
			
		if inside:
			
			if len(diff) == 0:
				diff = currLoc
			else:
				adjXBy = currLoc[0] - diff[0]
				#sentence ="adjXBy = currLoc[0](",currLoc[0],") - diff[0](",diff[0],") is: ",str(adjXBy)
				#Objs2.tempSqs.add(sentence)
				
				adjYBy = currLoc[1] - diff[1]
				#sentence ="adjYBy = currLoc[1](",currLoc[1],") - diff[1](",diff[1],") is: ", str(adjYBy)
				#Objs2.tempSqs.add(sentence)				
	
				#sentence ="loc[0] = loc[0](",str(loc[0]) ,") + adjXBy(",str(adjXBy) ,") is: "
				#Objs2.tempSqs.add(sentence)
				loc[0] = loc[0] + adjXBy
				#Objs2.tempSqs.add(str(loc[0]))		
				
				#sentence ="loc[1] = loc[1](",str(loc[1]) ,") + adjYBy(",str(adjYBy) ,") is: "
				#Objs2.tempSqs.add(sentence)
				loc[1] = loc[1] + adjYBy
				# Objs2.tempSqs.add(str(loc[1]))
				
				diff = currLoc		
				
		map['inventoryLoc'] = loc
		map['diff'] = diff
		map['inside'] = inside
		
		return map
			
	
		