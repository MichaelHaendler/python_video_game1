

import pygame
from pygame.locals import *#Color, KEYUP, K_ESCAPE, K_RETURN
from SingleTri import Shape

a = []
tempArray = []
for x in range(1,10):
	if tempArray != None:
		a.append(tempArray)
		tempArray = []
	for y in range(1,10):
		tempArray.append(x * y)
		

		
		
# for x1 in a:
	# print""
	# for y2 in x1:
		# if y2 <= 9:
			# print " ",y2," ",
		
		# else:
			# print y2," ",
			
# print""
# print""	
#over 3, down 0
# print a[3][0]

# n = None

# print "it is: ", n
		

# for y in range(10,1,-1):
	# print y," ",

heightt = 2
offsett = 1
#centert = [20,40]
centert = [150,200]
oct_xt = centert[0]
oct_yt = centert[1]
# point1t= (5,5)
# point2t = (5,25)
point1t = (116,115)
point2t = (184,115)

#rectt = pygame.Rect(0,0,26,45)
surface = pygame.display.set_mode((400,500))
#(self,center,pointA,pointB,surfaceRect,imageRect,filename)
tempRect = surface.get_rect()
#print "tempRect is: ",tempRect
#(self,center,pointA,pointB,surfaceRect,imageRect,sideToRemove,filename)


trit = Shape(centert,point1t,point2t,tempRect,(0,0,0,0),"right","tower.png")
trit.printArray3()


#(center,pointA,pointB,surfaceRect,imageRect,sideToRemove,filename):

