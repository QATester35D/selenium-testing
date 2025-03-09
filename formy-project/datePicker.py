from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

#########################################################################
# Exercising test automation on the datepicker web object
# Test Case to interact with the Date Picker - using sendkeys
#########################################################################
formybrowser = webdriver.Firefox()
formybrowser.get("https://formy-project.herokuapp.com/datepicker")
formybrowser.set_window_size(800, 800)

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "datepicker")))
pickDay=formybrowser.find_element(By.ID, "datepicker") #datepicker
pickDay.send_keys("07/10/2024")
# tabbing out of the object causes issues, you can't seem to get the focus back to the object
time.sleep(2)
pickDay.clear()
time.sleep(2)
pickDay.click()
time.sleep(1)
WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datepicker-switch")))
monthDisplayed=formybrowser.find_element(By.CLASS_NAME, "datepicker-switch").text
print ("Current month year combo:",monthDisplayed)
time.sleep(1)
prevBtn=formybrowser.find_element(By.CLASS_NAME,"prev").click() #select previous month
time.sleep(1)
nextBtn=formybrowser.find_element(By.CLASS_NAME,"next").click() #select next month
time.sleep(1)
pickDay.send_keys("07/15/2024")
pickDay.send_keys(Keys.ENTER) #this datepicker has odd functionality. after the send_keys you need this Enter key
pickDay.send_keys(Keys.ARROW_DOWN) #and then the down arrow to get back back to the datepicker
time.sleep(2)

#########################################################################
# Another approach/technique - Selecting the Day using xpath
#########################################################################
## One way is by XPath, however you have to know the "td" for the first day to increment from
### Selecting day 2
element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "datepicker")))
pickDay=formybrowser.find_element(By.ID, "datepicker")
pickDay.click()
element= formybrowser.find_element(By.XPATH, "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[3]")
element.click()
time.sleep(2)

#########################################################################
# Another approach/technique - by references the objects directly
formybrowser.find_element(By.ID, "datepicker").click()
formybrowser.find_element(By.CSS_SELECTOR, ".datepicker-days .datepicker-switch").click()
formybrowser.find_element(By.CSS_SELECTOR, ".month:nth-child(8)").click() #picks the 8th month - August
formybrowser.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .day:nth-child(1)").click() #Picks row 2, position 1 - August 4th
time.sleep(2)
#########################################################################