import spritesheet
 
class SpriteStripAnim(object):
    """sprite strip animator
    
    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """
    def __init__(self, filename, rects, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim
        
        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.
        
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.
        
        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
		
        #print "SpriteStripAnim obviously likes my rect as it gives me ",rects
        self.images = ss.load_strip(rects, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
		
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
		
#The deal with self.f and self.i is that
#you iterate through the images using
#self.i. However, you need to know where
#to stop. You do this by knowing when
# self.f gets to zero. I suppose this could be changed
# so that it just uses zero. 

    def next(self,num = None):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
	#print"self.i is: ",self.i
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
			
        if num != None:
            image = self.images[num]            
        return image
		
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
		

    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y


	