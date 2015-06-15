#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv)>=2:
	cadena=sys.argv[1]
	print "Imagen: "+cadena
	img = qrcode.make("www.adeter.org/SelfieMaton/"+cadena)
	print "www.adeter.org/SelfieMaton/"+cadena
	f = open("qr_"+cadena+".png", "wb")
	img.save(f)
	f.close()
else:
	print "Insert new photo. Ej) python CodigoQR.py 220119912203.jpg"

