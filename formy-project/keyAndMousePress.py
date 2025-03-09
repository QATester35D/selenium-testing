from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys
import time

#########################################################################
# Exercising test automation - performing keyboard actions and mouse clicks
#########################################################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Key and Mouse Press\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 800)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Key and Mouse Press")
keyMousePress.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "button")))

labelForField=formybrowser.find_element(By.XPATH,"/html/body/div/form/div[1]/div/label")
textLabel=labelForField.get_property("textContent")
if textLabel == "Full name":
    print ("The label above the field has the correct label of",textLabel)
else:
    print ("ERROR! The label above the field should have been:",textLabel)

fieldOnPage=formybrowser.find_element(By.ID, "name")
textToEnter="Shawn"
fieldOnPage.send_keys(textToEnter)
fieldOnPage.send_keys(Keys.TAB)
fieldTextContent=fieldOnPage.get_property("value")
if fieldTextContent == textToEnter:
    print ("The text field contains the correct entered value of",fieldTextContent)
else:
    print ("ERROR! The text field does NOT contain the correct entered value of",fieldTextContent)

buttonOnPage=formybrowser.find_element(By.ID, "button")
btnEnabled=buttonOnPage.is_enabled()
if btnEnabled == True:
    print ("The button on the page is enabled...this is correct. The enabled status is",btnEnabled)
else:
    print ("ERROR! The button on the page is disabled when it should be enabled, status is:",btnEnabled)

btnColor=Color.from_string(buttonOnPage.value_of_css_property('background-color'))
print("The color of the button is:",btnColor)
btnLabel=buttonOnPage.get_property("textContent")
buttonOnPage.click()

time.sleep(4) #Used only for testing purposes to see what is on the screen before the window is closed