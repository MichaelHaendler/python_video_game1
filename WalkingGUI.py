
import sys, pygame, random
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
import math
from Menu import Menu, Squares, Square
import Objs2



class WalkingGUI:

	def __init__(self):
		self.blend = 1
		self.clicked = False
		self.circles = []
		self.initialCircleAddedTF = False
		self.menu = Menu()
		self.menu.addChoice("walk")
		self.menu.addChoice("adjustCircle")
		self.menu.makeBasicMenu()
		self.rightButton = False # for displaying the (big)menu itself
		self.disCirMenu = False #display Circle Menu...for displaying the circle menu on a particular circle
		self.setTo = False #for showing the circles themselves
		self.oldTup = ()
		self.displayMenuAtLoc =(0,0)
		self.tempTupOfPath = []	

	def getMenu(self,map):		
		
		if self.menu.clickedOn(map): #menu.clickedOn returns true if you clicked on one of the squares, and false otherwise
			self.rightButton = False
			self.disCirMenu = False
		string = "here self.disCirMenu is22: ", str(self.disCirMenu)
		Objs2.tempSqs.add(string)
		return self.menu.currentMenu(map,self.displayMenuAtLoc)
		
	def clickedOn(self):
		return self.rightButton 
		
	def run(self):
		return self.setTo 
		
	def setToRun(self):
		self.setTo = True
		
	def stopRun(self):
		print "very bad"
		self.setTo = False
		
	def getAction(self):
		return self.menu.selectedBox()
		
	def resetAction(self):
		self.menu.resetSelectedBox()
		#self.which = "nothing11"
		
	def closeMenu(self):
		self.rightButton = False
		
	def closeCircleMenu(self):#check this out again
		self.disCirMenu = False
		

	def rightClickedACircle(self,map):
	
		#a silly, simple, and hacked way to keep this returning 
		# True so that the Menu doesn't disappear on the next iteration
		string = "self.disCirMenu is11: ", str(self.disCirMenu)
		Objs2.tempSqs.add(string)
		if self.disCirMenu == True:
			return True
				
		#print "bang" 
		for circle in self.circles:
			#print "zoom" 
			if circle.rightClickedOn(map) == True and circle.contains(map['coords']):
				self.displayMenuAtLoc = map['coords']
				self.disCirMenu = True
				return True
				
				
		return False
		#print "---------"
		#return False		
		
	def adjCirclePos(self,map,mouse):
		for circle in self.circles:
			if circle.leftClickedOn(map) and circle.contains(map['coords']):
				if len(self.oldCoords) == 0:
					self.oldCoords = new_tup
					circle.setColor(Color("blue"))
				else:
					new_coords = mouse.getLoc()
					#print "finally!"
					changeXby = new_coords[0] - self.oldCoords[0]
					changeYby = new_coords[1] - self.oldCoords[1]
					circle.adjLoc((changeXby,changeYby))
					old_tup = new_tup	
	
	def noLongerHoldingDownLeftButton(self):
		self.oldTup = ()
		circle.setColor("green")
		
	def hadBeenClickedOn(self,map):
		if len(self.oldTup) >= 1 and (map['button'] == "up" or map['button1'] == False):
			return True
		else:
			return False

	
		
	def input(self,map):
		if map['button1'] == 1:
			self.clicked = True
			
		if map['button2'] == True:
			self.removeCircle(map[coords])
			
	
	def clicked(self):
		temp = False
		if self.clicked == True:
			temp = self.clicked
			self.clicked = False
		return temp
	
	def blend(self):
		return self.blend
		
	def getCircles(self):
		return self.circles
		
	def setCircles(self, tup):
		self.circles = tup
		
	def removeCircle(self,coords):
		x = 0
		y = 1
		for circle in self.circles:
			if circle.inCircle(coords[x],coords[y]) == True: 
				self.circles.remove(circle) 
				
	def inside_Or_Outside_Of_Current_Circle(self,coords):
		x = 0
		y = 1
		for circle in self.circles:
			if circle.inCircle(coords[x],coords[y]) == True: 
				return True
				
		return False
		
	def addCircle(self,circle):
		self.circles.append(circle)
		
	def removeCircle(self,circle):
		self.circles.remove(circle)
		
	def emptyCircleTup(self):
		self.circles = []
		self.initialCircleAddedTF = False
		
	def addInitialCircle(self, circle):
		if len(self.circles) == 0:
			self.circles.append(circle)
			self.initialCircleAddedTF = True
		
	def initialCircleAdded(self):
		return self.initialCircleAddedTF	


#############################################

		
	def tupOfPath(self,map):
			
			#print "self.initialCircleAdded() is: ", self.initialCircleAdded()
			#print "size is: ", len(self.getCircles())
			
			if self.initialCircleAdded() == False:   
				self.addInitialCircle(map['getCircle']) #add it's circle to the general list to be printed
				
			if self.mouseOnExistingCircle(map):
				return self.getCircles()			
			
			#print "size2 is: ", len(self.getCircles())		
			
			circleTup = self.manipulateCircleLoc(map) #this allows you to change the location of a circle
			
			#circleTup = self.getCircles()
			circleToBeLinkedTo = circleTup[len(circleTup) - 1]
			
			#if we left click on a spot to create a new circle at that spot,then
			#create a new circle for that location, and link it to the last circle entered into the queue
			
			if map['button1'] == True: #and self.initialCircleAdded() == True:
				tempLoc = map['coords']
				newCircle = Circle(tempLoc[0],tempLoc[1])
				circleToBeLinkedTo.lineTo(map['coords'])
				self.addCircle(newCircle)		
				
			string = "self.getCircles() is: ", len(self.getCircles())
			Objs2.tempSqs.add(string)
			return self.getCircles()


	def manipulateCircleLoc(self,map):
	
		circleTup = self.getCircles()
		coords = map['coords']
		leftButton = map['button1']
		
		if leftButton == False:
			return circleTup
		
		for circle in circleTup:
			if circle.contains(coords):
				oldCoords =  self.oldCircle.getPosition()
				xVal = coords[0] - oldCoords[0] 
				yVal = coords[1] - oldCoords[1]
				pos = circle.getPosition()
				circle.adjPosition(pos)
				circle.setColor('blue')
				return circleTup # save a little time
		
		return circleTup #if left button is true but not on a circle
		


	def mouseOnExistingCircle(self,map):
	
		circleTup = self.getCircles()
		size = len(circleTup)
		coords = map['coords']
		
		#string = "The mouse is within a circle: ", str(circleTup[size -1].contains(coords))
		#Objs2.tempSqs.add(string)
		#print string
		if circleTup[size -1].contains(coords):
			return True
		else:
			for circle in circleTup:
				if circle.contains(coords):
					return True
		
		return False
		
	def deletePath(self):
		self.emptyCircleTup()
		self.set_clickedOn_to_false()
		
	def removeAnyClickedOnCircle(self):
		tupOfCircles = self.getCircles()
		for num in range(len(tupOfCircles)-1):
			circle = tupOfCircles[num]
			if circle.contains(loc):
				tupOfCircles.remove(circle)
				prevCircle = tupOfCircles[num - 1]
				prevCircle.pointToNothing()
				self.setCircles(tupOfCircles)
				
		#gives you an unmodified verion of what tupOfPath() already created		
	# def getTupOfPath(self):			
		# return self.getCircles()
		
	def getLoc(self):
		lowerLeft = self.rect.bottomleft
		lowerRight = self.rect.bottomright
		return (lowerRight[0] - lowerLeft[0],lowerLeft[1])
		
		
	def walkThePath(self,map):
		
		if len(self.tempTupOfPath) == 0:
			self.tempTupOfPath = self.getCircles()
			#del self.tempTupOfPath[] #remove character's circle 
		
		nextCircle = self.tempTupOfPath[1]
		
		#purpose of 'done' is to prevent 2 or even 3 of the if statements to run in a single run (and thus
		#causing the character to get moved more than he should in a single update.)
		done = False 
		
		''' if you haven't gotten to the next circle yet, just increment movement'''	
		if self.getLoc() != nextCircle.getPosition(): # and done == False:
			self.updatePos()
			done = True
			
		''' if you get to the circle that you're going to, and it's the last
		circle in the tup, it means you're at the end of the walk (so you end it)'''
		if self.getLoc() == nextCircle.getPosition() and len(self.tempTupOfPath) == 1 and done == False:
			#self.doneWalking()
			#del self.tempTupOfPath[0]
			self.tempTupOfPath = []
			done = True
			
		''' if you get to the circle that you were going to, and there are still more circles on the path to go to, 
		then delete the circle that you just came from and start going to the next one'''
		
		'''circle A, B, and C. You just went from A to B. Now you go from B to C by removing A, 
		and thus making the updatePos() method consider the angle between B and C'''
		if self.getLoc() == nextCircle.getPosition() and len(self.tempTupOfPath) > 1 and done == False: 
			del self.tempTupOfPath[0]
			#tempTupOfPath.pop()
			self.setCircles(tempTupOfPath) 
			self.updatePos()

	def updatePos(self):
		rateOfSpeed = 3 #increment this value in order to speed up movement
		currentCircleLoc = self.tempTupOfPath[0].getPosition()
		nextCircleLoc = self.tempTupOfPath[1].getPosition()
		# print "currentCircle[0] is: ",currentCircle
		# print " nextCircle[0] is: ",nextCircle[0]	
		deltaX = nextCircleLoc[0] - currentCircleLoc[0]
		deltaY = nextCircleLoc[1] - currentCircleLoc[1]
		
		val = deltaX/deltaY
		val *= rateOfSpeed
		tupOfPos =[self.rect.center[0],self.rect.center[1]]
		tupOfPos[0] += val
		tupOfPos[1] += val
		self.rect.center = tupOfPos		
		
################################################################
		
class Circle:

	def __init__(self, x = 90, y = 30):
		self.blend = 3
		self.radius = 10
		self.center_x = x
		self.center_y = y
		self.secondPoint = (-1,-1)
		self.color = "green"

		
	def rightClickedOn(self,map):
		coords = map['coords']
		# print "self.inCircle(coords[0],coords[1]) is: ",self.inCircle(coords[0],coords[1])
		# print "map['button3'] is: ",map['button3']
		# print "map['button'] is: ",map['button']
		# print "-----------"
		
		if self.inCircle(coords[0],coords[1]) == True and map['button3']== True and map['button'] == 'down':
			#print "here111" 
			self.rightButton = True
			return True
		# else:
			# return False
			
	def leftClickedOn(self,map):
		coords = map['coords']
		if self.inCircle(coords[0],coords[1]) == True and map['button1']== True and map['button'] == 'down':
			self.leftButton = True
		
	def setCenter(self,tup):
		self.center_x = tup[0]
		self.center_y = tup[1]
		
	def adjPos(self,adj):
		self.center_x += adj[0]
		self.center_y += adj[1]
		
	def setX(self,x):
		self.center_x = x	
		
	def setY(self,y):
		self.center_y = y	
		
	def inCircle(self, x, y):
		square_dist = (self.center_x - x) ** 2 + (self.center_y - y) ** 2
		return square_dist <= self.radius ** 2
		
	def lineTo(self,mouseTup):
		self.secondPoint = mouseTup 
		
	def getColor(self):
		return Color(self.color)
		
	def setColor(self,string):
		self.color = string
		
	def getRadius(self):
		return self.radius
		
	def getWidth(self):
		return self.radius - 1
		
	def getPosition(self):
		temp = [self.center_x,self.center_y]
		return temp
		
	def getPrevCirclePosition(self):
		return self.secondPoint
		
	def getBlend(self):
		return self.blend
		
	def pointToNothing(self):
		self.secondPoint = (-1,-1)		
		
		
	def contains(self,loc):
	
		#(mouse coordinates where the user clicked)
		mx = loc[0] 
		my = loc[1] 	

		#(centre of circle)
		cx = self.center_x
		cy = self.center_y

		distance = math.sqrt((mx - cx) * (mx - cx) + (my - cy) * (my - cy))
		
		if distance <= self.radius: 
			return True
		else:
			return False
		
		#http://cboard.cprogramming.com/game-programming/7470-point-lies-circle.html
		
		