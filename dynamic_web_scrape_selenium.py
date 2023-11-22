from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from bs4 import BeautifulSoup

# useful function to prettify our search outputs, often used when writing new code
def pretty(webelement):
    html_content = webelement.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    prettified_html = soup.prettify()
    print(prettified_html)

# Set up your driver (in headless mode to simulate a more human like behaviour)
edge_driver_path = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

# go to a website
driver.get('https://www.janespatisserie.com/')

# wait for prompt to accept cookies
try:
    cookies_accept = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'sc-qRumB.bWzgOU.amc-focus-first')) #must be a tuple
    )
    cookies_accept.click()
except:
    print('couldnt agree to cookies')


# Find the search icon to open the search bar
search_button = driver.find_element_by_class_name('search-button')
search_button.click()

# wait for search bar to open
try:
    search_text_box = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, 's')) #must be a tuple
    )

    # clear the text box, then put in my test string and hit return
    search_text_box.clear()
    search_text_box.send_keys('bread')
    search_text_box.send_keys(Keys.RETURN)

    # then we can wait 3 seconds, go back and search for something else
    time.sleep(3)
    driver.back()

    # You need to re-create all these old variables as otherewise 'Message: stale element reference: stale element not found'
    search_button = driver.find_element_by_class_name('search-button')
    search_button.click()
    search_text_box = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, 's'))  # must be a tuple
    )
    search_text_box.clear()
    search_text_box.send_keys('cake')
    search_text_box.send_keys(Keys.RETURN)

    results_div = driver.find_element_by_class_name('archive-posts-wrap')
    pretty(results_div)
    list_article_web_elements = driver.find_elements(By.TAG_NAME, 'article')
    for article_element in list_article_web_elements[:10]:
        title = article_element.find_element(By.TAG_NAME, 'h2').text
        print(title)

except:
    print('that failed')
    driver.quit()

print('success')
driver.quit()

