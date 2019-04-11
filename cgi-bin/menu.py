#!/usr/bin/python36

print("content-type: text/html")
print("\n")

import os
import subprocess
import pyttsx3	  #text to speech import gTTS for google voice(internet)
import getpass
import signal

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

invalid = "INVALID INPUT, Try Again"

def lw(x,y):
	print(subprocess.getoutput("clear"))
	exit()



signal.signal(2, lw) 			#to change comment when pressed crtl + c


os.system("tput setaf 7")		#setaf to change the text color
print("\n\n\n\n\n\t\t\t-------------------------------------")	
	
print("\t\t\t****welcome to express services ****")	

os.system("tput setaf 7")
print("\t\t\t-----------------------------------")
print("\n\n\n")


print(subprocess.getoutput("ifconfig enp0s3 | grep inet| head -1 | awk '{print $2}'")) #to print ipv4 address

engine.say("Welcome to web express, Please enter your password")
engine.runAndWait()



in_pass = getpass.getpass("enter ur password : ")

a_pass = "menu"


if in_pass == a_pass:


	 				#""" to print miltiple lines

	os.system("tput setaf 2")
	while True:
		print(subprocess.getoutput("clear"))
		print("""press 1 : to see date\npress 2 : to check calendar of specified year\npress 3 : to create file\npress 4 : to create a new user\npress 0: exit the menu""")

		os.system("tput setaf 7")

	 


		engine.say("Make Your Choice!")
		engine.runAndWait()

		 
		x= int(input("\n\n\t\tEnter Your Choice : "))	  #to get input from user


		if int(x) == 1:
			output1= subprocess.getstatusoutput("date")
			if output1[0] == 0:
				print("\n",output1[1])		
				engine.say(output1[1])
				engine.runAndWait()
		
			else:
				print("Wrong Input")



		elif int(x) == 2:
			month= input("\nenter month no. : ")
			year= input("\nenter year : ")
			engine.say("Here is the calendar")
			engine.runAndWait()
			output2= subprocess.getstatusoutput("cal {0} {1}".format(month,year))
			if output2[0] == 0:
				os.system("tput setaf 11")
				print("\n",output2[1])
				os.system("tput setaf 7")
			else:
				print(invalid)
	


		elif int(x) == 3:
			fname= input("\nenter file name : ")
			y=subprocess.getoutput("touch {0}" .format(fname))
			print(y)
			engine.say("File has been successfully created")
			engine.runAndWait()

	
		elif int(x) == 4:
			engine.say("Creating a New User in your system")
			engine.runAndWait()
			import add_user
		
		elif int(x) == 0:
			engine.say("Thanks for using web service express. Bye, See you soon!")
			engine.runAndWait()
			exit()
			
		else: print(invalid)
	
		input("press any key to begin again:")
else:
	engine.say("Sorry, Wrong Password! Try Again ")
	engine.runAndWait()
	print(invalid)
	


