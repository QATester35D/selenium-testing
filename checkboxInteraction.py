from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the Buttons page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(550, 692)
buttonsLink=formybrowser.find_element(By.LINK_TEXT, "Checkbox")
buttonsLink.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "checkbox-1")))
formybrowser.find_element(By.ID, "checkbox-1").is_displayed()
checkbox1=formybrowser.find_element(By.ID, "checkbox-1")
checkbox2=formybrowser.find_element(By.ID, "checkbox-2")
checkbox3=formybrowser.find_element(By.ID, "checkbox-3")
checkbox1Status=formybrowser.find_element(By.ID,"checkbox-1").is_selected()
checkbox2Status=formybrowser.find_element(By.ID,"checkbox-2").is_selected()
checkbox3Status=formybrowser.find_element(By.ID,"checkbox-3").is_selected()
print ("The Formy checkbox #1 checkbox status is: ",checkbox1Status)
print ("The Formy checkbox #2 checkbox status is: ",checkbox2Status)
print ("The Formy checkbox #3 checkbox status is: ",checkbox3Status)

fontType = checkbox1.value_of_css_property("font-family")
print ("The Formy checkbox #1 font type is: ",fontType)
fontSize = checkbox1.value_of_css_property("font-size")
print ("The Formy checkbox #1 font size is: ",fontSize)
fontWeight = checkbox1.value_of_css_property("font-weight")
print ("The Formy checkbox #1 font-weight is: ",fontWeight)
lineHeight = checkbox1.value_of_css_property("line-height")
print ("The Formy checkbox #1 line height is: ",lineHeight)
color = checkbox1.value_of_css_property("color")
print ("The Formy checkbox #1 color is: ",color)
textAlign = checkbox1.value_of_css_property("text-align")
print ("The Formy checkbox #1 text-align is: ",textAlign)
backgroundColor = checkbox1.value_of_css_property("background-color")
print ("The Formy checkbox #1 background color is: ",backgroundColor)
checkbox1.click()
checkbox2.click()
checkbox1Status=formybrowser.find_element(By.ID,"checkbox-1").is_selected()
checkbox2Status=formybrowser.find_element(By.ID,"checkbox-2").is_selected()
print ("The Formy checkbox #2 checkbox status is: ",checkbox2Status)
checkbox1.click() #unchecking checkbox1
checkbox1Status=formybrowser.find_element(By.ID,"checkbox-1").is_selected() 
print ("The Formy checkbox #1 checkbox status is: ",checkbox1Status)
checkbox3.click()
checkbox3Status=formybrowser.find_element(By.ID,"checkbox-3").is_selected()
print ("The Formy checkbox #3 checkbox status is: ",checkbox3Status)
checkbox2.click() #unchecking checkbox2
checkbox2Status=formybrowser.find_element(By.ID,"checkbox-2").is_selected()
print ("The Formy checkbox #2 checkbox status is: ",checkbox2Status)
time.sleep(4) #used just to see the status of the checkboxes at the end