#small calculator do working on 2 numbers

print('************MAKING A CALCULATOR**********')

print("Select one of the following")

a = int(input("First number:"))
b = int(input("second number:"))

print("1. multiplicaton ")
print("2. divide")
print("3. addition")
print("4. subtraction")

choice=int(input("what do you want:"))

if choice==1:
  print (a*b)

elif choice==2:
  print(a/b)

elif choice==3:
   print(a+b)

elif choice==4:
   print(a-b)