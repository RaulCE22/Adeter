#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys

name_photo='photo.jpg'
id_photo='photo'
id_album='1663703257189492'
id_token='CAACEdEose0cBAPWOhfWGrq6m13PqSGDCiMr4uuG5KxPKt9ZB1SSueGNBBlFTSfne46KejG97awrtj9vY1ww2ntXFKkgPlwJJYwH8CJuYyjeRYOj02f6EELw943loBkJNl9cJlFrx1O07gs9rcN4j0ilOoHdSYIZABlhecxZAOKVZBl1OOLLwOwiWIwVOGRgQmA8mMVfA4kQ6OwJGJvZAKwyuKBwfJWXgZD'

print "Uploading Photo......"
graph = facebook.GraphAPI(id_token)
graph.put_photo(open(name_photo),id_photo,id_album)
print "Finish"

