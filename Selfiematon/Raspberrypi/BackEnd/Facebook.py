#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys

name_photo= sys.argv[1]
id_photo=name_photo.split('.')[0]
id_album='1500659980218134'
id_token='CAACEdEose0cBAIQG1YCuSaHYAN21LIlwMYDfOGik8n38ZAqDWgYYEacP1SuZBUELQ9j1FaWCMH0766VoiuL4hPWq6HeZA2iusMQdbMZB4uOd1pUWuTZCMPR8dsWZCEK95SYExuaiFvW1P4atIF1CznXirceYZBgudfA0Rew18vAB4B5JNJHfsN0ZA47tbiMNVMuBW0Jzwv6ZA2ebL8NmZBnMwdt3vn6Px2rg4ZD'

print "Uploading Photo......"
graph = facebook.GraphAPI(id_token)
graph.put_photo(open(name_photo),id_photo,id_album)
print "Finish"
