from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
##########################################################################
seleniumDevbrowser = webdriver.Firefox()
print("Now working with the Selenium Dev webpages - the Drag and Drop page")
seleniumDevbrowser.get("https://www.selenium.dev/selenium/web/dragAndDropTest.html")
seleniumDevbrowser.set_window_size(900, 800)
action_chains=ActionChains(seleniumDevbrowser)
test1Item=seleniumDevbrowser.find_element(By.ID,"test1")
test2Item=seleniumDevbrowser.find_element(By.ID,"test2")
test3Item=seleniumDevbrowser.find_element(By.ID,"test3")
test4Item=seleniumDevbrowser.find_element(By.ID,"test4")
# Creating a vertical alignment. The offset is based on the object's location
action_chains.drag_and_drop_by_offset(test1Item,200,200).perform()
action_chains.drag_and_drop_by_offset(test2Item,200,220).perform()
action_chains.drag_and_drop_by_offset(test3Item,-160,40).perform()
action_chains.drag_and_drop_by_offset(test4Item,-160,60).perform()
time.sleep(1)
