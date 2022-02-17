***********************************************************************************************************************
imdb web-scraping with csv file 

from bs4 import BeautifulSoup
import requests
from csv import writer
url="https://www.imdb.com/chart/top/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('section',class_="listing items")

with open('movie.csv','w',encoding='utf8',newline='')as f:
    thewriter=writer(f)
    header=['Titel','Year','Rating']
    thewriter.writerow(header)
    for (variable) in lists:
         title = lists.find('a',class_="secondaryInfo").text.replace('\n',' ')
         year = lists.find('span',class_="secondaryInfo").text.replace('\n',' ')
         rating = lists.find('td',class_="ratingColumn imdbRating").text.replace('\n',' ')
         info=[title,year,rating]
         thewriter.writerow(info)
   
  ********************************************************************************************************************
  
  hotel web-scraping with csv
  
  from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__location").text.replace('\n', '')
        price = list.find('span', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('span', class_="illustrated-features__description").text.replace('\n', '')
        
        info = [title, location, price, area]
        thewriter.writerow(info)
  
