#!/usr/bin/python36

print("content-type: text/html")
print("")

import  cgi
import subprocess as sp



form = cgi.FieldStorage()
user = form.getvalue('user')
size = form.getvalue('size')

setup_output1 = sp.getstatusoutput("sudo ansible-playbook staas/blocklv.yml --extra-vars='client='{0}' size={1}'".format(user,size))

if setup_output1[0]  == 0:
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

	<strong>Target Setup done. Copy the following commands and run in your terminal</strong> </pre>  \n """)
	print(""" <br> <br> <strong> iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.7 --discover </strong>

	<br> <br> <strong> iscsiadm --mode node --targetname mycloud --portal 192.168.43.7:3260 --login
		     </strong> """)


 
else:
        print("target setup failed... .")
        


