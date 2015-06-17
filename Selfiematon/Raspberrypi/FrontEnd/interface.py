import pygame
import glob
import random

class interface:

	rute = "~PycharmProyejects/Adeter/Selfiematon/Raspberrypi/"
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
		self.pantalla.set_alpha(clarity)


		#Añadir directorio.
		self.place = place

	def loadAllImages(self):

		for d in self.directories:
			#Imagenes de cada directorio
			listImages = glob.glob(self.Rute + 'places/'+ self.place+'/'+d+'/*.'+self.imgExtension)

			#Inicializamos la lista auxiliar
			imgListAux=[]

			for img in listImages:
				imgAux = pygame.image.load(img).convert() 							#Carga una imagen de la lista
				imgAux = pygame.transform.scale(imgAux,(self.width,self.high))   	#Escalamos la imagen para que entre en el monitor
				imgListAux.append(imgAux)

			#Añadimos la lista con las imágenes
			self.allImages[d] = imgListAux


	def getImage(self,nameDirectory,index):

		#Comprobamos si está el nombre del directorio
		if self.allImages.has_key(nameDirectory):
			imgListAux = self.allImages[nameDirectory]
			#Comprobamos si se ha salido del index
			if index < len(imgListAux):
				return [imgListAux[index],0]
			else:
				return ["index: Fuera de rango",1]
		else:
			return ["nameDirectory: No se encuentra el directorio ",2]

	def getImage(self,nameDirectory):

		if self.allImages.has_key(nameDirectory):
			return [random.choice(self.allImages[nameDirectory]),0]
		else:
			return ["nameDirectory: No se encuentra el directorio ",2]


	def getLenImageDirectory(self,nameDirectory):
		if self.allImages.has_key(nameDirectory):
			return len(self.allImages[nameDirectory])
		else:
			return ["nameDirectory: No se encuentra el directorio ",2]