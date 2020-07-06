from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = input('Input Bukalapak URL: ')
driver = webdriver.Chrome()

products = []
prices = []
ratings = []
link = []

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, features='lxml')
for a in soup.findAll(attrs={'class': 'bl-flex-item mb-8'}):
    name = a.find('div', attrs={'class': 'bl-product-card__description-name'})
    price = a.find('div', attrs={'class': 'bl-product-card__description-price'})
    rating = a.find('div', attrs={'class': 'bl-product-card__description-rating'})
    lnk = a.find('div', attrs={'class': 'bl-thumbnail--slider'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
    if rating is not None:
        ratings.append(rating.text.strip())
    link.append(lnk.a.get('href'))
    print(lnk)

df = pd.DataFrame([products, prices, ratings,link]).transpose()
df.columns = ['Produk', 'Harga', 'Total Rating','Link Produk']
df.to_csv('Hasil Mulung.csv',index=False)
print("Products info has been saved in the current directory under the name 'Hasil Mulung.csv'")
driver.quit()