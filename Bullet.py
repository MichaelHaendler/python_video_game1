



class Bullet:

	def __init__(self,tup):
		self.speed = 6
		self.upY = 1
		self.overX = 1
		self.rect = (tup[0],tup[1],4,4)
		self.rect.fill(color('red'))
		#NEED TO DEAL WITH NEGATIVE VALUES ON THE GRAPH
		
	def setIncXY(self,incX,incY):
	
		#incX aka up (a la slope) and incY aka over
		num = 1
		slowSpeed = 1/num 
		self.upY = incX  * slowSpeed
		self.overX = incY * slowSpeed

		
	def incXY(self):
		self.rect.left += self.overX
		self.rect.top += self.upY

	def getLoc(self):
		return self.rect.topLeft
		
	def getX(self):
		return self.rect.left
		
	def getY(self):
		return self.rect.top
		
	def getWidth(self):
		return self.rect.width
		
	def getHeight(self):
		return self.rect.height
		
	def getBullet(self):
		return self.rect
		
	def getImage(self):
		return self.rect