#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess
import cgi

form = cgi.FieldStorage()
usr = form.getvalue('usr')
data = form.getvalue('data')
#passw = form.getvalue('passw')
print(data)
print(usr)


#usr = input("enter usrname")
#y = crypt.crypt(passw)
#a=subprocess.getstatusoutput("sudo useradd -p '"+y+"' "+usr)
if data == "1":
	oo=subprocess.getstatusoutput("sudo ansible-playbook hadoop/namenode_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook hadoop/data_one.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
	

   
elif data == "2":
	oo=subprocess.getstatusoutput("sudo ansible-playbook hadoop/namenode_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook hadoop/data_two.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")

elif data == "3":
	oo=subprocess.getstatusoutput("sudo ansible-playbook hadoop/namenode_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook hadoop/data_three.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
		
elif data == "4":
	oo=subprocess.getstatusoutput("sudo ansible-playbook hadoop/namenode_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook hadoop/data_four.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
				
elif data == "5":
	oo=subprocess.getstatusoutput("sudo ansible-playbook hadoop/namenode_setup.yml")
	o=subprocess.getstatusoutput("sudo ansible-playbook hadoop/data_five.yml")
	if oo[0] or o[0] != 0:
		print("Server Error, Contact your server")
	else:
		print("Successful")
		

		
print("""<style type="text/css">

		#pre {
	background-color: #051e30 ;
    border-color: #289ff4;
    border-style: solid;
    border-width: 1px 1px 1px 4px;
    font-family: 'Cutive Mono', monospace;
    line-height: 19px;
    margin: 30px 0;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 10px 10px 10px 18px;
    word-wrap: break-word;
    border: 1px solid #ddd;
    
    vertical-align: baseline;
	display: block;
	color: #fff;
} 
</style>

""")

	

print("""  <pre id="pre"><strong> For Windows: </strong> 
DOWNLOAD MOBAXTERM FROM HERE TO UPLOAD FILES!!!!!
<a href="https://download.mobatek.net/1062018041114250/MobaXterm_Installer_v10.6.zip" download>Download Mobaxterm</a>
$ Open Mobaxterm and Click on start local terminal and wait for terminal to arrive
<strong>Copy the following command and execute it!!</strong> </pre>  \n """)


print(""" <pre id="pre"> \n
<strong>Type your password</strong>
$ your default password is : iuc
</pre>
""")



