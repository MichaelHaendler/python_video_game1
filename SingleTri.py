import pygame, sys, random
from pygame.locals import *
from spritesheet import spritesheet
from math import * 
#import pygame.math
import math 


'''
things to be done: 
-get it to properly follow you. 
-make a delay when its following you
-

'''
class Shapes:

	def __init__(self,center,map,surfaceRect,imageMap,filename):		

		self.center = center
		self.objs = {}
		self.names = map.keys()
		self.origSurfaceRect = surfaceRect
		#print "names is: ",self.names
		
		for name in self.names:
			tup = map[name] 
			point1 = tup[0]
			point2 = tup[1]
			#(self,center,pointA,pointB,surfaceRect,imageRect,sideToRemove,filename)
			self.objs[name] = Shape(center,point1,point2,surfaceRect,imageMap[name],"top",filename)
		
	def getShape(self,num):
		temp = self.objs[num]
		return temp
		
	def getImage(self,num):
		temp = self.objs[num]
		return temp.getImage()
		
	def getNames(self):
		return self.names
		
	def getX(self):
		return self.center[0]
		
	def getY(self):
		return self.center[1]
		
	def getCenter(self,num):
		
		temp = self.objs[num]
		tempRect = temp.getImageRect()

		pointX =  self.center[0] - (tempRect.width/2)
		pointY =  self.center[1] - (tempRect.width/2)
		return (pointX,pointY)
		
	
		


class Shape:

	def __init__(self,center,pointA,pointB,surfaceRect,imageRect,sideToRemove,filename):
	
		self.filename = filename
		self.imageRect = pygame.Rect(imageRect)
		spriteSheetImage = spritesheet(filename)
		self.image = spriteSheetImage.image_at(imageRect)
		width = 1
		closed = True
		self.tup = (center,pointA,pointB)
		self.colorA = Color("black")
		
		#self.points = [self.transCenter(center),self.transPointA(pointA),self.transPointB(pointB)]
		#self.surfaceRect = pygame.Rect(0,0,surfaceRect.width,surfaceRect.height)
		#print "surfaceRect.width is: ",surfaceRect.width
		#print "surfaceRect.height is: ",surfaceRect.height
		
		#self.surface = pygame.Surface((surfaceRect.width,surfaceRect.height))
		self.surface = pygame.Surface(self.tranSurfaceRect(center,pointA,pointB))
		self.surface.fill(Color("white"))
		self.surfaceRect = self.surface.get_rect()
		
		tempCenter = self.convertPoint(center,pointA,pointB,center)
		tempPointA = self.convertPoint(center,pointA,pointB,pointA)
		tempPointB = self.convertPoint(center,pointA,pointB,pointB)	
		
		valX = self.smallestX(center,pointA,pointB)
		valY = self.smallestY(center,pointA,pointB)
		self.transLocVar = (valX,valY) 
		
		pygame.draw.lines(
		self.surface,
		Color("black"),
		closed,
		[tempCenter,tempPointA,tempPointB],
		width
		)
		
		
		# print "the surface width is: ",self.surface.get_width()
		# print "the surface height is: ",self.surface.get_height()	

		# print "center is: ",tempCenter
		# print "pointA is: ",tempPointA
		# print "pointB is: ",tempPointB
		
		self.makeSheet3()
		#self.removeSide("top") # starts at the top and goes down (0 to height) 
		self.removeSide(sideToRemove) #starts at the bottom (height) and goes to zero 
		
	def tranSurfaceRect(self,center,point1,point2):
		width = self.figureOutWidth(center,point1,point2)
		height = self.figureOutHeight(center,point1,point2)
		
		tup = (width,height)
		return tup
		
	def transLoc(self,tup):
		valX = tup[0] - self.transLocVar[0]
		valY = tup[1] - self.transLocVar[1]
		return (valX,valY)

	def figureOutWidth(self,center,point1,point2):
		buffer = 1
		num1 = self.smallestX(center,point1,point2)
		num2 = self.biggestX(center,point1,point2)
		num3 = (num2 + buffer) - (num1 - buffer)
		return num3		
		
			
	def figureOutHeight(self,center,point1,point2):	
		buffer = 1
		num1 = self.smallestY(center,point1,point2)
		num2 = self.biggestY(center,point1,point2)
		num3 = (num2 + buffer) - (num1 - buffer)
		return num3		
		
	def biggestY(self,center,point1,point2):	
		num1 = self.highest(center[1],point1[1])
		num2 = self.highest(num1,point2[1])
		return num2 
		
		
	def biggestX(self,center,point1,point2):
		buffer = 1
		num1 = self.highest(center[0],point1[0])
		num2 = self.highest(num1,point2[0])
		return num2
		
	
	def smallestY(self,center,point1,point2):	
		num1 = self.lowest(center[1],point1[1])
		num2 = self.lowest(num1,point2[1])
		return num2 
		
		
	def smallestX(self,center,point1,point2):
		num1 = self.lowest(center[0],point1[0])
		num2 = self.lowest(num1,point2[0])
		return num2

			
	def highest(self,num1,num2):
		
		if num1 >= num2:
			return num1
		else:#otherwise, num2 is bigger
			return num2

	def lowest(self,num1,num2):
	
		if num1 <= num2:
			return num1
		else:#otherwise, num2 is smaller
			return num2
			
		
	def convertPoint(self,center,point1,point2,pointToConvert):
		num1 = pointToConvert[0] - self.smallestX(center,point1,point2)
		num2 = pointToConvert[1] - self.smallestY(center,point1,point2)
		tup = (num1,num2)
		return tup 
		
		
	def getShape(self):
		return self.tup 
		
	def getImage(self):
		return self.image
		
	def getImageRect(self):
		return self.imageRect
		
	def getSurface(self):
		return self.surface
		
	def getKeyPoint(self):
		return ################################################################
		
	def getCenter(self):
		return self.center
		
	def makeSheet(self):
		self.array = []
		tempArray = []
		seenBlack = False
		opTempArray = [] #opposit temp Array values
		for x in range(0,self.surfaceRect.width-1):
		
			if tempArray != None:
				self.array.append(tempArray)
				tempArray = []

			for y in range(0,self.surfaceRect.height-1):
				
				if self.surface.get_at((x,y)) == Color("white"):# and seenBlack == True:
					seenBlack = False	
					
				if self.surface.get_at((x,y)) == Color("black"):# and seenBlack == False:
					seenBlack = True
				
				if seenBlack == True:
					tempArray.append('T')
				else:
					tempArray.append('q')
		
		self.fillShape()
		
				
		
	def fillShape(self):
	
		tempArray = self.array
		start = False
		end = False
		y1 = 0
		y2 = 0
		for x in range(1,self.surfaceRect.width -1):
			start = False

			for y in range(1,self.surfaceRect.height - 1):
			
				if start == True and self.array[x][y] == 'T':
					y2 = y
					break
					
				if self.array[x][y] == 'T':
					start = True
					y1 = y
					
			# if y1 != 0 and y2 != 0:	
				# for i in range(y1,y2):
					# print "self.array[",x,"][",i,"] = 'T'"
					# self.array[x][i] = 'T'
			
			y1 = 0
			y2 = 0
######################################################
					
					
	#GOOD ONE!
	def makeSheet3(self):
		self.array = []
		tempArray = []
		seenBlack = False
		seen1 = False
		seen2 = False
		point1 = 0
		point2 = 0
		
		# print "222 width of surface is: ", self.surface.get_width()
		# print "222 height of surface is: ", self.surface.get_height()
		
		opTempArray = [] #opposit temp Array values
		for x in range(0,self.surfaceRect.width):
		
			if tempArray != None:
				self.array.append(tempArray)
				tempArray = []
				opTempArray = []
			
			seen1 = False
			seen2 = False
			point1 = 0
			point2 = 0
			tempArray = []
			opTempArray = []
			for y in range(0,self.surfaceRect.height):
				
				#print "x: ",x," y: ",y
				if self.surface.get_at((x,y)) == Color("white"):
					seenBlack = False	
					
				if self.surface.get_at((x,y)) == Color("black") and seen1 == True:
					seenBlack = True	
					point2 = y
					tempArray = self.change(tempArray,opTempArray,point1,point2)
					
				if self.surface.get_at((x,y)) == Color("black"):
					seenBlack = True
					seen1 = True
					point1 = y
				
				if seenBlack == True:
					tempArray.append('T')
					opTempArray.append('T')
				else:
					tempArray.append('q')
					
					if seen1 == True:
						opTempArray.append('T')
					else:
						opTempArray.append('q')
						
						
						
						
	def change(self,tup1,tup2,point1,point2):	
		if len(tup1) != len(tup2):
			print "fuckup! tup1 is: ",len(tup1)," and tup2 is: ",len(tup2)
		
		#print "tup1 before: ",tup1
		for i in range(point1,point2):
			tup1[i] = tup2[i]
		
		#print "tup1 after: ",tup1
		return tup1
		
		
#####################################################
	# def makeSheet2(self):
		# self.array = []
		# tempArray = []
		# seenBlack = False
		# loc1 = 0
		# loc2 = 0
		# seen1 = False
		# seen2 = False
		# opTempArray = [] #opposit temp Array values (maybe) 
		# for x in range(0,self.surfaceRect.width-1):
		
			# if tempArray != None:
				# self.array.append(tempArray)
				# tempArray = []

			# for y in range(0,self.surfaceRect.height-1):
				
				# if self.surface.get_at((x,y)) == Color("white"):
					# seenBlack = False	
					
				# if self.surface.get_at((x,y)) == Color("black"):
					# seenBlack = True
					
					# if seen1 == True:
						# seen2 = True
						# loc2 = y
					
					# if seen1 == False:
						# seen1 = True
						# loc1 = y
				
				
				#print "tempArray is: ",tempArray
				# if seenBlack == True:
					# tempArray.append('T')
					#tempArray[len(tempArray):] = 'T'
				# else:
					# tempArray.append('q')
				
				# if seen1 and seen2:
					# tempArray = self.reverse(tempArray,loc1,loc2)
					# seen1 = False
					# seen2 = False
					# loc1 = 0
					# loc2 = 0
					
			# self.array.append(tempArray)
			# tempArray = []
			
	# def reverse(self,tup,start,end):
		#print "after tup is: ",tup
		# print "start is: ",start
		# print "end is: ",end
		# for num in range(start,end):
			# tup[num] = 'T'
		#print "after tup is: ",tup
		# return tup
		
		
	def removeSide(self,side):
		#print "self.surfaceRect.height is: ",self.surfaceRect.height
		num = 1
		
		newLet = 'C'
		
		if side == "top":
			for x in range(1,self.surfaceRect.width - 1):
				for y in range(1,self.surfaceRect.height - 1):
					if self.array[x][y] == 'T':
						self.array[x][y] = newLet
						break
		
		if side == "bottom":
			#print "right here" 
			for x in range(1,self.surfaceRect.width - 1):
				for y in range(self.surfaceRect.height - 2,0,-1):
					#print "x is: ",x, "y is: ",y
					if self.array[x][y] == 'T':
						self.array[x][y] = newLet
						break
						
		
		if side == "left":
			for y in range(1,self.surfaceRect.height - 1):
				for x in range(1,self.surfaceRect.width - 1):
					if self.array[x][y] == 'T':
						self.array[x][y] = newLet
						break
						
		if side == "right":
			for y in range(self.surfaceRect.height - 2,1,-1):
				for x in range(self.surfaceRect.width - 2,1,-1):
					# print "x is: ", x
					# print "y is: ", y
					if self.array[x][y] == 'T':
						self.array[x][y] = newLet
						break			
						

						
		if side != "bottom" and side != "top" and side != "left" and side != "right":
				print "accepted input values:"
				print "top"
				print "bottom"
			
	def contains(self,person):
		personRect = person.getRect()
		newLoc = self.transLoc(personRect.center)
		x = int(newLoc[0])
		y = int(newLoc[1])
		# x = int(x)
		# y = int(y)
		

		
		# print "surface width: ", len(self.array)
		# tempVar = self.array[x]
		# print "blah: ", tempVar
		# print "surface height: ", len(tempVar)
		
		if x <= 0 or x >= self.surface.get_width() or y <= 0 or y >= self.surface.get_height():
			return False
		
		else: #try putting all the if statments below this 'else' statement, actually inside this else statement
		
			# print "personX is: ",x
			# print "personY is: ",y
			
			if self.array[x][y] == 'T':
				return True
			
			#I want to test that this is all working properly.
			#which is why I am using a 2nd if rather than an else
			
			if self.array[x][y] == 'F':
				return False
				
			# if self.array[x][y] == None:
				# return None
			
	def getColor(self):
		return self.colorA
		
	def setColor(self,color):
		self.colorA = Color(color)
		
	def pointList(self):
		#return self.points
		return self.tup
		
	def printArray(self):
		for x1 in self.array:
			print""
			for y2 in x1:
				print y2," ",
				
				
	def printArray2(self):
		count = 0
		print "size of x is: ", len(self.array)
		print "size of y is: ", len(self.array[1])
		test1 = "  "
		print test1,
		for x2 in range(len(self.array[1])):
			if x2 <= 9:
				print x2,"", 
			if x2 >= 10:
				print x2, 
		
		
		for x in range(len(self.array)):
		
			for y in range(len(self.array[x])):
			
				if y == 0 and x <= 9:
					print " ",x," ",	
					
				if y == 0 and x >= 10:
					print x," ",
			
				print self.array[x][y]," "
		
			print ""
			
			
	#GOOD ONE!
	def printArray3(self):
	
		count = 0
		# print "size of x is: ", len(self.array)
		# print "size of y is: ", len(self.array[1])
		# test1 = "  "
		# print test1,
		for x2 in range(len(self.array)):
			if x2 <= 9:
				print x2,"", 
			if x2 >= 10:
				print x2, 
				
		print ""
		
		num = 1
		for y in range(1,len(self.array[num]) - 1):
		
			for x in range(1,len(self.array)-1):
			
				if y == 0 and x <= 9:
					print " ",x," ",	
					
				if y == 0 and x >= 10:
					print x," ",
			
				# print "x is: ",x
				# print "y is: ",y
				print self.array[x][y]," ",
				
			num +=1
		
			print ""
		
		print "number of columns: ",len(self.array)
		print "number of rows: ",len(self.array[num])
					
					
		
	
		
	