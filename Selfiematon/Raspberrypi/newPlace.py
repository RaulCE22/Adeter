import os

name = raw_input('Introduce el nombre del lugar: ')

print "Creando carpetas..."


d = 'mkdir places/'+name
c = ['album','capture','log','logotype','presentation','thankyou']

os.system(d)
for i in c:
	os.system(d+'/'+str(i))
