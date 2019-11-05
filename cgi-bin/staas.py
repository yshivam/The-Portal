#!/usr/bin/python36

print("content-type: text/html")
print("")


import subprocess as sp
import cgi 



form = cgi.FieldStorage()
user = form.getvalue('user')
size = form.getvalue('size')


o= sp.getstatusoutput("sudo ansible-playbook staas/staas.yml --extra-vars=' client='{0}' size={1}'".format(user,size))

if o[0]==0:
	print("storage is created")
else:
	print("error")
	
	
	
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


	

print("""  <pre id="pre"><strong> For Linux: </strong> 

<strong>Copy the following command and execute it to mount !!</strong> </pre>  \n """)

print("mkdir /media/{0}".format(user))
print("<br> <br>")
print("<br> <br> mount 172.20.10.2:/staas/{0}  /media/{0}".format(user))


