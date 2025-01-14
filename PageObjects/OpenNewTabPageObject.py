from Base.BaseClass import BaseClass
from Locators.OpenNewTab import OpenNewTab
from selenium.webdriver.remote.webelement import WebElement
import time

class OpenNewTabPageObject(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def click_on_button(self):
        original_window = self.driver.current_window_handle
        new_tab_element = self.find_element_function(OpenNewTab.OPEN_TAB_PATH)
        self.click_element(new_tab_element)
        new_window = self.driver.window_handles
        self.switch_tabs(new_window[-1])
        self.capture_screenshot("new tab")
        return self.get_page_title()
        # self.switch_tabs(original_window)
        # self.capture_screenshot("old tab")