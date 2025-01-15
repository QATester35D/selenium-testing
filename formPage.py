from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import random
import requests
import time

#Should look at refactoring this WebOrderForm class
# 1. focus just on dropdown/listbox functionality
# 2. grouping the other behaviors in another class
class WebOrderForm:
    def __init__(self, url):
        #Attributes of the WebOrderForm class here
        # self.url = "https://www.selenium.dev/selenium/web/formPage.html"
        self.url = url

    #The following are methods for the behavior and actions - this is mixed and why it should be refactored later
    def launchPage(self):
        seleniumDevbrowser = webdriver.Firefox()
        print("Now working with the Selenium Dev webpages - the web form page")
        seleniumDevbrowser.get(self.url)
        seleniumDevbrowser.set_window_size(900, 800)
        return(seleniumDevbrowser)

    def selectMultiItems(self,dropdown):
        listValues=[]
        dd1=seleniumDevbrowser.find_element(By.NAME, dropdown)
        v=Select(dd1)
        if v.is_multiple:
            print("This is a multiple select list.")
            listSize=len(v.options)
            nbrToSelect=random.randrange(1,listSize)
            for i in v.options:
                listValues.append(i.text)
            random_items = random.sample(listValues, nbrToSelect)
            v.deselect_all()
            for i in range(0,nbrToSelect):
                v.select_by_visible_text(random_items[i])        
            WebOrderForm.selectedItems(self,v)
        else:
            print("This is not a multi select list; exiting functionality.")

    def selectedItems(self,object):
        itemsSelected=object.all_selected_options
        size=len(itemsSelected)
        if size == 0:
            print("There are no items selected.")
            return
        for i in range(0,size):
            val=itemsSelected[i].text
            print("The value that was selected is:",val)

    def successPage(self,seleniumDevbrowser):
        element=WebDriverWait(seleniumDevbrowser,10).until(EC.presence_of_element_located((By.ID,'greeting')))
        messageText = seleniumDevbrowser.find_element(By.ID,"greeting")
        msg=messageText.text
        print("The status message is:",msg)
        seleniumDevbrowser.back()

    def checkURL(self):
        # Finding all the available links on webpage
        links = seleniumDevbrowser.find_elements(By.TAG_NAME, "a")
        # Iterating each link and checking the response status
        for i in links:
            url = i.get_attribute("href")
            # verifyLink(url)
            try:
                response = requests.head(url)
                # check the status code
                if response.status_code == 200:
                    continue
                else:
                    print(False,"for URL:",url)
                    continue
            except requests.ConnectionError as e:
                print("Connection error message:",e)

#Not using the main menu page
# wof=WebOrderForm("https://www.selenium.dev/selenium/web/index.html")
# seleniumDevbrowser=wof.launchPage()
# wof.checkURL()
# seleniumDevbrowser.close()

wof=WebOrderForm("https://www.selenium.dev/selenium/web/formPage.html")
seleniumDevbrowser=wof.launchPage()

##########################################################################################
###This is a temporary working section at the top between comment lines is for working on code and then moving it
wof.selectMultiItems("multi")
dropdown="multi"
listValues=[]
dd1=seleniumDevbrowser.find_element(By.NAME, dropdown)
v=Select(dd1)
if v.is_multiple:
    print("This is a multiple select list.")
    listSize=len(v.options)
    nbrToSelect=random.randrange(1,listSize)
    for i in v.options:
        listValues.append(i.text)
    random_items = random.sample(listValues, nbrToSelect)
    v.deselect_all()
    for i in range(0,nbrToSelect):
        v.select_by_visible_text(random_items[i])

singleDisabled=seleniumDevbrowser.find_element(By.NAME, "single_disabled")
v=Select(singleDisabled)
val=v.options
value=v.first_selected_option
# time.sleep(1)
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

## First Dropdown after the checkboxes (used to be line 137)
dd1=seleniumDevbrowser.find_element(By.NAME, "selectomatic")
dropDown1=Select(dd1) #dropbox
selectedItem=dropDown1.first_selected_option #This is used for whatever items is selected
val=selectedItem.text
print("Dropdown box 1 has value:",val)
dropDown1.select_by_index(2)
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
print("The selected value from the dropdown is now:",val)
dropDown1.select_by_value("two")
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
nbrOfItems=len(dropDown1.options)
randNbr=random.randrange(nbrOfItems)
randNbr=randNbr-1
dropDown1.select_by_index(randNbr)
selectedItem=dropDown1.first_selected_option
val=selectedItem.text
print("Ending with the selection of this random value:",val)

#Randomly selecting values from the listbox and printing them out
print("Randomly selecting values from the listbox named: multi")
wof.selectMultiItems("multi")
#Grab the selections in the rest of the listboxes
disabledDropDown=seleniumDevbrowser.find_element(By.NAME, "no-select")
v=Select(disabledDropDown)
value=v.first_selected_option
print("The value in the no-select disabled dropdown is:",value.text)
#Now get the values from the next listbox
print("Randomly selecting values from the listbox named: select_empty_multiple")
wof.selectMultiItems("select_empty_multiple")
print("Randomly selecting values from the listbox named: multi_true")
wof.selectMultiItems("multi_true")
print("Randomly selecting values from the listbox named: multi_false")
wof.selectMultiItems("multi_false")
##### Dealing now with the unique dropdown that has a disabled item

#####
# alert = driver.switch_to.alert
time.sleep(1)