import pytest
import time
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
cities = ['Kochi','Mohali','Calicut','Aurangabad','Kota','Chennai','Goa','Nagpur','Delhi','Chandigarh','Pune','Amritsar','Shirdi','Wayanad','Agra','Mathura','Jalandhar','Gurgaon','Faridabad','Vadodara','Hyderabad','Varanasi','Zirakpur','Vijayawada','Jodhpur','Raipur','Coimbatore','Mangalore','Nainital','Nashik','Patna','Ghaziabad','Noida','Siliguri','Guwahati','Shillong','Jamshedpur','Kanpur','Surat','Munnar','Shimla','Dehradun','Lucknow','Indore','Coorg','Jaipur','Puri','Mumbai','Gwalior','Katra','Prayagraj','Udaipur','Ujjain','Madurai','Bhopal','Digha','Meerut','Ludhiana','Ahmedabad','Pondicherry','Kolkata','Ranchi','Bareilly','Mahabaleshwar','Bangalore','Mysore','Tirupati','Manali','Bhubaneswar','Ajmer','Mussoorie','Jabalpur','Haridwar','Trivandrum','Ooty','Gangtok','Rishikesh','Lonavala','Visakhapatnam']
for city in cities:
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.tripadvisor.in/")
        #driver.set_window_size(671, 816)
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@class='ui_pill brand-trip-search-geopill-TripSearchGeoPill__pill--2CF8h']").click()
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Where to?']")))
        except TimeoutException:
            print("Loading took too much time!")
        myElem.send_keys(city)
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[@class='common-typeahead-results-BasicResult__resultTitle--1TQbu']").click()
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Things to do')]")))
        except TimeoutException:
            print("Loading took too much time!")
        myElem.click()
        time.sleep(5)
        myElem = driver.find_element(By.XPATH,"//div[@class='attractions-carousel-shelf-ShelfCarousel__items--2kwB3']")
        html = myElem.get_attribute('innerHTML')
        #print(html)
        todo = [] 
        result = re.findall('<h3>.+?</h3>', html)
        for i in result:
            todo.append(i.replace("<h3>","").replace("</h3>","").replace("amp;",""))
        todo_dict = {city:todo}
        print(todo_dict)
        driver.quit()
    except:
        driver.quit()
        continue
