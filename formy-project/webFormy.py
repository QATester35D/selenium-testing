from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import timedelta, date
import time

#########################################################################
#Setting up a tuple to make this test script a data driven test with data
#########################################################################
formTestData = [("Jerry","Seinfeld","Comedian","Grad","Male","4","+40"),
    ("Cosmos","Kramer","Schmooch","HighSchool","NotSay","1","0"),
    ("George","Costanza","Yankees Executive","College","Male","2","+20"),
    ("Elaine","Benes","Copy Editor","Grad","Female","1","-12"),
    ("Estelle","Costanza","Mom","HighSchool","Female","4","+42"),
    ("Francis","Newman","Postman","HighSchool","NotSay","3","-24"),
    ("Helen","Seinfeld","Mom","Grad","Female","2","-2")
]

def findDate (dateValue):
    # -x = subtract number from today's date, 0 = today's date, +x = add number to today's date
    dateConversion=len(dateValue)
    if dateConversion == 1:
        dateManipulation = "today"
    else:
        symbolForDate=dateValue[:1]
        if symbolForDate == "+":
            dateManipulation = "add"
        elif symbolForDate == "-":
            dateManipulation = "sub"
        digitForDate=int(dateValue[1:])

    match dateManipulation:
        case "today":
            addToDate = date.today()
            newDate=str(addToDate.month) +"/"+ str(addToDate.day) +"/"+ str(addToDate.year)
        case "add":
            addToDate = date.today() + timedelta(digitForDate)
            newDate=str(addToDate.month) +"/"+ str(addToDate.day) +"/"+ str(addToDate.year)
        case "sub":
            subFromDate = date.today() - timedelta(digitForDate)
            newDate=str(subFromDate.month) +"/"+ str(subFromDate.day) +"/"+ str(subFromDate.year)
        case _:
            print("Something went wrong with converting date.")
    
    return newDate

#########################################################################
#Test Case to fill out form
#########################################################################
formybrowser = webdriver.Firefox()
print("Now working with the Formy webpages - the \"Complete Web Form\" page")
formybrowser.get("https://formy-project.herokuapp.com/")
formybrowser.set_window_size(800, 800)
keyMousePress=formybrowser.find_element(By.LINK_TEXT, "Complete Web Form")
keyMousePress.click()

i=1
#get tuple size
for sublist in formTestData:
    if i==1:
        i+=1
    else:
        formybrowser.get("https://formy-project.herokuapp.com/form")

    element= WebDriverWait(formybrowser, 10).until(EC.presence_of_element_located((By.ID, "datepicker")))

    firstName=formybrowser.find_element(By.ID, "first-name") #text field
    lastName=formybrowser.find_element(By.ID, "last-name") #text field
    jobTitle=formybrowser.find_element(By.ID, "job-title") #text field
    edRb1HighSchool=formybrowser.find_element(By.ID, "radio-button-1") #radio button
    edRb2College=formybrowser.find_element(By.ID, "radio-button-2") #radio button
    edRb3Grad=formybrowser.find_element(By.ID, "radio-button-3") #radio button
    sexMale=formybrowser.find_element(By.ID, "checkbox-1") #checkbox
    sexFemale=formybrowser.find_element(By.ID, "checkbox-2") #checkbox
    sexNotSay=formybrowser.find_element(By.ID, "checkbox-3") #checkbox
    yrsExp=formybrowser.find_element(By.ID, "select-menu") #dropbox
    someDate=formybrowser.find_element(By.ID, "datepicker") #datepicker
    submitButton=formybrowser.find_element(By.CLASS_NAME,"btn-primary")
    
    firstName.send_keys(sublist[0])
    lastName.send_keys(sublist[1])
    jobTitle.send_keys(sublist[2])
 
    #Education
    match sublist[3]:
        case "HighSchool":
            edRb1HighSchool.click()
        case "College":
            edRb2College.click()
        case "Grad":
            edRb3Grad.click()
        case _:
            print("The data value isn't a valid one for education.")
    #Sex
    match sublist[4]:
        case "Male":
            sexMale.click()
        case "Female":
            sexFemale.click()
        case "NotSay":
            sexNotSay.click()
        case _:
            print("The data value isn't a valid one for education.")

    #Years of experience
    # yrsExp.select_by_index(sublist[5])
    formybrowser.find_element(By.ID, "select-menu") #Form Filling Dropdown Options
    dropdown = Select(formybrowser.find_element(By.ID,"select-menu"))
    dropdown.select_by_value(sublist[5])

    #Date
    testData=sublist[6]
    dateToSelect=findDate(testData)
    someDate.send_keys(dateToSelect)
    someDate.send_keys(Keys.TAB)

    time.sleep(2) #Used only for testing purposes to see what is on the screen before the window is closed
    submitButton.click()
    #Verify submission
    formSubmissionAlert=formybrowser.find_element(By.CLASS_NAME, "alert-success") 
    alertMsg=formSubmissionAlert.get_property("innerText")
    # alertMsg=formSubmissionAlert.text()
    expectedMessage="The form was successfully submitted!"
    if alertMsg == expectedMessage:
        print("Submission successful.")
    else:
        print("Error with submitting form. The message displayed is:",alertMsg)
    formybrowser.get("https://formy-project.herokuapp.com/form")

print("Done with data driven test on form submission.")