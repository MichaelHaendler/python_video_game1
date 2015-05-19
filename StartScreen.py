
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
import Objs2

class StartScreen: 

	def __init__(self,width,height):
		self.buttons = []
		self.surface = pygame.Surface((width,height))
		self.keepOpen = True
		self.selected = "nothing"
		
	
	#note: I could have inserted them based on length of 
	#tup...but the string makes the useage more obvious
	#(besides, this is still just alpha code)
	def placeAt(self,string,tup):
		
		if string == "background-noFile":
			self.staticImage_noFile(tup[0],tup[1])
		if string == "background":
			self.staticImage(tup[0],tup[1],tup[2])
		if string == "button":
			self.button(tup[0],tup[1],tup[2],tup[3],tup[4])
		
		
	def staticImage_noFile(self,image,toCoords):
		self.surface.blit(image,toCoords)
		
	#can be either whole backgrounds or just pieces (order sensitive) 		
	def staticImage(self,filename,rect,toCoords):
		sheet = spritesheet.spritesheet(filename)
		image = sheet.image_at(rect)
		self.surface.blit(image,toCoords)
		
		
	def button(self,filename,string,rect1,rect2,toCoords):
	
		tempSheet = spritesheet.spritesheet(filename)
		
		tempButton = Button()
		tempButton.setString(string)
		tempButton.setOffButton(tempSheet.image_at(rect1))
		tempButton.setOnButton(tempSheet.image_at(rect2))
		tempButton.setCoords(toCoords)
		self.buttons.append(tempButton)
		
		
	def makeBasicScreen(self):
		for button in self.buttons:
			self.surface.blit(button.getOffButton(),button.getCoords())
			
			
	def updateButtons(self,map):		
		tempSur = self.surface
		#tempSur = pygame.Surface(self.surface)
		coords = map['coords']
		clicked = map['button1']
		
		if clicked != False:
			for button in self.buttons:
				#string = "button.offContains(coords) is: ",str(button.offContains(coords))
				#Objs2.tempSqs.add(string)
				#string = "clicked is: ",str(clicked)
				#Objs2.tempSqs.add(string)
				if button.offContains(coords) and clicked:
					self.keepOpen = False
					#print "button.getString() is: ",button.getString()
					self.selected = button.getString()
					tempSur.blit(button.getOffButton(),button.getCoords())			
					
		
	def getScreen(self,map):
		
		tempSur = self.surface
		#tempSur = pygame.Surface(self.surface)
		coords = map['coords']
		clicked = map['button1']
		
		# if coords == (-1,-1) or clicked == False:
			# return (tempSur,self.getCoords())
		
		for button in self.buttons:
			string = "button.offContains(coords) is: ",str(button.offContains(coords))
			#Objs2.tempSqs.add(string)
			string = "clicked is: ",str(clicked)
			#Objs2.tempSqs.add(string)
			if button.offContains(coords) and clicked:
				self.keepOpen = False
				#print "button.getString() is: ",button.getString()
				self.selected = button.getString()
				tempSur.blit(button.getOffButton(),button.getCoords())
				
		return (tempSur,self.getCoords())
		
	def getCoords(self):
		return (0,0) #this will take up the whole screen 
		
	def getSelection(self):	
		return self.selected
		
	def stayOpen(self,map):
		return self.keepOpen
	
	def retSurfaceTup(self):
		return (self.surface,self.getCoords())
		
	
	
class Button:

	def __init__(self):
		self.loc = (0,0)
		self.offButton = 0
		self.onButton = 0
		self.string = "default_string22"
		
	def setCoords(self,loc):
		self.loc = loc
		
	def getCoords(self):
		return self.loc
		
	def setString(self,str):
		self.string = str

	def getString(self):
		return self.string
	
	def setOffButton(self,surf):
		self.offButton = surf
		
	def getOffButton(self):
		return self.offButton

	def offContains(self,loc):
	
		rect = self.offButton.get_rect()
		rect.topleft = self.loc
		
		if rect.collidepoint(loc):
			return True
		else:
			return False		
			
########

	def setOnButton(self,surf):
		self.onButton = surf
		
	def getOnButton(self):
		return self.onButton
		
	def onContains(self,loc):
	
		rect = self.onButton.get_rect()
		rect.topleft = self.loc
		
		if rect.collidepoint(loc):
			return True
		else:
			return False
			


	