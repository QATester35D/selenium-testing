from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def successPage():
    element=WebDriverWait(seleniumDevbrowser,10).until(EC.presence_of_element_located((By.ID,'greeting')))
    messageText = seleniumDevbrowser.find_element(By.ID,"greeting")
    msg=messageText.text
    print("The status message is:",msg)
    seleniumDevbrowser.back()

seleniumDevbrowser = webdriver.Firefox()
print("Now working with the Selenium Dev webpages - the web form page")
seleniumDevbrowser.get("https://www.selenium.dev/selenium/web/formPage.html")
seleniumDevbrowser.set_window_size(900, 800)
email=seleniumDevbrowser.find_element(By.ID,"email")
age=seleniumDevbrowser.find_element(By.ID,"age")
helloThereButton=seleniumDevbrowser.find_element(By.ID,"submitButton")
btnLabel=helloThereButton.accessible_name
print("The button label is:",btnLabel)
email.send_keys("shawn@email.com")
age.send_keys("21")
helloThereButton.click()
successPage()
clickMeButton=seleniumDevbrowser.find_element(By.ID,"imageButton")
btnLabel=clickMeButton.accessible_name
print("The button label is:",btnLabel)
clickMeButton.click()
successPage()

seleniumDevbrowser.find_element(By.ID, "checky").is_displayed()
checkbox1=seleniumDevbrowser.find_element(By.ID, "checky")
checkbox2=seleniumDevbrowser.find_element(By.ID, "checkedchecky")
checkbox3=seleniumDevbrowser.find_element(By.ID, "disabledchecky")
checkbox4=seleniumDevbrowser.find_element(By.ID, "randomly_disabled_checky")
cb1Status=checkbox1.is_selected()
cb2Status=checkbox2.is_selected()
cb3Status=checkbox3.is_selected()
cb4Status=checkbox4.is_selected()
print ("The Formy checkbox #1 checkbox status is: ",cb1Status)
print ("The Formy checkbox #2 checkbox status is: ",cb2Status)
print ("The Formy checkbox #3 checkbox status is: ",cb3Status)
print ("The Formy checkbox #3 checkbox status is: ",cb4Status)
checkbox1.click()
checkbox2.click()
cb1Status=checkbox1.is_selected()
cb2Status=checkbox2.is_selected()
try:
    assert cb1Status == True
except:
    print("The checkbox should be checked.")

try:
    assert cb2Status == False
except:
    print("The checkbox should not be checked.")
dd1=seleniumDevbrowser.find_element(By.NAME, "selectomatic")
dropDown1=Select(dd1) #dropbox
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
print("Dropdown box 1 has value:",val)

time.sleep(1)