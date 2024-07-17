from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Radio Button\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 500)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Radio Button")
keyMousePress.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "radio-button-1")))

#########################################################################
#new code
#########################################################################
radioButtonList=formybrowser.find_elements(By.NAME, "exampleRadios") #The actual radio button circle itself
radioButtonLabelList=formybrowser.find_elements(By.CLASS_NAME, "form-check-label") #The label associated with each radio button

time.sleep(2) #Used only for testing purposes to see what is on the screen before the window is closed