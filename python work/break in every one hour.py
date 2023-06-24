# An code which tells you to take a break every one hour 
import win32com.client
import time 
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True :
   
   def nap_break():

      l1="Its time to take a break."
      speaker.speak(l1)
      print("waiting 10 sec")
      time.sleep(3600)#this in an endless loop you can set the timing by yourself 
   
   nap_break()


