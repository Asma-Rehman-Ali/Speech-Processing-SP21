import requests
url='http://www.wildengland.com/englands-cities/'
page = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
city_names = [s.split('.')[1].strip().replace(')','').replace('(','') for s in [s.get_text()  for s in soup.find_all('strong')][1:51]]
print(city_names)
