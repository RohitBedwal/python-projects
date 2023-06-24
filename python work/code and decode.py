print("*********welcome to code and decode**********")
print('\n')
import random
choice = 0
while choice!=3:
  print("press 1 to make secret code")
  print("press 2 to decode the secret code")
  print("press 3 to exit.")
  
  choice=int(input("\nenter your choice:"))
  while choice==1:
    a=input("\nenter the secret code")
    b=a.split()
    print("\n")
    for x in b:
      if len(x)<=3:
        print(x[::-1],end=" ")
    #     break
    #   else:
        
      else:
        
          if len(x)>3:
            q=x[1:]+x[0]
            a=['a','d','f','g','h','j','k','r','e','v','x','s','m','t','b']
            j=['a','d','f','g','h','j','k','r','e','v','x','s','m','t','b']
            y=['a','d','f','g','h','j','k','r','e','v','x','s','m','t','b']
            b=random.choice(a)
            d=random.choice(j)
            e=random.choice(y)
            c=b+e+d+q+d+e+b
            print(c,end=" ")
            
    break      
  print("\n")
  

  while choice==2:
    a=input("\nenter the secret code you want to decode")
    b=a.split()
    print("\n")
    for x in b:
      if len(x)<=3:
        print(x[::-1],end=" ")
    #     break
    #   else:
        
      else:
        
          if len(x)>3:
            
            g=x[-4]+x[3:-4]
           
            print(g,end=" ")
            
    break      
  print("\n")
    
    

print("Have a Nice Day")