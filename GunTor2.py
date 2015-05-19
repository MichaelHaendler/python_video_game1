
# import sys
# import pygame
# from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
# import spritesheet
# import pygame, sys, random
# from pygame.locals import *
from GunImage import GunImage
from sprite_strip_anim import SpriteStripAnim

class GunTor:

	def __init__(self,filename,listTupImage,listTupShape,square,surface,locX = 90,locY = 90):

		self.default_loc = 0
		self.fakeSurface = surface
		self.area = square
		self.x = locX
		self.filename = filename
		self.y = locY
		self.firedRound = []
		self.map = {}
		self.gunTorObjs = []
		self.count = 0
		self.tempStrips = []
		self.firedShots = []
		
		for tup in listTupImage:
		
		#'gunImage(listTupImage[self.count]' holds the squares used to get image and se it's boundaries
		#the init parameters for GunImage are: (self,rect,filename,shapeTup,name)
			self.gunTorObjs.append(
			GunImage(listTupImage[self.count],# this holds the squares used to get image and se it's boundaries
			filename,
			listTupShape[self.count], # this is the triangle associated with it
			self.count) # it's "name" 
			)
			
			tempGun = GunImage(listTupImage[self.count],filename,listTupShape[self.count],self.count)
			self.map[self.count] = tempGun
			self.count += 1
			
		self.curGun = self.gunTorObjs[self.default_loc] #gives you a default gun
		
	def setDefaultGun(self,num):
		self.default_loc = num
		
	def getX(self):
		return self.x
		
	def setX(self,x):
		self.x = x
		
	def getY(self):
		return self.y
		
	def setY(self,y):
		self.y = y
		
	def getRect(self):
		return self.Rect
		
		#checks whether or not a person is in range. 
		#If so, the person is aimed at, then fire upon 
		
		
	def setArea(self,square):
		self.area = square
		
	def getCircle(self):
		return self.area 
		
	#MEAT OF CODE!!!!
	
	'''
	#needs to see if char is in there. 
	
	#if the character is within the general square, start tracking
	
	#if the character is within the second square, fire. 
	'''
	def scanAreaAndFire(self,person):
		#print "HELLLLOOOO22222"
		for gunTorObj in self.gunTorObjs:
			#print "HELLLLOOOO"
		
			#see if it's within one of the triangles
			if gunTorObj.containsPerson(person.getRect() , self.fakeSurface.size) == True:	
				
				#check if we're current looking at the character via the barrel of the gun.
				if self.curGun.getCountName() == gunTorObj.getCountName():
					#if we are, then fire. 
					self.shoot(person.getRect())
				
				#if it's within one of the triangles but we're NOT current looking at the character via the barrel of the gun:
				else:
					#turn gun torrent (by one image at a time) towards the person
					nextGun = swivelTur(self.curGun,gunTorObj) 
					#set this as our current gun
					self.curGun = nextGun
					#and put the image into tempStrips
					self.tempStrips.append(self.curGun.getImage(),self.curGun.getX(),self.curGun.getY())
						
						
		#note: updateShots is outside of if statement, b/c all currently flying shots need to be
		#updated, regardless of whether or not a shot was fired
		self.updateShots(person)
		
		#next, append shot to list of things to be displayed (don't display that went off the screen or hit the person) 
		for shot in self.firedShots:
			self.tempStrips.append(pygame.Rect(shot.getBullet()))
			

					
	#turrent direction				
	def swivelTur(self,fromGun,toGun):	
		
		val1 = clockWise(fromGun,toGun)
		val2 = counterClockWise(fromGun,toGun)
		array = []
		if val1 <= val2:
			num = fromGun.getCountName() +1
			if num == len(self.map): #aka  8
				return self.map[0]
			else:
				return self.map[fromGun.getCountName() +1]
				
		if val2 <= val1: #could have used an else, but this is easier to understand
			num2 = fromGun.getCountName() - 1
			if num2 == -1:
				return self.map[len(self.map) - 1] 
			else:
				return self.map[num]
				
				
				
		
	def clockWise(self,fromGun,toGun):
		diff = fromGun.getCountName() - toGun.getCountName()
		diff = math.fabs(diff)
		return diff
	
	def counterClockWise(self,fromGun,toGun):
		num = (len(self.gunTorObjs) + fromGun.getCountName()) - toGun.getCountName
		return num
	
	
	#this method makes a bullet, fires it, and sends it on its merry way. 
	def shoot(self,personsRect):
		x = 0
		y = 1
		
		#centerOfBarrel needs to be set for each gun via setCenterOfBarrel
		
		#note: "comes_out_of_this_barrel" is very important, as it is the point
		#that is used to define the line aka trajectory between the bullet
		#coming out of, and where it is going. 
		comes_out_of_this_barrel = self.curGun.centerOfBarrel()
		bullet = Bullet(comes_out_of_this_barrel)
		
		slopeY = personsRect.center(y) - curGun.getRect().midLeft(y)
		slopeX = personsRect.center(x) - curGun.getRect().midLeft(x)
		
		bullet.setIncXY(slopeY,slopeX)
		firedRound.append(bullet)
		
		
	#updates the situation for the various bullets that have been fired. 
	#note: requires fakeSurface to see whether or not the bullet is still on the screen. 
	def updateShots(self,person):
		x = 0
		y = 1
		screenBufferVal = 10
		surfaceTup = self.fakeSurface.size
		
		for bullet in self.firedRound:
		
			#see if the bullet hit the person.
			hit = bullet.contains(person.getRect())
			
			#if it did, deduct one from the player's health 
			if hit == True:
				deduct_one_from_health = -1
				person.changeHealth(deduct_one_from_health)	
				
			#otherwise, increment it's location. 
			else:
				bullet.incXY()
				bulletLoc = bullet.getLoc()
				
			#if the bullet is still well within the seen screen and you didn't hit anyone, put it into the list of bullets to be displayed. 
			numX = surfaceTup[x] - screenBufferVal
			numY = surfaceTup[y] - screenBufferVal
			if bulletLoc[x] < numX and bulletLoc[x] > screenBufferVal and bulletLoc[y] < numY and bulletLoc[y] > screenBufferVal and hit == False:
				self.firedRound.append(bullet)
			#else do nothing. it shouldn't be in there since it's gone outside of the screen. 
		
		

		
	def getImages(self):
		return self.tempStrips		
		
		
	# def image(self):
		# return self.tempStrips.next()
		
		
	#returns a list of the gun torrent images to be shown
	# def moveAnim(self,fromGun,toGun):	
		
		# val1 = clockWise(fromGun,toGun)
		# val2 = counterClockWise(fromGun,toGun)
		# array = []
		# if val1 <= val2:
			# for num in range(fromGun.getCountName() +1,toGun.getCountName()):
				# array.append(self.map[num].getRect())
		# else: # if val2 (aka counter clockwise) is the way to go...
			# start = fromGun.getCountName() - 1
			# end = 0 
			# for num3 in range(start,end,-1):
				# array.append(self.map[num3])
				# if num3 == 0:
					# start = len(self.gunObjs) - 1
					# end = toGun.getCountName()
					
					
					
#####################STUFF THAT YOU CAN PASTE BACK INTO RUN IF YOU WANT (for rotating and for getting the gun)

    # tempRect = trit.getSurface().get_rect()
    # tempCent = tempRect.center
    # x2 = char.getX()
    # x1 = tempCent[0]
    # y2 = char.getY()
    # y1 = tempCent[1]
    ## deltaX = x2 - x1
    ## deltaY = y2 - y1
    # deltaX = x2 - x1
    # deltaY = y1 - y2
    # aids = math.atan2(deltaY, deltaX) * 180 / math.pi # aids == angleInDegrees
	
    # tempVar = pygame.transform.rotate(trit.getSurface(), aids)
    # surface.blit(tempVar,(50,50)) #helpful for debugging Shape in SingleTri
	
    # shapeNames = tris.getNames()
	
    # for name in shapeNames:
        # tempShape = tris.getShape(name)
        # if tempShape.contains(char):
            # tempShape.setColor("green")
            # surface.blit(tempShape.getImage(),tris.getCenter(name))
  
        # else:
            # tempShape.setColor("black")
        # pygame.draw.lines(surface,tempShape.getColor(),True,tempShape.pointList(),width)