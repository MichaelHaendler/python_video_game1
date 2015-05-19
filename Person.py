
import pygame, sys, random
from pygame.locals import *
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
from sprite_strip_anim import SpriteStripAnim
from WalkingGUI import WalkingGUI, Circle
from Menu import Menu
#from Item import BackPack

import Objs2
import pygame
pygame.font.init()

class Person(pygame.sprite.Sprite):
    # Set speed vector
	change_x=0
	change_y=0
	
	#this variable is for when you begin, and the old x and old y, match
	#up to the new/current x and y
	default_left = 90
	default_top = 90

	def __init__(self):
		self.front = 0
		self.back = 1
		self.left = 2
		self.right = 3
		self.oldLeft = 0
		self.oldTop = 0         
		self.strips = []
		self.starting_pos = True
		self.rect = pygame.Rect(0,0,0,0)
		self.list = []
		self.graphicChoice = 0
		self.itemList = []
		self.choice = self.front
		self.dictLookUp = {}
		self.count = 0
		self.cho = 0
		self.clicked = False
		self.clickedSpot = (0,0)
		self.rightButton = False
		self.menu = Menu()
		self.walking = WalkingGUI()
		self.menu.addChoice("walking")
		self.menu.addChoice("back_pack")
		self.menu.addChoice("testing")
		self.menu.makeBasicMenu()
		#self.LTSelectedString = "nothing" 
		self.which = "nothing"
		#print "----"

		#self.backPack = BackPack()
		

	def sizeOfload(self,size):
		for number in range(size):
			self.strips.append(number)
	
	def load(self, filename, rects, count,which,name,colorkey=None, loop=False, frames=1):
		temp = SpriteStripAnim(filename, rects, count, colorkey, loop, frames)
		#self.strips.append(temp)
		#self.strips.append(str(which):  SpriteStripAnim(self, filename, rects, count, colorkey, loop, frames) )
		
		#print "name: ",name
		#print "which: ",which
		if which == "front" or which == "down" :
			num = self.front + self.locForStrips()
			
		if which == "back" or which == "up":
			num = self.back + self.locForStrips()
			
		if which == "left":
			num = self.left + self.locForStrips()
			
		if which == "right":
			num = self.right + self.locForStrips()
		
		self.count += 1
		tempString = name + "-" + which 
		self.dictLookUp[tempString] = num
		#print "num is: ", num 
		#print "-------------"
		self.strips[num] = temp
		self.rect = pygame.Rect(90,90,rects[0][2],rects[0][3])
		
	def locForStrips(self):
		
		diff = self.count % 4
		#print "diff (",diff,") = self.count (",self.count,") % 4"
		#print "returned: ",self.count - diff
		return self.count - diff
		
	def setRect(self,leftX = default_left,topY = default_top):
		self.rect.left = leftX
		self.rect.top = topY
		
	def changeX(self,x):
		self.rect.left += x
	
	def changeY(self,y):
		self.rect.top += y
	
	def setX(self,x):
		self.rect.left = x

	def setY(self,y):
		self.rect.top = y
		
	def getX(self):
		return self.rect.left
		
	def getY(self):
		return self.rect.top
		
	def getRect(self):
		return self.rect
		
	def Health(self,num):
		self.health += num 
		
	def Dead(self):
		if self.health <= 0:
			return True
		else:
			return False

	def setGraphic(self,string):
		self.graphicChoiceString = string
		
	def setWhichChar(self,name):
		self.charChoice = name
		
	def getWhichChar(self):
		return self.charChoice
	
	def whichAnim(self,name,which):
		tempString = name + "-" + which
		self.cho = self.dictLookUp[tempString]
		#if self.dictLookUp[tempString] == None:
			#print "not in here"
			#need to set a fallback graphic!!!
			#tempString = self.defaultLoc
			
	
	def image(self):
		#false, meaning he wasn't in the same place
		if self.change_x == 0 and self.change_y == 0:
			standing_still_image = self.strips[self.cho].next(1)
			self.pic = standing_still_image
			return self.pic
		else:
			self.pic = self.strips[self.cho].next()
			return self.pic
		#else:
			#return self.pic
			
	def move(self,map):
	
		if map['type'] == 'KEYDOWN':
			if map['K_LEFT'] == True:
				#Objs2.tempSqs.add('K_LEFTD')
				self.changespeed(-3,0)
				self.whichAnim(self.getWhichChar(),'left')
			if map['K_RIGHT'] == True:
				#Objs2.tempSqs.add('K_RIGHTD')
				self.changespeed(3,0)
				self.whichAnim(self.getWhichChar(),'right')
			if map['K_UP'] == True:
				#Objs2.tempSqs.add('K_UPD')
				self.changespeed(0,-3)
				self.whichAnim(self.getWhichChar(),'back')
			if map['K_DOWN'] == True:
				#Objs2.tempSqs.add('K_DOWND')
				self.changespeed(0,3)
				self.whichAnim(self.getWhichChar(),'front')

		if map['type'] == 'KEYUP':
			if map['K_LEFT'] == True:
				#Objs2.tempSqs.add('K_LEFTU')
				self.changespeed(3,0)
			if map['K_RIGHT']== True:
				#Objs2.tempSqs.add('K_RIGHTU')
				self.changespeed(-3,0)
			if map['K_UP'] == True:
				#Objs2.tempSqs.add('K_UPU')
				self.changespeed(0,3)
			if map['K_DOWN'] == True:
				#Objs2.tempSqs.add('K_DOWNU')
				self.changespeed(0,-3)

		self.wasClickedOn(map)
		self.rightClick(map)
	
	def setString(self,string):
		self.string = string

	def getString(self):
		return self.string	

	def addStringS(self,string):
		self.list.append(string)

	def getStringS(self):
		return self.list
		
	def clearStackData(self):
		self.list = []
		
	def graphic(self,num):
		self.graphicChoice = num
		
	def setGraphic(self,string):
		if string == "front":
			self.choice = self.front
		if string == "back" or string == "down":
			self.choice = self.back
		if string == "left":
			self.choice = self.left
		if string == "right":
			self.choice = self.right
		
    # Change the speed of the player
	def changespeed(self,x,y):
		#string = 'self.change_x is: ',str(self.change_x)
		#Objs2.tempSqs.add(string)
		#string = 'self.change_y is: ',str(self.change_y)
		#Objs2.tempSqs.add(string)
		
		self.change_x+=x
		self.change_y+=y
		
    # Find a new position for the player
	def update(self,collisionObjs):
        # Get the old position, in case we need to go back to it
		old_x=self.rect.left
		new_x=old_x+self.change_x
		self.rect.left = new_x

        #Did this update cause us to hit a wall?
		for rect in collisionObjs:
			collide = rect.colliderect(self.rect)
			if collide:
            #Whoops, hit a wall. Go back to the old position
				self.rect.left=old_x

		old_y=self.rect.top
		new_y=old_y+self.change_y
		self.rect.top = new_y

		for rect in collisionObjs:
		    #Did this update cause us to hit a wall?
			collide = rect.colliderect(self.rect)
			if collide:
            #Whoops, hit a wall. Go back to the old position
				self.rect.top=old_y
				
	def addItem(self,item):
		self.itemList.append(item)
		
	def savedClickedSpot(self):
		return self.clickedSpot
		
	def wasClickedOn(self,map):
		if self.rect.collidepoint(map['coords']) == True and map['button'] == 'down':
			self.clicked = True
			self.clickedSpot = map['coords']
			
	def rightClick(self,map):
		# print "self.rect is: ", self.rect
		# print "mouse is at: ",map['coords']
		# print "self.rect.collidepoint(map['coords']) is: ",self.rect.collidepoint(map['coords'])
		# print "map['button3'] is: ", map['button3']
		# print "map['button'] is: ",map['button']
	
		if self.rect.collidepoint(map['coords']) == True and map['button3']== True and map['button'] == 'down':
			self.rightButton = True
			self.clickedSpot = map['coords']
			
	def rightClicked(self):
		return self.rightButton
			
			
	def clickedOn(self):
		return self.clicked
			
	def set_clickedOn_to_false(self):
		self.clicked = False
		
	def closingClick(self,map):
		if self.clicked == True and self.rect.collidepoint(map['coords']) == True and map['button'] == 'down' and map['button3'] == True:
				return True 

				
	def runWalkingPath(self):
		if self.menu.nameOfSelectedBox() == "walking":
			return True
		else:
			return False
		

	def getMenu(self,map):
		#print "1 ----"
		'''getMenu checks to see if you clicked on something on the menu. 
	
		   if you did, it sets clicked to false, so that on the next screen update, the menu
		   will not appear. '''
	
		if self.menu.clickedOn(map): #menu.clickedOn returns true if you clicked on one of the squares, and false otherwise
			self.clicked = False
		return self.menu.currentMenu(map,self.clickedSpot) #returns the current menu
		
		
		#is used to prevent making circles in the exact same place

			
	def selected(self):
		#print self.menu.selectedBox()
		temp = self.menu.selectedBox()
		##print "temp is: ",temp
		#self.setLTSelected(temp)
		return temp
		
	def resetSelected(self):
		return self.menu.resetSelectedBox()
		
	# def setLTSelected(self,string):# set long term selected
		# self.LTSelectedString = string
		
	# def getLTSelected(self):
		# #print "self.LTSelectedString is: ",self.LTSelectedString
		# return self.LTSelectedString
		
	def runAction(self):
		#print "7 ----"
		if self.selected() == "exit":
			#print "exit"
			self.closeMenu()
		if self.selected() == "walking":
			#print self.selected()
			#print "11------------------"
			self.which = "walking"
			self.closeMenu()
			
		self.resetSelected()
		#print "and here it is: ",self.selected()
		
	def getAction(self):
		return self.which
			
	def resetAction(self):
		self.which = "nothing11"
			

		
	# def walkingString(self):
		# return "walking"
			
	def closeMenu(self):
		#print "set to false"
		self.rightButton = False
					
	
	def getCircleLoc(self):
		difference = self.rect.bottomright[0] - self.rect.bottomleft[0]
		difference = difference/2
		loc = [self.rect.bottomleft[0],self.rect.bottomleft[1]]
		loc[0] += difference
		return loc
		
	def getCircle(self):
		temp = Circle()
		temp.setCenter(self.getCircleLoc())
		return temp
	
	def updateScreen(self,map,surfaceObj):
		
		mouse = map["coords"]
		map["getCircle"] = self.getCircle()
		#items = map["items"]
		
		if self.getAction() == "walking":
		
			if self.rightClicked() == True: 
				self.closeMenu()
			
			circleTup = self.walking.tupOfPath(map) # adds circles
			for circle in circleTup:
				pygame.draw.circle(surfaceObj,circle.getColor(),circle.getPosition(),circle.getRadius(),circle.getWidth())
				tempLoc = circle.getPrevCirclePosition()
				if tempLoc[0] != -1 and tempLoc[1] != -1:
					pygame.draw.aaline(surfaceObj,circle.getColor(),circle.getPrevCirclePosition(),circle.getPosition(),circle.getBlend())
			
			
			if self.walking.rightClickedACircle(map) == True:
				tempMenu = self.walking.getMenu(map)
				surfaceObj.blit(tempMenu[0],tempMenu[1])
				
			if self.walking.getAction() == "exit":
				self.walking.closeCircleMenu()
				self.walking.resetAction()
				
			if self.walking.hadBeenClickedOn(map):
				self.walking.noLongerHoldingDownLeftButton()
				
			if self.walking.getAction() == "adjustCircle":
				self.adjCirclePos(map,mouse)
				
			if self.walking.getAction() == "walk":
				self.walking.walkThePath(map)			
				
		
		#FOR BACKPACK 
		
		'''
		backpack methods: 
		itemColumnContains(item) boolean
		backpack.add(item) nothing
		getBackPack(map) tup(surface,loc)
		'''
		
		'''
		Item methods: 
		getItems() tup of items
		
		# item.beenBlited = True
		'''
		
		# if self.getAction() == "back_pack":
				# #item needed a boolean "self.beenBlited" variable to know when to blit and not to blit
						
				# tempBackPack = self.backPack.getBackPack(map)
				# surface.blit(tempBackPack[0],tempBackPack[1]
				
			# if self.backPack.closePack() == True:
				# self.backPack.set_closePack_ToFalse()
				# self.walking.resetAction()
				
		surfaceObj.blit(self.image(), (self.getX(),self.getY()))
		self.image()
		
		#FOR DISPLAYING CHAR'S MENU
			
		if self.rightClicked() == True:
			tempMenu = self.getMenu(map)
			surfaceObj.blit(tempMenu[0],tempMenu[1])
			self.runAction()
		
		return surfaceObj
	##############END OF WALKING CALLS
	

	