#!/usr/bin/python

#Clase que implementa todas las funciones para conseguir un 
#seguimiento de las capturas de imagenes 

import glob
import os


class LogFotos:
	strNumeroFotos='/home/pi/SelfieMaton/BackEnd/LOG/NumeroFotos.txt'
	strNombreFotos='/home/pi/SelfieMaton/BackEnd/LOG/NombreFotos.txt'
	strFotoRealizada='foto.jpg'
	intNumeroFotos=0
	listTipoFotos=['ForoEmprende','Parejas','Grupos','Solo']
	intTipoFotos=0
	strTipoFotos='ForoEmprende'
	intFotosCapturadas=0

	def __init__(self):
		#Obtener el numero de fotos hechas
		f = open(self.strNumeroFotos,'r')
		self.intNumeroFotos = int(f.read())
		f.close()
		
	def FuncIncrementarFoto(self):
		#Incrementar el numero de fotos
		self.intNumeroFotos += 1
		f = open(self.strNumeroFotos,'w')
		f.write(str(self.intNumeroFotos))
		f.close()
	def FuncNombrarFoto(self):
		self.strFotoRealizada = self.strTipoFotos+'_'+str(self.intNumeroFotos)

	def FuncCambiarTipo(self,tipo):	
		#Elegir el tipo de fotos realizada
		if tipo>0 and tipo<4:
			self.strTipoFotos = self.listTipoFotos[tipo]	

	def FuncGuardarFoto(self):
		#Guardar el nombre de la foto procesada
		f = open(self.strNombreFotos,'a')
		f.write(self.strFotoRealizada+'\n')
		f.close()

	def FuncProcesarImagen(self):
		self.FuncNombrarFoto()
		ListFotos = glob.glob("/home/pi/SelfieMaton/BackEnd/Captura/*.jpg")
		ListFotos2 = glob.glob("/home/pi/SelfieMaton/BackEnd/Imagenes/*.jpg")
		NumFotos = len(ListFotos)
		NumFotos2 = len(ListFotos2)
		if NumFotos > 0 and NumFotos2 == 0:
			os.system("mv "+ListFotos[0]+" /home/pi/SelfieMaton/BackEnd/Imagenes/"+self.strFotoRealizada+".jpg")

	def FuncSubirImagen(self):
		ListFotos=glob.glob("/home/pi/SelfieMaton/BackEnd/Imagenes/*.jpg")
		if len(ListFotos)>0:
#			if os.system('python Facebook.py /home/pi/SelfieMaton/BackEnd/Imagenes/'+self.strFotoRealizada+'.jpg') == False:
			if os.system("dropbox_uploader.sh upload "+"/home/pi/SelfieMaton/BackEnd/Imagenes/"+self.strFotoRealizada+".jpg /Public/IniciativaEmprendedora")==0:	
				#si se ha subido correctamente borramos
				os.system("rm /home/pi/SelfieMaton/BackEnd/Imagenes/*.*")
				print("Subida")
				self.FuncGuardarFoto()
				self.FuncIncrementarFoto()
			else:
				print("NoSobida")			
	
