import requests
import json
print("""********welcome to Rohit News*********
what type of news you want to get today:
""")

name_of_news=input("what type of news you want:")
r=requests.get(f"https://newsapi.org/v2/everything?q={name_of_news}&from=2023-05-24&sortBy=publishedAt&apiKey=22792aea8c9e4a55ac0d1626f67634b1")#you can take this link from news api .
# t=r.text
# print(t)this will print all the descripion
cott=t.count("title")
data=r.content
g=json.loads(data)
for x in range(cott):
            
            s=g["articles"][x]["title"],g["articles"][x]["description"]#this method will show you the title and the details about it.
            print(s,"\n")
