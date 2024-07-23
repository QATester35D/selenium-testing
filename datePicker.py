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
# pickDay.send_keys(Keys.TAB) #this causes issues, you can't seem to get the focus back to the object
time.sleep(2)
pickDay.clear()
time.sleep(2)
pickDay.click()
time.sleep(2)
WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "datepicker-switch")))
monthDisplayed=formybrowser.find_element(By.CLASS_NAME, "datepicker-switch").text
print ("Current month year combo:",monthDisplayed)
time.sleep(2)
prevBtn=formybrowser.find_element(By.CLASS_NAME,"prev").click()
time.sleep(2)
nextBtn=formybrowser.find_element(By.CLASS_NAME,"next").click()
time.sleep(2)
#########################################################################
# Selecting the Day
#########################################################################
## One way is by XPath, however you have to know the "td" for the first day to increment from
### Selecting day 2
element= formybrowser.find_element(By.XPATH, "/html/body/div[2]/div[1]/table/tbody/tr[1]/td[3]")
element.click()
time.sleep(2)
#########################################################################
# Another way is sending the date - THIS NEEDS TO BE FIXED
# pickDay.click()
# # element= formybrowser.find_element(By.CSS_SELECTOR, "data-date").text("1719964800000")
# # ActionChains(formybrowser).move_to_element(element).click().send_keys("14").perform()
# select = Select(formybrowser.find_element(By.CSS_SELECTOR, 'data-date').text("1721628000000"))
# # select.select_by_value('14')
time.sleep(2)
