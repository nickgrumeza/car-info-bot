import requests
from bs4 import BeautifulSoup

class Car:
    def __init__(self, title, price_net, price_gross, mileage, transmission, power, year, fuel_type, owners, image_url):
        self.title = title
        self.price_net = price_net
        self.price_gross = price_gross
        self.mileage = mileage
        self.transmission = transmission
        self.power = power
        self.year = year
        self.fuel_type = fuel_type
        self.owners = owners
        self.image_url = image_url

def fetch_car_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cars = []
    for item in soup.select('.vehicle-card'):
        title = item.select_one('.vehicle-title').text.strip()
        price_net = item.select_one('.price-net').text.strip()
        price_gross = item.select_one('.price-gross').text.strip()
        mileage = item.select_one('.mileage').text.strip()
        transmission = item.select_one('.transmission').text.strip()
        power = item.select_one('.power').text.strip()
        year = item.select_one('.year').text.strip()
        fuel_type = item.select_one('.fuel-type').text.strip()
        owners = item.select_one('.owners').text.strip()
        image_url = item.select_one('.image').get('src')
        cars.append(Car(title, price_net, price_gross, mileage, transmission, power, year, fuel_type, owners, image_url))
    return cars