from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import pytest
import allure

@pytest.mark.usefixtures("setup")
class BaseClass:
    def find_element_function(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator[0], locator[1])))
    
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

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator[0], locator[1])))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def hover_action(self, locator):
        hoverable = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator[0], locator[1])))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def is_text_visible(self, locator):
        element = self.find_element_function(locator)
        return element.text
    
    def switch_tabs(self, window):
        self.driver.switch_to.window(window)

    def get_page_title(self):
        return self.driver.title
    
    def switch_frame(self, iframe):
        self.driver.switch_to.frame(iframe)
    
    # def get_drop_down_text(self):
    #     return self.