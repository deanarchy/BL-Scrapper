from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen, Request

search = input('Search some products from bukalapak.com: ')
pages_count = int(input('How many pages you want to scrape? '))

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

products = []
prices = []
ratings = []

for i in range(1,pages_count+1):
    bl_pages = f'https://www.bukalapak.com/products?page={i}&search%5Bkeywords%5D={search}'
    url = urlopen(Request(bl_pages, headers=hdr))
    bs = BeautifulSoup(url, 'lxml')
    print(f'Processing page : {i}/{pages_count} from {bl_pages}')
    for a in bs.findAll(attrs={'class': 'bl-flex-item mb-8'}):
        name = a.find('div', attrs={'class': 'bl-product-card__description-name'})
        price = a.find('div', attrs={'class': 'bl-product-card__description-price'})
        rating = a.find('div', attrs={'class': 'bl-product-card__description-rating'})
        lnk = a.find('div', attrs={'class': 'bl-thumbnail--slider'})
        products.append(name.text.strip())
        prices.append(price.text.strip())
        if rating is not None:
            ratings.append(rating.text.strip())

df = pd.DataFrame([products, prices, ratings]).transpose()
df.columns = ['Produk', 'Harga', 'Total Rating']
df.to_csv('Hasil Mulung.csv',index=False)
print("Products info has been saved in the current directory under the name 'Hasil Mulung.csv'")