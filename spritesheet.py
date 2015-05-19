# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)
 
import pygame
 
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message
			
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
		
		#take the area from rect, and post it at loc 0,0 on the surface/sheet. 
		#without this, image does not get put on surface. 
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
				
				
				
	 #pygame.RLEACCEL in the set_colorkey() method instructs pygame 
	 #to process [compile] the resulting image taking into account 
	 #the transparency color so that it will be blitted faster in the future.
	 
	 #google Surface.set_colorkey to understand this. 
	 #basically it gets colorkey, and then uses RLEACCEL to make it go faster
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
		
		
		
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
	var = []
	for rect in rects:
		var.append(self.image_at(rect, colorkey))
	return var
		
        #return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rects, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
	#tups2 = []
	#for x in range(image_count):
		#tups2.append(pygame.Rect(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]))
	#colorkey=(255,255,255)
	#var3 = [(70,40,30,40),(40, 40, 30, 40),(5,40,30,40)]
	var2 = []
	for j in range(len(rects)):
		#print "at ",j," we have ", rects[j]," 222222222222222"
		var2.append(self.image_at(rects[j], colorkey))
	return var2
	
	#var = []
	#for j in range(image_count):
	#	rect = pygame.Rect(rect[0] + rect[2] * j, rect[1], rect[2], rect[3])
	#	print rect
	#	#print"rect[2] is", rect[2]
	#	var.append(self.image_at(rect, colorkey))
	#return var
	
	#tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
	#return self.images_at(tups, colorkey)
	
	