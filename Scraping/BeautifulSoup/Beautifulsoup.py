from requests import get
from bs4 import BeautifulSoup
headers = {"Accept-Language": "en-US, en;q=0.5"}
url = 'https://www.walmart.com/browse/electronics/laptop-computers/hp/3944_3951_132960?cat_id=3944_3951_7052607&sort=best_seller#searchProductResult'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

#fazendo importação do site de 10 produtos - 1 container para cada 10 produtos
# fazer um Try/Exception para tratar erro, caso o container seja menor que 10
main_container_note = html_soup.find_all('div', class_='search-result-product-title gridview')
main_container_preco = html_soup.find_all('span', class_='price display-inline-block arrange-fit price price-main')
main_container_star = html_soup.find_all('span', class_='visuallyhidden seo-avg-rating')
main_container_reviews = html_soup.find_all('span', class_='seo-review-count visuallyhidden')
