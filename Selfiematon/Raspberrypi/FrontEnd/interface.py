import pygame
import glob
import random
import os
import time

class interface:

	rute = "/Users/RaulCE22/PycharmProjects/Adeter/Selfiematon/Raspberrypi/FrontEnd/"
	imgExtension = "jpg"
	directories = ["presentation","disclaimer","loading","thankyou"]
	allImages = {}

	def __init__(self,place,clarity,fullscreen):

		#Iniciamos pygame
		pygame.init()
		pygame.mouse.set_visible(False)

		#Tamaño de la pantalla donde se mostrara la interfaz
		info=pygame.display.Info()
		self.width = info.current_w
		self.high = info.current_h

		#Elegimos si queremos o no pantalla completa
		if fullscreen:
			self.screen = pygame.display.set_mode((self.width,self.high),pygame.FULLSCREEN)
		else:
			self.screen = pygame.display.set_mode((self.width,self.high))

		#Le introducimos el brillo. Esto dependera si el selfiematon se encuenta en zona abierta o cerrada.
		self.screen.set_alpha(clarity)


		#Añadir directorio.
		self.place = place

	def loadAllImages(self):

		for d in self.directories:
			#Imagenes de cada directorio
			listImages = glob.glob(self.rute + 'places/'+ self.place+'/'+d+'/*.'+self.imgExtension)
			#Inicializamos la lista auxiliar
			imgListAux=[]

			for img in listImages:
				imgAux = pygame.image.load(img).convert() 							#Carga una imagen de la lista
				imgAux = pygame.transform.scale(imgAux,(self.width,self.high))   	#Escalamos la imagen para que entre en el monitor
				imgListAux.append(imgAux)

			#Añadimos la lista con las imágenes
			self.allImages[d] = imgListAux


	def loadImage(self,nameDirectory,index):

		#Comprobamos si está el nombre del directorio
		if nameDirectory in self.allImages:
			imgListAux = self.allImages[nameDirectory]
			#Comprobamos si se ha salido del index
			if index < len(imgListAux):
				self.screen.blit(imgListAux[index],(0,0))
				pygame.display.flip()
				return True
			else:
				return False
		else:
			return False

	def loadImage(self,nameDirectory):

		if nameDirectory in self.allImages:
			imgAux = random.choice(self.allImages[nameDirectory])
			self.screen.blit(imgAux,(0,0))
			pygame.display.flip()

			return True
		else:
			return False

	def getLenImageDirectory(self,nameDirectory):
		if nameDirectory in self.allImages:
			return len(self.allImages[nameDirectory])
		else:
			return ["nameDirectory: No se encuentra el directorio ",2]

	def newPlace(self,name):

		print ("Creando carpetas...")


		d = 'mkdir places/'+name
		c = ['album','capture','log','logotype','presentation','disclaimer','loading','thankyou']

		os.system(d)
		for i in c:
			os.system(d+'/'+str(i))



I = interface("paniagua",128,False)


#I.newPlace("paniagua")
I.loadAllImages()
print (I.loadImage("presentation"))
time.sleep(3)

