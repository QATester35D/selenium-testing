from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Radio Button\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 500)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Radio Button")
keyMousePress.click()

element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "radio-button-1")))

#########################################################################
#Process through radio buttons getting checked status and the label text
#########################################################################
radioButtonList=formybrowser.find_elements(By.NAME, "exampleRadios") #The actual radio button circle itself
radioButtonLabelList=formybrowser.find_elements(By.CLASS_NAME, "form-check-label") #The label associated with each radio button
listSize=len(radioButtonList)
labelListSize=len(radioButtonLabelList)
if listSize == labelListSize:
    ctr=1
    for a in range(listSize):
        radioButton=formybrowser.find_elements(By.NAME, "exampleRadios")[a]
        radioButtonVal=radioButton.get_attribute("value")
        rbText=radioButtonLabelList[a].text
        print("The label for radio button #",ctr,"is:",rbText)
        radioButtonChk=radioButton.get_attribute("checked")
        if radioButtonChk:
            print("The radio button",radioButtonVal,"is checked/selected, value is", radioButtonChk)
        else:
            print("The radio button",radioButtonVal,"is NOT checked/selected, value is", radioButtonChk)
        ctr += 1
else:
    print("The sizes of the two arrays should be the same, they are not, so exiting out.")

##########################################################################
#Click through the list
##########################################################################
formybrowser.find_elements(By.NAME, "exampleRadios")[1].click() #select "Radio button 2"
time.sleep(1)
formybrowser.find_elements(By.NAME, "exampleRadios")[2].click() #select "Radio button 3"
time.sleep(1)
formybrowser.find_elements(By.NAME, "exampleRadios")[0].click() #select "Radio button 1"
time.sleep(1)
formybrowser.find_elements(By.NAME, "exampleRadios")[2].click() #select "Radio button 1"
time.sleep(1)
##########################################################################
#Approach #2 - get the list of radio buttons and process through the list
##########################################################################
radio_list = formybrowser.find_elements(By.NAME,"exampleRadios")
time.sleep(2)
# 2. Using for loop iterate the list object and click on required option
for rbutton in radio_list:
    rbutton_t = rbutton.get_attribute("value")
    print(rbutton_t)
    rbutton.click()
    time.sleep(1)

time.sleep(2) #Used only for testing purposes to see what is on the screen before the window is closed