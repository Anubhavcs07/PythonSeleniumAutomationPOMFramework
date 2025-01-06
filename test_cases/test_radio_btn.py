from Base.BaseClass import BaseClass
from PageObjects.RadioPageObject import RadioPageObject
import allure

class TestRadio(BaseClass):
    
    @allure.title("Clicking Radio Button")
    @allure.description("Clicking and verifying the raio button is clicked")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_radio(self):
        radioPageObject = RadioPageObject(self.driver)
        value = radioPageObject.radio_find_element()
        radioPageObject.capture_screenshot("Radio Button Clicked")
        value == "True", "Radio button is selected"
        