print("library management system")

a = int(input("write the  no. of anime you want to enter "))
c = []

for x in range(0, a):
  b = input("name of the anime")
  c.append(b)

for index, c in enumerate(c, start=1):
  print(index, c)








class library:
  books=[]
  no_of_books=int(input("Enter the no. of books you want:"))
  for x in range(0,no_of_books):  
      b=input("Enter the name of the book")
      books.append(b)
  print(books)
  def gg(self):
    print(f"no of books are{self.no_of_books}")
  if no_of_books==len(books):
    print("no. of books are same as books")
  else:
    raise ValueError("You are writing a wrong answer try again")
c=library()
c.gg()
