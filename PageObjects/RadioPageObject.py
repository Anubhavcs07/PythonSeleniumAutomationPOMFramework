from Base.BaseClass import BaseClass
from Locators.RadioButton import RadioButtonLocator

class RadioPageObject(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.radioButton = RadioButtonLocator()

    def radio_find_element(self):
        web_elem = self.find_element_function(self.radioButton.RADIOBTN)
        self.click_element(web_elem)
    
    def screenshot_capture(self, screenshotName):
        self.capture_screenshot(screenshotName)