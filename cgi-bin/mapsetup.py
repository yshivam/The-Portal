#!/usr/bin/python36

import cgi
import subprocess


print("content-type: text/html")
print("")


form = cgi.FieldStorage()
data = form.getvalue('data')
usr = form.getvalue('usr')
#passw = form.getvalue('passw')


if data == "1":
	oo=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/jobtracker_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/task1.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
	

   
elif data == "2":
	oo=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/jobtracker_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/task2.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")

elif data == "3":
	oo=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/jobtracker_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/task3.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
		
elif data == "4":
	oo=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/jobtracker_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/task4.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
				
elif data == "5":
	oo=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/jobtracker_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook mapreduce/task5.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
