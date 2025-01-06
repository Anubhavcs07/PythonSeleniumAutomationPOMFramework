from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

@pytest.mark.usefixtures("setup")
class BaseClass:
    def find_element_function(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    
    def click_element(self, web_element):
        web_element.click()

    def element_selected(self, web_element):
        return web_element.is_selected()
    
    def capture_screenshot(self, screenshotName):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, attachment_type=allure.attachment_type.PNG, name=screenshotName)

    def select_drop_down(self, web_element):
        return Select(web_element)

    def choose_value(self, select ,text):
        select.select_by_visible_text(text)

    # def get_drop_down_text(self):
    #     return self.