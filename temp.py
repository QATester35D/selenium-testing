from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import timedelta, date
import time

#########################################################################
#Test Case to fill out form
#########################################################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Complete Web Form\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 800)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Complete Web Form")
keyMousePress.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "datepicker")))

firstName=formybrowser.find_element(By.ID, "first-name") #text field
