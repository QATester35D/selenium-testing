from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

print("Working with selenium test pages - submit buttons") #The main page is: https://www.selenium.dev/selenium/web/
# browser.get("https://www.selenium.dev/selenium/web/click_tests/html5_submit_buttons.html") #This is the direct page
browser.get("https://www.selenium.dev/selenium/web/")
browser.set_window_size(550, 692)

element= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ul/li[30]/a")))
browser.find_element(By.LINK_TEXT,"click_tests/html5_submit_buttons.html").is_displayed()
buttonLinkText=browser.find_element(By.LINK_TEXT,"click_tests/html5_submit_buttons.html")
buttonLinkText.click()

element=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'name')))
nameTextField = browser.find_element(By.NAME,"name")
nameTextField.clear()
nameTextField.send_keys("Shawn") # Find the label element 

internalExplicitButton=browser.find_element(By.ID, "internal_explicit_submit")
label = internalExplicitButton.text
print("internal_explicit_submit label is: ",label)
lineHeight = internalExplicitButton.value_of_css_property("line-height")
print("internal_explicit_submit line height is: ",lineHeight)
size = internalExplicitButton.value_of_css_property("font-size")
print("internal_explicit_submit size is: ",size)
fontUsed = internalExplicitButton.value_of_css_property("font-family")
print("internal_explicit_submit font being used is: ",fontUsed)
padding = internalExplicitButton.value_of_css_property("padding")
print("internal_explicit_submit padding being used is: ",padding)
color = internalExplicitButton.value_of_css_property("color")
print("internal_explicit_submit color being used is: ",color)

internalExplicitButton.click()
browser.back()

internalImplicitButton=browser.find_element(By.ID, "internal_implicit_submit")
label=internalImplicitButton.text
print("internal_implicit_submit label is: ",label)
internalImplicitButton.click()
browser.back()

spannedSubmitButton=browser.find_element(By.ID, "internal_span_submit")
label=spannedSubmitButton.text
print("internal_span_submit label is: ",label)
spannedSubmitButton.click()
browser.back()

externalExplicitButton=browser.find_element(By.ID, "external_explicit_submit")
label = externalExplicitButton.text
print("external_explicit_submit label is: ",label)
externalExplicitButton.click()
browser.back()
externalImplicitButton=browser.find_element(By.ID, "external_implicit_submit")
label = externalImplicitButton.text
print("external_implicit_submit label is: ",label)
externalImplicitButton.click()
browser.back()
browser.back()

element= WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ul/li[5]/a")))
browser.find_element(By.LINK_TEXT,"attributes.html").is_displayed()
buttonLinkText=browser.find_element(By.LINK_TEXT,"attributes.html")
browser.find_element(By.LINK_TEXT,"attributes.html").click()
browser.find_element(By.CLASS_NAME, "cur")
browser.back()
browser.quit()
##################################
# Using another site now - Formy #
##################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the Buttons page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(550, 692)
buttonsLink=formybrowser.find_element(By.LINK_TEXT, "Buttons")
buttonsLink.click()
# browser.switch_to.window("https://formy-project.herokuapp.com/buttons")
primaryButton=formybrowser.find_element(By.CLASS_NAME, "btn-primary")
label = primaryButton.text
print ("The Formy blue Primary button label is: ",label)
color = primaryButton.value_of_css_property("color")
print ("The Formy blue Primary button color is: ",color)
lineHeight = primaryButton.value_of_css_property("line-height")
print ("The Formy blue Primary button line height is: ",lineHeight)
fontSize = primaryButton.value_of_css_property("font-size")
print ("The Formy blue Primary button font size is: ",fontSize)
fontType = primaryButton.value_of_css_property("font-family")
print ("The Formy blue Primary button font size is: ",fontType)

primaryButton.click()
successButton=formybrowser.find_element(By.CLASS_NAME, "btn-success")
successButton.click()
infoButton=formybrowser.find_element(By.CLASS_NAME, "btn-info")
infoButton.click()
warningButton=formybrowser.find_element(By.CLASS_NAME, "btn-warning")
warningButton.click()
dangerButton=formybrowser.find_element(By.CLASS_NAME, "btn-danger")
dangerButton.click()
linkObject=formybrowser.find_element(By.CLASS_NAME, "btn-link")
linkObject.click()
leftButton=formybrowser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .btn:nth-child(1)")
leftButton.click()
middleButton=formybrowser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .btn:nth-child(2)")
middleButton.click()
rightButton=formybrowser.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(3)")
rightButton.click()
oneButton=formybrowser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .col-sm-8 > .btn-group > .btn:nth-child(1)")
oneButton.click()
twoButton=formybrowser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .btn:nth-child(2)")
dropdownItem=formybrowser.find_element(By.ID, "btnGroupDrop1")
dropdownItem.click()
dropdownLink1=formybrowser.find_element(By.LINK_TEXT, "Dropdown link 1")
dropdownLink1.click()
dropdownItem=formybrowser.find_element(By.ID, "btnGroupDrop1")
dropdownItem.click()
dropdownLink2=formybrowser.find_element(By.LINK_TEXT, "Dropdown link 2")
dropdownLink2.click()
formybrowser.back()
formybrowser.quit()