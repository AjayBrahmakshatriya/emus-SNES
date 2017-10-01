import pygame
import numpy

colors = [0x7C7C7C, 0x0000FC, 0x0000BC, 0x4428BC, 0x940084, 0xA80020, 0xA81000, 0x881400, 0x503000, 0x007800, 0x006800, 0x005800, 0x004058, 0x000000, 0x000000, 0x000000, 0xBCBCBC, 0x0078F8, 0x0058F8, 0x6844FC, 0xD800CC, 0xE40058, 0xF83800, 0xE45C10, 0xAC7C00, 0x00B800, 0x00A800, 0x00A844, 0x008888, 0x000000, 0x000000, 0x000000, 0xF8F8F8, 0x3CBCFC, 0x6888FC, 0x9878F8, 0xF878F8, 0xF85898, 0xF87858, 0xFCA044, 0xF8B800, 0xB8F818, 0x58D854, 0x58F898, 0x00E8D8, 0x787878, 0x000000, 0x000000, 0xFCFCFC, 0xA4E4FC, 0xB8B8F8, 0xD8B8F8, 0xF8B8F8, 0xF8A4C0, 0xF0D0B0, 0xFCE0A8, 0xF8D878, 0xD8F878, 0xB8F8B8, 0xB8F8D8, 0x00FCFC, 0xF8D8F8, 0x000000, 0x000000]
width = 256
height = 240

class NES_display:
	def __init__(self):
		self.screen = pygame.display.set_mode((width, height))
	def render(self):
		pygame.display.flip()
	def process_frame(self):
		result = numpy.zeros([width,height, 3], dtype=numpy.uint8)
		f=open("temp_file.txt")
		buffer = f.read(256*480)
		f.close()
		offset = 0
		for i in range(height):
			for j in range(width):
				color = colors[ord(buffer[offset])]
				offset+=1	
				result[j,i,0] = (color >> 16)  
				result[j,i,1] = (color >> 8) % 0x100
				result[j,i,2] = (color >> 0) % 0x100
				
		surf = pygame.surfarray.make_surface(result)
		self.screen.blit(surf, (0, 0))
		
	def start_render(self):
		running = True
		while(running):
			self.process_frame()
			self.render()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
			        	running = False
if __name__== "__main__":
	game1 = NES_display()
	game1.start_render()
