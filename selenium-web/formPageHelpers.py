from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import random
import requests
import time

##########################################################################################
# This script is intended to be a helper file with methods to be used against a web order form
##########################################################################################
#Should look at refactoring this WebOrderForm class
#   1. focus just on dropdown/listbox functionality
#   2. grouping the other behaviors in another class
class WebOrderForm:
    def __init__(self, url):
        #Attributes of the WebOrderForm class here
        self.url = url   # self.url = "https://www.selenium.dev/selenium/web/formPage.html"

    #The following are methods for the behavior and actions - this is mixed and why it should be refactored later
    def launchPage(self):
        seleniumDevbrowser = webdriver.Firefox()
        print("Now working with the Selenium Dev webpages - the web form page")
        seleniumDevbrowser.get(self.url)
        seleniumDevbrowser.set_window_size(900, 800)
        return(seleniumDevbrowser)

    def selectMultiItems(self,seleniumDevbrowser,dropdown):
        listValues=[]
        dd1=seleniumDevbrowser.find_element(By.NAME, dropdown)
        v=Select(dd1)
        if v.is_multiple:
            print("This is a multiple select list.")
            listSize=len(v.options)
            nbrToSelect=random.randrange(0,listSize)
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

    def checkURL(self,seleniumDevbrowser):
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

    def retrieveValuesInList(self,seleniumDevbrowser,objName):
        disabledDropDown=seleniumDevbrowser.find_element(By.NAME, objName)
        v=Select(disabledDropDown)
        #check object type to see if ths option is available
        objType=disabledDropDown.aria_role
        match objType:
            case "combobox":
                value=v.first_selected_option
                print("The value selected and displayed is:",value.text)
            case "listbox":
                print("Checking this listbox allows multiple selections:",v.is_multiple)

        state=disabledDropDown.is_enabled()
        if state:
            print("The dropdown/listbox is in an enabled state.")
        else:
            print("The dropdown/listbox is in a disabled state.")
        listSize=len(v.options)
        for i in range(0,listSize):
            print("Value in the list:",v.options[i].text)
        time.sleep(1)
