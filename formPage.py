from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import random
import time

class WebOrderForm:
    def __init__(self):
        self.url = "https://www.selenium.dev/selenium/web/formPage.html"

    def launchPage(self):
        seleniumDevbrowser = webdriver.Firefox()
        print("Now working with the Selenium Dev webpages - the web form page")
        # seleniumDevbrowser.get("https://www.selenium.dev/selenium/web/formPage.html")
        seleniumDevbrowser.get(self.url)
        seleniumDevbrowser.set_window_size(900, 800)
        return(seleniumDevbrowser)

    def selectMultiItems(self,dropdown):
        dd1=seleniumDevbrowser.find_element(By.NAME, dropdown)
        v=Select(dd1)
        valList=v.options
        v.deselect_all()
        bkfstLen=len(valList)
        nbrToSelect=random.randrange(1,bkfstLen)
        # dd1=seleniumDevbrowser.find_element(By.NAME, "multi")
        dropDown1=Select(dd1) #dropbox
        for i in range(0,nbrToSelect):
            dropDown1.select_by_index(i)

        WebOrderForm.selectedItems(self,dropDown1)
        # itemsSelected=dropDown1.all_selected_options
        # for i in range(0,nbrToSelect):
        #     val=itemsSelected[i].text
        #     print(val)

    def selectedItems(self,object):
        itemsSelected=object.all_selected_options
        size=len(itemsSelected)
        if size == 0:
            print("There are no items selected.")
            return
        for i in range(0,size):
            val=itemsSelected[i].text
            print(val)

    def successPage(self,seleniumDevbrowser):
        element=WebDriverWait(seleniumDevbrowser,10).until(EC.presence_of_element_located((By.ID,'greeting')))
        messageText = seleniumDevbrowser.find_element(By.ID,"greeting")
        msg=messageText.text
        print("The status message is:",msg)
        seleniumDevbrowser.back()

wof=WebOrderForm()
seleniumDevbrowser=wof.launchPage()
wof.selectMultiItems("multi")
##################This section between comment lines is for working on code and then moving it
#Grab the selections in the rest of the listboxes
disabledDropDown=seleniumDevbrowser.find_element(By.NAME, "no-select")
v=Select(disabledDropDown)
value=v.first_selected_option
print("The value in the disabled dropdown is:",value.text)
#Now get the values from the next listbox
wof.selectMultiItems("select_empty_multiple")
wof.selectMultiItems("multi_true")
wof.selectMultiItems("multi_false")


time.sleep(1)
##########################################################################################
email=seleniumDevbrowser.find_element(By.ID,"email")
age=seleniumDevbrowser.find_element(By.ID,"age")
helloThereButton=seleniumDevbrowser.find_element(By.ID,"submitButton")
btnLabel=helloThereButton.accessible_name
print("The button label is:",btnLabel)
email.send_keys("shawn@email.com")
age.send_keys("21")
helloThereButton.click()
wof.successPage()
clickMeButton=seleniumDevbrowser.find_element(By.ID,"imageButton")
btnLabel=clickMeButton.accessible_name
print("The button label is:",btnLabel)
clickMeButton.click()
wof.successPage()

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

## Dropdown
dd1=seleniumDevbrowser.find_element(By.NAME, "selectomatic")
dropDown1=Select(dd1) #dropbox
selectedItem=dropDown1.first_selected_option #This is used for whatever items is selected
val=selectedItem.text
print("Dropdown box 1 has value:",val)
dropDown1.select_by_index(2)
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
dropDown1.select_by_value("two")
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
time.sleep(1)

#Mulit-select list
wof.selectMultiItems()

# alert = driver.switch_to.alert
time.sleep(1)