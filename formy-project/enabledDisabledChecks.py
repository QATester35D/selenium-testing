from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import json
import time

formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Enabled and disabled elements\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(600, 800)
buttonsLink=formybrowser.find_element(By.LINK_TEXT, "Enabled and disabled elements")
buttonsLink.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "disabledInput")))
formybrowser.find_element(By.ID, "disabledInput").is_displayed()
formybrowser.find_element(By.ID, "input").is_displayed()
disabledField=formybrowser.find_element(By.ID, "disabledInput")
enabledField=formybrowser.find_element(By.ID, "input")

disabledFieldStatus=disabledField.is_enabled()
enabledFieldStatus=enabledField.is_enabled()
if disabledFieldStatus == False:
    print ("The \"Disabled input here...\" textbox is disabled...this is correct. The enabled status is",disabledFieldStatus)
else:
    print ("ERROR! The \"Disabled input here...\" textbox should be disabled...but it is enabled, status is:",disabledFieldStatus)

if enabledFieldStatus == True:
    print ("The \"Input here...\" textbox is enabled...this is correct. The enabled status is",enabledFieldStatus)
    print ("Entering in some text.")
    textToEnter="Testing"
    enabledField.send_keys(textToEnter)
    val=enabledField.get_property("value")
    if val == textToEnter:
        print("The text string that was entered is found in the textbox. The text in the field is:",val)
    else:
        print("The text in the field is not correct. The text should be",textToEnter," but it contains",val)
else:
    print ("ERROR! The \"Input here...\" textbox should be enabled...but it is not, status is:",enabledFieldStatus)

time.sleep(4)