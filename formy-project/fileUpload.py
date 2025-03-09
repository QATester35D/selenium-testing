from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys
import time

#########################################################################
# Exercising test automation on the capability to upload a file
#########################################################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"File Upload\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(600, 800)
buttonsLink=formybrowser.find_element(By.LINK_TEXT, "File Upload")
buttonsLink.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-choose")))
formybrowser.find_element(By.CLASS_NAME, "btn-choose").is_displayed()
chooseBtn=formybrowser.find_element(By.CLASS_NAME, "btn-choose")

chooseBtnTextContent=chooseBtn.get_property("textContent")
if chooseBtnTextContent == "Choose":
    print ("The Choose button has the correct label of",chooseBtnTextContent)
else:
    print ("ERROR! The Choose button label should have been:",chooseBtnTextContent)

chooseBtnEnabled=chooseBtn.is_enabled()
if chooseBtnEnabled == True:
    print ("The Choose button is enabled...this is correct. The enabled status is",chooseBtnEnabled)
else:
    print ("ERROR! The Choose button is disabled when it should be enabled, status is:",chooseBtnEnabled)

chooseBtnColor=Color.from_string(formybrowser.find_element(By.CLASS_NAME,'btn-choose').value_of_css_property('background-color'))
print("The color of the button is:",chooseBtnColor)

#Enter text into the file field since the File Explorer window isn't supported by Selenium
fileName="C:\Temp\Selenium test file.txt"
fileUploadField=formybrowser.find_element(By.ID, "file-upload-field")
fileUploadField.send_keys(fileName)
fileUploadField.send_keys(Keys.TAB)
fileFieldValue=fileUploadField.get_property("value")
print("The value in the text field is",fileFieldValue)

resetBtn=formybrowser.find_element(By.CLASS_NAME, "btn-reset")
resetBtnEnabled=resetBtn.is_enabled()
if resetBtnEnabled == True:
    print ("The Reset button is enabled...this is correct. The enabled status is",resetBtnEnabled)
else:
    print ("ERROR! The Reset button is disabled when it should be enabled, status is:",resetBtnEnabled)

resetBtn.click()
fileFieldValue=fileUploadField.get_property("value")
if fileFieldValue == "":
    print ("The text field has been properly reset and the value is now empty. The value property is",fileFieldValue)
else:
    print ("ERROR! The text field has NOT been properly reset and the value reads",fileFieldValue)

time.sleep(4) #Used only for testing purposes to see what is on the screen before the window is closed