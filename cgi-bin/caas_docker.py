#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess
import cgi
#import crypt
#import getpass

form = cgi.FieldStorage()
usr = form.getvalue('usr')

#usr = "rahul"
port = form.getvalue('port')
#usr = input("enter new user you want to add : ")
#port = input("enter a number (1024 - 65000) : ")
#passw = "iuc"
#passw = crypt.crypt(passw)
#a=subprocess.getstatusoutput("sudo useradd -p '"+passw+"' "+usr)
#if a[0] == 0:
#container_name = sp.getstatusoutput("sudo ansible-playbook staas/shellinabox.yml --extra-vars='x={0}'".format(cname))


b = subprocess.getstatusoutput("sudo docker run -dit -v /usr/bin/hostname:/usr/bin/hostname -p {0}:4200 --name {1} syaduka/shellinabox_final:v1".format(port,usr))
if b[0] == 0:
	print("<br><br>")
	#y = subprocess.getoutput("sudo docker exec -it {0} hostname -i".format(usr))
	#print(y)	
	x = subprocess.getoutput("sudo docker inspect -f '{use}' {usr1}".format( use='{{ .NetworkSettings.IPAddress }}',usr1=usr))	
	#x = subprocess.getoutput("sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' {usr1}".format(usr1=usr))
	print("<strong><br><br>USER NAME: root")	
	print("<br>DEFAULT PASSWORD: iuc")
	print("<br>IP ADDRESS: ")	
	print(x)	
	print("</strong> <br> <br> <br>")	
	print("""
	</div>
	<div style="padding:20px">
	<center><a href='http://""")
	print("""{0}:4200' target="Beatles">DOCKER LAUNCH</a>
	<iframe frameborder="0" name="Beatles" height="70%" width="100%">            
	</center>
	</div>  """.format(x))

else:
	print("<strong> <center><marquee behavior='alternate' direction='down'>sorry! Try different name....</marquee></center> </strong>")
	print(b[1])
