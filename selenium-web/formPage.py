from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import formPageHelpers
import random
import requests
import time

#Process through the main page of links making sure each link is valid; can be pinged/hit
#Not running this check all the time
check=False
if check:
    wof=formPageHelpers.WebOrderForm("https://www.selenium.dev/selenium/web/index.html")
    seleniumDevbrowser=wof.launchPage()
    wof.checkURL(seleniumDevbrowser)
    seleniumDevbrowser.close()

wof=formPageHelpers.WebOrderForm("https://www.selenium.dev/selenium/web/formPage.html")
seleniumDevbrowser=wof.launchPage()

##########################################################################################
###This is a temporary working section at the top between comment lines is for working on code and then moving it

##########################################################################################
email=seleniumDevbrowser.find_element(By.ID,"email")
age=seleniumDevbrowser.find_element(By.ID,"age")
helloThereButton=seleniumDevbrowser.find_element(By.ID,"submitButton")
btnLabel=helloThereButton.accessible_name
print("The button label is:",btnLabel)
email.send_keys("shawn@email.com")
age.send_keys("21")
helloThereButton.click() #clicking the "submitButton"
wof.successPage(seleniumDevbrowser)
#Testing the Image button
clickMeButton=seleniumDevbrowser.find_element(By.ID,"imageButton")
btnLabel=clickMeButton.accessible_name
print("The button label is:",btnLabel)
clickMeButton.click()
wof.successPage(seleniumDevbrowser)

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

## First Dropdown after the checkboxes
dd1=seleniumDevbrowser.find_element(By.NAME, "selectomatic")
dropDown1=Select(dd1) #dropbox
selectedItem=dropDown1.first_selected_option #This is used for whatever items is selected
val=selectedItem.text
print("Dropdown box 1 has the following value selected by default:",val)
nbrOfItems=len(dropDown1.options)
dropDown1.select_by_index(random.randrange(0,nbrOfItems)) #randomly select a value from the dropdown
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
print("Ending with the selection of this random value:",val)

#Randomly selecting values from the listbox and printing them out
print("Randomly selecting values from the listbox named: multi")
wof.selectMultiItems(seleniumDevbrowser,"multi")

#Grab the selections in the rest of the listboxes
wof.retrieveValuesInList(seleniumDevbrowser,"no-select")

#Now get the values from the next listbox
print("Randomly selecting values from the listbox named: select_empty_multiple")
wof.retrieveValuesInList(seleniumDevbrowser,"select_empty_multiple")
print("Randomly selecting values from the listbox named: multi_true")
wof.selectMultiItems(seleniumDevbrowser,"select_empty_multiple")

print("Randomly selecting values from the listbox named: multi_true")
wof.selectMultiItems(seleniumDevbrowser,"multi_true")
print("Randomly selecting values from the listbox named: multi_false")
wof.selectMultiItems(seleniumDevbrowser,"multi_false")
##### Dealing now with the unique dropdown that has a disabled item
##########Continue coding here:
singleDisabled=seleniumDevbrowser.find_element(By.NAME, "single_disabled")
v=Select(singleDisabled)
val=v.options
value=v.first_selected_option
time.sleep(1)
#####
# alert = driver.switch_to.alert
time.sleep(1)