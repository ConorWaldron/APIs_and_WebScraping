from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Set up your driver (in headless mode to simulate a more human like behaviour)
edge_driver_path = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

# go to a website
driver.get('https://www.atptour.com/en/rankings/singles')

time.sleep(1)

# print the title
title = driver.title
print(title)

# useful function to prettify our search outputs, often used when writing new code
def pretty(webelement):
    html_content = webelement.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    prettified_html = soup.prettify()
    print(prettified_html)

n = 3
# Part 1, print the top n players by ranking points
print(f'The top {n} players by ATP ranking are')

# find the table, then examine its HTML using Beautiful Soup prettify() to decide what to search for next
search = driver.find_element_by_id('player-rank-detail-ajax')
time.sleep(3)

# In the table, find the row that contains the player
list_player_row = search.find_elements_by_class_name('player-cell-wrapper')
for count, player_row in enumerate(list_player_row[:n]):  # only the top 8 qualify for ATP finals
    # Get row for top players
    player_name = player_row.text # within the row, find the name
    print(f'at position number {count+1}, {player_name}')
    time.sleep(2)
time.sleep(3)

# Part 2, find the oldest n players by sorting by age
print(f'the oldest {n} players are')

# find the sort by age web element, note it is still in the table
header_row_element = search.find_element_by_class_name('header-row')
time.sleep(1)
age_header_element = header_row_element.find_element_by_css_selector('.header-row .age-cell')
time.sleep(1)
age_anchor_element = age_header_element.find_element_by_css_selector('.sorting-arrow')
time.sleep(1)
#click on the age sorting anchor element
age_anchor_element.click()  # This doesnt work as cloudflare knows we are a bot
time.sleep(1)

age_sorted_search = driver.find_element_by_id('player-rank-detail-ajax')
age_sorted_list_player_row = age_sorted_search.find_elements_by_class_name('player-cell-wrapper')
for count, player_row in enumerate(age_sorted_list_player_row[:n]):  # only the top 8 qualify for ATP finals
    # Get row for top players
    player_name = player_row.text # within the row, find the name
    print(f'the number {count+1} oldest player is {player_name}')
    time.sleep(2)

driver.quit()