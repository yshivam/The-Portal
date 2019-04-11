#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess
#import crypt
#import getpass
import cgi

form = cgi.FieldStorage()
#usr = form.getvalue('usr')
port = form.getvalue('port')

#usr = input("enter new user you want to add : ")
#port = input("enter a number (1024 - 65000) : ")

#passw = "iuc"

#passw = crypt.crypt(passw)
#a=subprocess.getstatusoutput("sudo useradd -p '"+passw+"' "+usr)

#if a[0] == 0:
print("User has been successfully created. <br> Please follow the instructions to use terminator")
	
	
print("""  <style type="text/css">

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
DOWNLOAD MOBAXTERM FROM HERE!!!!!
<a href="https://download.mobatek.net/1062018041114250/MobaXterm_Installer_v10.6.zip" download>Download Mobaxterm</a>
$ Open Mobaxterm and Click on start local terminal and wait for terminal to arrive
<strong>Copy the following command and execute it!!</strong> </pre>  \n """)

print("\n \n <strong> ssh terminator@192.168.43.7 -X terminator </strong>")

print(""" <pre id="pre"> \n
<strong>Type your password</strong>
$ your default password is : iuc
</pre>
""")

