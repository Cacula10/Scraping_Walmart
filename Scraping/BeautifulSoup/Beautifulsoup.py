from requests import get
from bs4 import BeautifulSoup
headers = {"Accept-Language": "en-US, en;q=0.5"}
url = 'https://www.walmart.com/browse/electronics/laptop-computers/hp/3944_3951_132960?cat_id=3944_3951_132960&page=1&sort=new#searchProductResult'

# BeautifulSoup
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

main_container_note = html_soup.find_all('div', class_='search-result-product-title gridview')
main_container_preco = html_soup.find_all('span', class_='price display-inline-block arrange-fit price price-main')
main_container_star = html_soup.find_all('span', class_='visuallyhidden seo-avg-rating')
main_container_reviews = html_soup.find_all('span', class_='seo-review-count visuallyhidden')
main_container_link = html_soup.find_all('a', class_='product-title-link line-clamp line-clamp-2 truncate-title')


