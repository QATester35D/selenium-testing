from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#########################################################################
# Exercising test automation on the ability to use the scrollbar
#########################################################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Page Scroll\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 500)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Page Scroll")
keyMousePress.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "date")))

html = formybrowser.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(2)
html.send_keys(Keys.HOME)
time.sleep(2)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
html.send_keys(Keys.PAGE_UP)
time.sleep(2)
html.send_keys(Keys.HOME)
time.sleep(2)
formybrowser.execute_script("window.scrollTo(0, 100)")
time.sleep(2)
html.send_keys(Keys.HOME)
time.sleep(2)
html.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
html.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
html.send_keys(Keys.ARROW_UP)
time.sleep(2)
html.send_keys(Keys.ARROW_UP)
time.sleep(2) #Used only for testing purposes to see what is on the screen before the window is closed