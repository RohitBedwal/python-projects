# change name of file


import os
print(os.getcwd())
# function
def call_png():
  a=os.listdir("")#here write path of the folder of file 
  for x in a:
    if x.endswith(".png"):
      b=input("what name you want to give")
      z=os.rename(x,f"{b}.png")
      

    
call_png()