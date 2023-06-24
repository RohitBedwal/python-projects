
import time 
from win11toast import toast

a= int(input("how many time you want to run the code:"))

for x in range(a) :
   heading= input("Enter the heading:")
   Description= input("Enter the message you want to give:")
   time.sleep(0)#it is the the time you want the code to wait before waiting (in seconds).
   toast(heading,Description,
      icon="")#paste the path of the icon you want to show
   
