#!/usr/bin/python

from ClassLogFotos import LogFotos
import time

LOG = LogFotos()
while True:
	LOG.FuncProcesarImagen()
	LOG.FuncSubirImagen()
	time.sleep(5)

