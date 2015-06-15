#!/usr/bin/python 

import pygame
import glob 
import os
import time, threading
import io
import picamera
from PIL import Image
import RPi.GPIO as GPIO

#Inicializa el interfaz
pygame.init()

#Obtiene parametros de la pantalla (Ancho,Alto)
info=pygame.display.Info() 
pygame.mouse.set_visible(False)
#Ruta

Ruta = '/home/pi/SelfieMaton/FrontEnd/'

#**************** DEFINICIONES  *******************

ANCHO = info.current_w
ALTO = info.current_h

print ANCHO
print ALTO
POS_PANTALLA = (ANCHO,ALTO)

im  = Image.open(Ruta+"Botones/Boton_Hacer_Foto.png")
(AN,AL) = im.size
POS_BOTON_FOTO = (ANCHO/2-AN/2,ALTO-AL)

im = Image.open(Ruta+"Botones/OK_2.png")
(AN,AL) = im.size
POS_BOTON_OK = (ANCHO-100-AN,ALTO-AL)

im = Image.open(Ruta+"Botones/NOK_2.png")
(AN,AL) = im.size
POS_BOTON_NOK = (100,ALTO-AL)

im = Image.open(Ruta+"Botones/CuentaAtras1.png")
(AN,AL) = im.size
POS_CUENTA_ATRAS = (ANCHO/2-AN/2,ALTO/2-AL/2)

im = Image.open(Ruta+"Intentos/1_intento.png")
(AN,AL) = im.size
POS_INTENTO = (0, ALTO-AL-20)

#im = Image.open(Ruta+"Botones/boton_aceptar.png")
#(AN,AL) = im.size
#POS_BOTON_ACEPTAR = (ANCHO/2-AN/2,ALTO/2-AL/2+2*AL)

#********************* funciones auxiliares **************************

#Temporizadores

#1- Presentacion
H1 = True
pulsadorListo = False

def Hecho1():
	global H1
	global pulsadorListo
	pulsadorListo = False
	H1 = True

#2- Cuenta atras
H2 = True
def Hecho2():
	global H2
	H2 = True

#3- Dissclaimer
H3 = True
def Hecho3():
	global H3
	H3 = True

#4- No pulsacion rapida
H4 = True
def Hecho4():
	global H4
	H4 = True



#********************* PULSADORES EXTERNOS **************************
GPIO.setmode(GPIO.BCM)

pulsadorSi = 17
pulsadorNo = 22
#leds=23
pulsadorListo = False

#GPIO.setup(leds, GPIO.OUT)
GPIO.setup(pulsadorSi, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pulsadorNo, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



#********************************************************************


#Leer pulsadores de pantalla

def LeerPulsadores(B_Av, B_Re, Est):
	global H4
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if B_Av.collidepoint(pos):
                                if H4:
                                        H4=False
                                        timer4 = threading.Timer(1,Hecho4)       # 3 Segundos (Se puede modificar)
                                        timer4.start()
                                        Est+=1
                                        print("Avanzar: "+str(Est))
                        if B_Re.collidepoint(pos):
                                if H4:
                                        H4=False
                                        timer5 = threading.Timer(1,Hecho4)
                                        timer5.start()
                                        Est=4
                                        print("Retroceder: "+str(Est))
        return Est


#****************** Parametros de inicializacion **********************

#Pantalla
pantalla = pygame.display.set_mode(POS_PANTALLA,pygame.FULLSCREEN) #pygame.FULLSCREEN ( pantalla completa )
pantalla.set_alpha(128)
#Botones
Boton_Foto = pygame.image.load(Ruta+"Botones/Boton_Hacer_Foto.png").convert_alpha()
B_Foto = pantalla.blit(Boton_Foto,POS_BOTON_FOTO)

#Se utiliza para que la funcion LeerPulsadores pueda tener como entrada solo un pulsador
Boton_Vacio = pygame.image.load(Ruta+"Botones/vacio.png").convert_alpha()
B_Vacio = pantalla.blit(Boton_Vacio,(0,0))	#Posicionar en pantalla

Boton_OK = pygame.image.load(Ruta+"Botones/OK_2.png").convert_alpha()
Boton_NOK = pygame.image.load(Ruta+"Botones/NOK_2.png").convert_alpha()


#Cuenta atras
Cuenta5 = pygame.image.load(Ruta+"Botones/CuentaAtras5.png").convert_alpha()
Cuenta4 = pygame.image.load(Ruta+"Botones/CuentaAtras4.png").convert_alpha()
Cuenta3 = pygame.image.load(Ruta+"Botones/CuentaAtras3.png").convert_alpha()
Cuenta2 = pygame.image.load(Ruta+"Botones/CuentaAtras2.png").convert_alpha()
Cuenta1 = pygame.image.load(Ruta+"Botones/CuentaAtras1.png").convert_alpha()

#Intentos

Intento1 = pygame.image.load(Ruta+"Intentos/1_intento.png")
Intento2 = pygame.image.load(Ruta+"Intentos/2_intento.png")
Intento3 = pygame.image.load(Ruta+"Intentos/3_intento.png")
Intentos = [Intento1,Intento2,Intento3]

#Dissclaimer
Dissclaimer = pygame.image.load(Ruta+"Dissclaimer/1_dissclaimer.jpg")
Dissclaimer = pygame.transform.scale(Dissclaimer,(ANCHO,ALTO))
Boton_Aceptar = pygame.image.load(Ruta+"Botones/boton_aceptar.png").convert_alpha()

#Cargando
Cargando1 = pygame.image.load(Ruta+"Cargando/2_cargar.jpg") 
Cargando1 = pygame.transform.scale(Cargando1,(ANCHO,ALTO))
Cargando2 = pygame.image.load(Ruta+"Cargando/3_cargar.jpg")
Cargando2 = pygame.transform.scale(Cargando2,(ANCHO,ALTO))
Cargando3 = pygame.image.load(Ruta+"Cargando/4_cargar.jpg")
Cargando3 = pygame.transform.scale(Cargando3,(ANCHO,ALTO))
Cargando4 = pygame.image.load(Ruta+"Cargando/5_cargar.jpg")
Cargando4 = pygame.transform.scale(Cargando4,(ANCHO,ALTO))

#Gracias
Gracias = pygame.image.load(Ruta+"Cargando/6_gracias.jpg")
Gracias = pygame.transform.scale(Gracias,(ANCHO,ALTO))

#Fondo
Fondo = pygame.image.load(Ruta+"Fondo/fondo.jpg")
Fondo = pygame.transform.scale(Fondo,(ANCHO,ALTO))

#Contador Imagenes
NumeroFotos = 0


#***************** Maquina de estados **********************


Est = 0
while True:
	time.sleep(0.01)
	if Est == 0:

		#leds
		#GPIO.output(leds,GPIO.HIGH)

		#Preparar Presentacion ( Las imagenes tienen que estar en la carpeta Imagenes )
		ListFotos = glob.glob(Ruta+"Imagenes/*.jpg")
		print ListFotos
		i=0

		#Inicio limite veces foto fallida
		FotoFallida=3
	
		Est+=1

	elif Est == 1:
		#Mostrar Presentacion		
		
		#Imagenes de fondo
		im = pygame.image.load(ListFotos[i]).convert() 	#Carga una imagen de la lista
		im = pygame.transform.scale(im,(ANCHO,ALTO))   	#Escalamos la imagen para que entre en el monitor
		pantalla.blit(im,(0,0))			       	#Posicionamos la imagen
		
                #Botones
                B_Foto = pantalla.blit(Boton_Foto,POS_BOTON_FOTO) 	#Poscionamos el boton de inicio

		#Tiempo para el cambio de imagen
		if H1:
			timer1 = threading.Timer(5,Hecho1)	# 3 Segundos (Se puede modificar)
			H1=False					# Cada 3 segundos se cambia una foto
			timer1.start()
			i+=1
			print i
			if i>=len(ListFotos):
				i=0

		#Actualizamos pantalla
		pygame.display.flip()

		#Leer los pulsadores ( Si se pulsa avanza al siguiente estado )
		#Est = LeerPulsadores(B_Foto, B_Vacio, Est)
		pulsadorListo=True
		while pulsadorListo:
			time.sleep(0.1)
			if GPIO.input(pulsadorSi)==1:
				Est+=1
				pulsadorListo = False										
	elif Est == 2:
		timer3 = threading.Timer(20,Hecho3)
		H3=False
		timer3.start()
		Est+=1

	elif Est == 3:
		#leds
		#GPIO.output(leds,GPIO.LOW)

		#Se agoto el tiempo de espera
		if H3:
			Est=0
		pantalla.blit(Fondo,(0,0))
		pantalla.blit(Dissclaimer,(0,0))
		#B_Aceptar = pantalla.blit(Boton_Aceptar,POS_BOTON_ACEPTAR)
		pygame.display.flip()
		#Est = LeerPulsadores(B_Aceptar,B_Vacio,Est)
		time.sleep(3)

		#leds
		#GPIO.output(leds,GPIO.HIGH)

		pulsadorListo=True
		while pulsadorListo:
			if GPIO.input(pulsadorNo)==1:
				Est=1
				pulsadorListo=False
				break
			if GPIO.input(pulsadorSi)==1:
				Est+=1
				pulsadorListo=False
				break		
				
	elif Est == 4:
		#Foto Fallida
		if FotoFallida==0:
			Est=7 	#Subir Foto
		else:		
			
			#leds
			#GPIO.output(leds,GPIO.LOW)

			#Preparar camara con la preview
			pantalla.blit(Fondo,(0,0))
			pygame.display.flip()
			camera = picamera.PiCamera()
			camera.resolution = (ANCHO,ALTO)
			camera.start_preview()
			camera.preview_alpha=230
			#os.system("raspistill -o foto.jpg -w 1920 -h 1080 -t 10000 -p '0,0,1920,1080' -op 200 &")
			CuentaAtras=4
			FotoRealizada=False
			Est+=1

	elif Est == 5:

		pantalla.blit(Fondo,(0,0))
						
		#Intentos
		pantalla.blit(Intentos[FotoFallida-1],POS_INTENTO)

		#Cuenta Atras
                if H2: 
                        CuentaAtras-=1
                        H2=False
			timer2 = threading.Timer(1,Hecho2)
                        timer2.start()

		#if CuentaAtras==5:
                #	pantalla.blit(Cuenta5,POS_CUENTA_ATRAS)
                #elif CuentaAtras==4:
                #        pantalla.blit(Cuenta4,POS_CUENTA_ATRAS)
                elif CuentaAtras==3:
                        pantalla.blit(Cuenta3,POS_CUENTA_ATRAS)
                elif CuentaAtras==2:
                        pantalla.blit(Cuenta2,POS_CUENTA_ATRAS)
                elif CuentaAtras==1:
                        pantalla.blit(Cuenta1,POS_CUENTA_ATRAS)
		elif CuentaAtras==0:
			pantalla.blit(Fondo,(0,0))
			pygame.display.flip()
			#camera.resolution = (1920,1080)
			camera.capture(Ruta+'foto.jpg')
			camera.stop_preview()
			FotoFallida-=1
			camera.close()
			Est+=1
		pygame.display.flip()


	elif Est == 6:


		#leds
		#GPIO.output(leds,GPIO.HIGH)

		#Limpiamos
		pantalla.fill(0)
		#Validar foto
		#Mostramos la foto y preguntamos si quiere validar
		im = pygame.image.load(Ruta+'foto.jpg')
		im =  pygame.transform.scale(im,(ANCHO,ALTO))
                pantalla.blit(im,(0,0))
		#Botones
                B_OK = pantalla.blit(Boton_OK,POS_BOTON_OK)
                B_NOK = pantalla.blit(Boton_NOK,POS_BOTON_NOK)	
	
		pygame.display.flip()
		#Est = LeerPulsadores(B_OK, B_NOK, Est)
		pulsadorListo=True
		while pulsadorListo:
			time.sleep(0.1)
			if (GPIO.input(pulsadorSi)==1):
				Est+=1
				pulsadorListo=False
				break
			if (GPIO.input(pulsadorNo)==1):
				Est=4
				pulsadorListo=False
				break		
	
	elif Est == 7:
		#leds
		#GPIO.output(leds,GPIO.LOW)

		#Foto Subida con exito
		os.system("mv "+Ruta+"foto.jpg /home/pi/SelfieMaton/BackEnd/Captura/foto"+str(NumeroFotos)+".jpg")
		NumeroFotos+=1
		#Cargando...
		
		pantalla.blit(Cargando1,(0,0))
		pygame.display.flip()
		time.sleep(2)
		pantalla.blit(Cargando2,(0,0))
		pygame.display.flip()
		time.sleep(1)
		pantalla.blit(Cargando3,(0,0))
		pygame.display.flip()
		time.sleep(3)
		pantalla.blit(Cargando4,(0,0))
		pygame.display.flip()
		time.sleep(2)

		pantalla.blit(Gracias,(0,0))
		pygame.display.flip()
		time.sleep(3)
		
		#break	( Pruebas solo se ejecuta una vez todo el proceso )		
	
		#break
		Est=0
	 
		#Lectura de tecla
