from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClickingButtons():
#   def setup_method(self, method):
  def __init__(self):
    # self.driver = webdriver.Firefox()
    options = webdriver.FirefoxOptions()
    self.driver = webdriver.Firefox(options=options)
    # self.vars = {}

#   def test_basic_options():
#     options = webdriver.FirefoxOptions()
#     driver = webdriver.Firefox(options=options)

  def teardown_method(self, method):
    self.driver.quit()

browserDriver = TestClickingButtons()

browserDriver.driver.get("https://www.selenium.dev/selenium/web/click_tests/html5_submit_buttons.html")
browserDriver.driver.set_window_size(550, 692)
nameTextField=browserDriver.driver.find_element(By.ID, "name")
nameTextField.click()
nameTextField.send_keys("Shawn") # Find the label element 

internalExplicitButton=browserDriver.driver.find_element(By.ID, "internal_explicit_submit")
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
browserDriver.driver.back()

internalImplicitButton=browserDriver.driver.find_element(By.ID, "internal_implicit_submit")
label=internalImplicitButton.text
print("internal_implicit_submit label is: ",label)
internalImplicitButton.click()
browserDriver.driver.back()

spannedSubmitButton=browserDriver.driver.find_element(By.ID, "internal_span_submit")
label=spannedSubmitButton.text
print("internal_span_submit label is: ",label)
spannedSubmitButton.click()
browserDriver.driver.back()

externalExplicitButton=browserDriver.driver.find_element(By.ID, "external_explicit_submit")
label = externalExplicitButton.text
print("external_explicit_submit label is: ",label)
externalExplicitButton.click()
browserDriver.driver.back()

externalImplicitButton=browserDriver.driver.find_element(By.ID, "external_implicit_submit")
label = externalImplicitButton.text
print("external_implicit_submit label is: ",label)
externalImplicitButton.click()
browserDriver.driver.back()
browserDriver.driver.quit()

#Using another site now - Formy
formyBrowserDriver = TestClickingButtons()
formyBrowserDriver.driver.get("https://formy-project.herokuapp.com/")
formyBrowserDriver.driver.set_window_size(550, 692)
buttonsLink=formyBrowserDriver.driver.find_element(By.LINK_TEXT, "Buttons")
buttonsLink.click()
# browserDriver.driver.switch_to.window("https://formy-project.herokuapp.com/buttons")
primaryButton=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-primary")
primaryButton.click()
successButton=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-success")
successButton.click()
infoButton=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-info")
infoButton.click()
warningButton=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-warning")
warningButton.click()
dangerButton=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-danger")
dangerButton.click()
linkObject=formyBrowserDriver.driver.find_element(By.CLASS_NAME, "btn-link")
linkObject.click()
leftButton=formyBrowserDriver.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .btn:nth-child(1)")
leftButton.click()
middleButton=formyBrowserDriver.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .btn:nth-child(2)")
middleButton.click()
rightButton=formyBrowserDriver.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(3)")
rightButton.click()
oneButton=formyBrowserDriver.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .col-sm-8 > .btn-group > .btn:nth-child(1)")
oneButton.click()
twoButton=formyBrowserDriver.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .btn:nth-child(2)")
dropdownItem=formyBrowserDriver.driver.find_element(By.ID, "btnGroupDrop1")
dropdownItem.click()
dropdownLink1=formyBrowserDriver.driver.find_element(By.LINK_TEXT, "Dropdown link 1")
dropdownLink1.click()
dropdownItem=formyBrowserDriver.driver.find_element(By.ID, "btnGroupDrop1")
dropdownItem.click()
dropdownLink2=formyBrowserDriver.driver.find_element(By.LINK_TEXT, "Dropdown link 2")
dropdownLink2.click()
formyBrowserDriver.driver.quit()