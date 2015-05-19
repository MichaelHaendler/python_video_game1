

class GunTor:

	def __init__(self,filename,listTupImage,listTupShape,locX = 90,locY = 90):

		'''
		self.up = gunImage(listTupImage[0],listTupShape[0])
		self.upperRight = gunImage(listTupImage[1],listTupShape[1])
		self.right = gunImage(listTupImage[2],listTupShape[2])
		self.lowerRight = gunImage(listTupImage[3],listTupShape[3])
		self.down = gunImage(listTupImage[4],listTupShape[4])
		self.lowerLeft = gunImage(listTupImage[5],listTupShape[5])
		self.left = gunImage(listTupImage[6],listTupShape[6])
		self.upperLeft = gunImage(listTupImage[7],listTupShape[7])
		'''
		self.x = locX
		self.filename = filename
		self.y = locY
		self.firedRound = []
		self.map = {}
		self.gunTorObjs = []
		self.count = 0
		self.tempStrip = []
		for tup in listTupImage:
		
			self.gunTorObjs.append(
			gunImage(listTupImage[self.count],# this holds the squares used to get image and se it's boundaries
			filename,
			listTupShape[self.count], # this is the triangle associated with it
			self.count) # it's "name" 
			)
			
			self.map[self.count] = gunImage(listTupImage[self.count],filename,listTupShape[self.count],self.count)
			self.count += 1
			
		self.curGun = self.gunTorObjs[0] #gives you a default gun
		
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
		
	#MEAT OF CODE!!!!
	def runCheck(self,person,fakeSurface = (200,200)):
		FPS = 120
		speed = 14
		frames = FPS / speed
		for gunTorObj in self.gunTorObjs:
			if gunTorObj.containsPerson(person.getRect(),fakeSurface) == True:
				if self.curGun.getCountName() == gunTorObj.getCountName():
					self.curGun.shoot(person.getRect())
					tupOfShots = self.updateShots(person)
					
					for shot in tupOfShots:
						self.tempStrip.append(shot)
					
					animStrip = SpriteStripAnim(self.filename, self.curGun.getRect(),1,-1, False, frames)
					
					for image in animStrip: 
						self.tempStrip.append(image)
					
				else:
					tempTup = self.moveAnim(self.curnGun,gunTorObj) 
					self.tempStrip = SpriteStripAnim(self.filename, tempTup, len(tempTup),-1, False, frames)
					# return tempTup
			# else:
				# return self.curGun.getImage()
				
	def moveAnim(self,fromGun,toGun):	
		
		val1 = clockWise(fromGun,toGun)
		val2 = counterClockWise(fromGun,toGun)
		array = []
		if val1 <= val2:
			for num in range(fromGun.getCountName() +1,toGun.getCountName()):
				array.append(self.map[num].getRect())
		else: # if val2 (aka counter clockwise) is the way to go...
			start = fromGun.getCountName() - 1
			end = 0 
			for num3 in range(start,end,-1):
				array.append(self.map[num3])
				if num3 == 0:
					start = len(self.gunObjs) - 1
					end = toGun.getCountName()
				
				
		
	def clockWise(self,fromGun,toGun):
		diff = fromGun.getCountName() - toGun.getCountName()
		diff = math.fabs(diff)
		return diff
	
	def counterClockWise(self,fromGun,toGun):
		num = (len(self.gunTorObjs) + fromGun.getCountName()) - toGun.getCountName
		return num
	
	
	def shoot(self,personsRect,fakeSurface):
		x = 0
		y = 1
		comes_out_of_this_barrel = self.curGun.centerOfBarrel()
		bullet = Bullet(comes_out_of_this_barrel)
		
		slopeY = personsRect.center(y) - curGun.getRect().midLeft(y)
		slopeX = personsRect.center(x) - curGun.getRect().midLeft(x)
		
		bullet.setIncXY(slopeY,slopeX)
		firedRound.append(bullet)
		
	def updateShots(self,person,fakeSurface):
		x = 0
		y = 1
		screenBufferVal = 20
		surfaceTup = fakeSurface.get_size()
		for bullet in self.firedRound:
			if bullet.contains(person.getRect()):
				deduct_one_from_health = -1
				person.changeHealth(deduct_one_from_health)	
				bullet.incXY()
				bulletLoc = bullet.getLoc()
				
			if bulletLoc[x] < surfaceTup[x] - screenBufferVal and bulletLoc[y] < surfaceTup[y] - screenBufferVal:
				self.firedRound.append(bullet)
			#else do nothing. it shouldn't be in there since it's gone outside of the screen. 
		
		gunShots = []
		for shot in self.firedRound:	
			gunShots = pygame.rect(shot.getX(),shot.getY(),shot.getBulletWidth(),shot.getBulletHeight())
			
		return gunShots
		
	def image(self):
		return self.tempStrips.next()

class bullet:

	def __init__(self,tup):
		self.loc = tup
		self.speed = 6
		#NEED TO DEAL WITH NEGATIVE VALUES ON THE GRAPH
		
	def setIncXY(self,up,over):
		slowSpeed = 1 #/3  undo the '#' in front of the 3 in order to slow things down. 
		self.upY = up  * slowSpeed
		self.overX = over * slowSpeed
		self.rect = (0,0,4,4)
		self.rect.fill(color('red'))
		
	def incXY(self):
		x = 0
		y = 1
		self.loc[x] += self.overX
		self.loc[y] += self.upY
		self.rect.left = self.loc[x]
		self.rect.top = self.loc[y]

	def getLoc(self):
		return self.loc
		
	def getX(self):
		return self.loc[0]
		
	def getY(self):
		return self.loc[1]
		
	def getBulletWidth(self):
		return self.rect.width
		
	def getBulletHeight(self):
		return self.rect.height
		
class gunImage:

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
		temp = SpriteStripAnim(filename, rect, count, colorkey, loop, frames)
		self.image = temp.next(0)
		self.filename = filename
		
	def getImage(self):
		return self.image
		
	def shape_And_Filename(self):
		return (self.shape,self.filename)
		
	def getCountName(self):
		return self.countName # 0 to 7 
		
	def containsPerson(personRect, fakeSurface = (0,0)):
		if fakeSurface == (0,0):
			fakeSurface = pygame.display.set_mode((400,500))
		tempShape = pygame.draw.lines(fakeSurface,-1,True, self.shape, width=1)
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
		