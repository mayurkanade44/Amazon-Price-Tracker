from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from dotenv import load_dotenv
load_dotenv()
import os
password = os.environ.get('password')
myid = os.environ.get('myid')


url = input('enter product url ')
email_id = input('enter your email id').lower()
desired_price = float(input('enter your desired price'))


product_url = url
agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

desired_price = desired_price

response = requests.get(url=product_url, headers={'User-Agent': agent})
product_data = response.text

soup = BeautifulSoup(product_data, 'html.parser')
name = soup.find(name='span', id='productTitle').get_text().strip()
price = soup.find(name='span', class_="a-size-medium a-color-price priceBlockDealPriceString").get_text().strip('₹ ')
price = float(price.replace(',', ''))
if price < desired_price:
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=myid, password=password)
        connection.sendmail(from_addr=myid, to_addrs=email_id,
                            msg=f"Subject:Low Price Alert\n\n{name} is at {price}")