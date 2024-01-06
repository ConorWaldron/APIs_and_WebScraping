from bs4 import BeautifulSoup
import requests

# source will be a string
source = requests.get('https://www.ucd.ie/chembioeng/').text

#soup will be a bs4.Beautiful Soup object
soup = BeautifulSoup(source, 'lxml')

# Find the carousel image thing
carousel = soup.find('div', class_="swiper swiper-banner swiper--arrows")

# Extract the title and content for every image, noting that every item has a title, but not all have a content
for count, rotating_image in enumerate(carousel.find_all('a')):
    print(f'Item {count + 1} in the carousel')

    try:
        rotating_image_header = rotating_image.find(class_="swiper-banner__head").text
    except:
        rotating_image_header = 'No header found'
    print('Title: ' + rotating_image_header)

    try:
        rotating_image_content = rotating_image.find('div', class_="swiper-banner__content").p.text
    except:
        rotating_image_content = 'No Content'
    print('Content: ' + rotating_image_content)

    print() # white space between items