import requests
from bs4 import BeautifulSoup
import mariadb
import csv

mydb = mariadb.connect(
  host="127.0.0.1",
  user="root",
  password="123",
  database="deneme"
)
mycursor = mydb.cursor()
# csv
f = open('wordlist.csv', 'at', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(["search", "url"])
# user search
user_input = input("enter something to search :")
print("geliyor gelmekte olan ....")


# google search
class google_search:
    def __init__(self, name_search):
        self.name = name_search

    def Gsearch(self):
        count = 0
        try:
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")
        for i in search(query=self.name, tld='co.in', lang='en', num=2, stop=10, pause=0):
            count += 1
            print(count)
            print(i)
            csv_writer.writerow(["google", i])
            sql = "INSERT INTO list (search_engine, url) VALUES (%s, %s)"
            val = ("Google",i)
            mycursor.execute(sql, val)
            mydb.commit()

if __name__ == '__main__':
    gs = google_search(user_input)
    gs.Gsearch()

# bing search
bing_input = 'https://www.bing.com/search?q=' + user_input

headers = {
    'User-Agent':
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
}  # Linux

request = requests.get(bing_input, headers=headers)
webContent = BeautifulSoup(request.content, 'html.parser')

listContent = webContent.find_all('ol')

for content in listContent:
    liContent = content.find_all('li')
    for content in liContent:
        divContent = content.find('div')
        if divContent == None:
            pass
        else:
            h2Content = divContent.find('h2')
            if h2Content == None:
                pass
            else:
                aContent = h2Content.find('a').get('href')
                if aContent == None:
                    pass
                else:
                    csv_writer.writerow(["bing", aContent])
                    sql = "INSERT INTO list (search_engine, url) VALUES (%s, %s)"
                    val = ("bing", aContent)
                    mycursor.execute(sql, val)
                    mydb.commit()