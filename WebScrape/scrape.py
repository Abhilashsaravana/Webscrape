import requests
import csv
from bs4 import BeautifulSoup
import mail_system

urls = ["https://finance.yahoo.com/quote/TSLA/","https://finance.yahoo.com/quote/LLY?p=LLY&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"] #URLs of yahoo finance pages
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

file_w = open("data.csv","w")
writer = csv.writer(file_w)
writer.writerow(['Stock Name','Current Price','Previous Close','Open','Bid','Ask','Day''s Range','52 Week Range','Volume','Avg.Volume'])
for url in urls:
    rows = []
    html_page = requests.get(url,headers=headers) #reads the html page
    soup = BeautifulSoup(html_page.content,'lxml') #reads the contents of the html page
    title = soup.find_all("div",id="mrt-node-Lead-5-QuoteHeader")[0].find("h1").get_text() #finds stock name
    price = soup.find_all("div",id="mrt-node-Lead-5-QuoteHeader")[0].find("div",class_='D(ib) Mend(20px)').find("fin-streamer").get_text() #finds stock price
    rows.append(title)
    rows.append(price)
    table1_info = soup.find_all("div",id='quote-summary')[0].find_all("table")[0] 
    table1_len = len(table1_info.find_all('td'))
    for i in range(1,table1_len,2): #finds the other information of the stock
        rows.append(table1_info.find_all('td')[i].get_text())
    writer.writerow(rows)
 

file_w.close()

mail_system.email_send('data.csv') #Calls the email sender function
    



