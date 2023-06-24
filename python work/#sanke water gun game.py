# sanke water gun game

import random
print("Welcome to snake water gun game")
print("""
rules:
1. snake will drink water.
2. gun will kill snake.
3. gun will lost in water.
""")

l1=["snake","water","gun"]
l2=["snake",
   "water",
   "gun"]
print("0 = snake")
print("1 = water")
print("2 = gun \n")
a = int(input("enter you choice :"))
b = random.choice(l2[0:3])

print(f"your choice===  {l1[a]} vs {b}  ====computer choice")
if l1[a]==b:
  print ('draw')
elif a==0 and b=="water"or a==1 and b=="gun" or a==2 and b=="snake":
  print("you win")
# elif a==1 and b=="gun":
#   print ('you win')
# elif a==2 and b=="snake":
#   print("you win")
else:
  print ("you loose")