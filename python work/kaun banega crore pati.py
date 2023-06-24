print("***************KAUN BANEGA CROREPATI******************")
name=input("Enter your name:")
print("Welcome to Kaun Banega crorepati",name)
print("""***rules of the game***
1.You will be given 4 options (option A,B,C,D)

2.. 1 price 1000
    2 price 2000
    3 price 3000
    4 price 4000
    5 price 5000
    6 price 6000
    7 price 7000
    8 price 8000
    9 price 9000
   10 price 10000
   
pehle 3 question ke baad apka price lock hojaiga matlb ki 3 prashno ka sahi jawab dene ke baad nishchit roop se aap 3000 ruppeee leke jainge


""")

quiz = ("1.Which of these sports requires you to shout out a word loudly during play?","2.In which of these two sports is the term ‘free hit’ used?","3.Which year is the leap year?","4.If David’s age is 27 years old in 2011. What was his age in 2003?","5.What is the reminder of 21 divided by 7","6.I am a number. I have 7 in the ones place. I am less than 80 but greater than 70. What is my number?","7.How many years are there in a decade?","8.Oil, natural gas and coal are examples of?","9.How many teeth does an adult human have?","10.What is the perimeter of a circle called?")

print("press 1 to play:")
print("press 2 to exit:")
b=int(input("enter your choice:"))
if b==1:
 print("THE QUIZ BEGAAAAAAAAAAAANNNNNNNNNNNNN")
 for x in quiz:
  if x==quiz[0]:
    print(quiz[0])
    print("""    <A.KHO KHO  >         <B.LUDO >
    <C.CARROM >         <D.CHESS>""")
    a=input("enter your choice:")
    if a=="A":
      print("you won 1000 rupees")
      continue
    else:
      print("apka uttar galat hai")
      break


  if x==quiz[1]:
    print(quiz[1])
    print("""    <A.cricket,football  >         <B.hockey,badminton >
    <C.football,kabaddi >         <D.cricket,hockey >""")
    a=input("enter your choice:")
    if a=="D":
      print("you won 2000 rupees")
      continue
    else:
      print("apka uttar galat hai")
      break    

  if x==quiz[2]:
    print(quiz[2])
    print("""    <A.1996 >         <B.2001 >
    <C.1515 >         <D.2018>""")
    a=input("enter your choice:")
    if a=="A":
      print("you won 3000 rupees")
      continue
    else:
      print("apka uttar galat hai, ab app yaha se 3 haazzar jarur leke jainge ")
      break    

  if x==quiz[3]:
    print(quiz[3])
    print("""    <A.25 >         <B.15 >
    <C.19 >         <D.11 >""")
    a=input("enter your choice:")
    if a=="C":
      print("you won 4000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break

  if x==quiz[4]:
    print(quiz[4])
    print("""    <A. 1 >         <B.0 >
    <C.2 >         <D.3>""")
    a=input("enter your choice:")
    if a=="B":
      print("you won 5000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break

  if x==quiz[5]:
    print(quiz[5])
    print("""    <A.67  >         <B.57 >
    <C.77 >         <D.87>""")
    a=input("enter your choice:")
    if a=="C":
      print("you won 6000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break

  if x==quiz[6]:
    print(quiz[6])
    print("""    <A.5  >         <B.100 >
    <C.50 >         <D.10>""")
    a=input("enter your choice:")
    if a=="D":
      print("you won 7000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break     

  if x==quiz[7]:
    print(quiz[7])
    print("""    <A.organs  >         <B.fossil fuels >
    <C.bio fuels >         <D.food>""")
    a=input("enter your choice:")
    if a=="B":
      print("you won 8000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break    

  if x==quiz[8]:
    print(quiz[8])
    print("""    <A.32  >         <B.30 >
    <C.27 >         <D.28>""")
    a=input("enter your choice:")
    if a=="A":
      print("you won 9000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break

  if x==quiz[9]:
    print(quiz[9])
    print("""    <A.diameter  >         <B.pie chart >
    <C.chord >         <D.circumference >""")
    a=input("enter your choice:")
    if a=="D":
      print("you won 10000 rupees")
      continue
    else:
      print("apka uttar galat hai,lakin apko 3000 ka check jarur milta hai")
      break   
      
  print(name,"is the crorepati taliaaaaaaa :),XD XD XD XD XD XD :):):):):):)")
elif b==2:
  print("good to see you",name,'come back again.')
else:
  print("entered the wrong number run the game again")
  