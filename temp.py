from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

#########################################################################
#Test Case to interact with the Date Picker
#########################################################################
formybrowser = webdriver.Firefox()
# formybrowser.get("https://formy-project.herokuapp.com/form")
formybrowser.get("https://formy-project.herokuapp.com/datepicker")
formybrowser.set_window_size(800, 800)

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "datepicker")))
pickDay=formybrowser.find_element(By.ID, "datepicker") #datepicker
pickDay.send_keys("07/10/2024")
