from Base.BaseClass import BaseClass
from Locators.HoverOver import HoverOver


class HoverOverPageObject(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def perform_click_on_top(self):
        self.scroll_to_element(HoverOver.HOVER_ELEMENT_ID)
        self.hover_action(HoverOver.HOVER_ELEMENT_ID)
        self.capture_screenshot("hovering over button element")
        elem = self.find_element_function(HoverOver.TOP_LINK)
        self.click_element(elem)
    
    def check_text_is_displayed(self):
        text = self.is_text_visible(HoverOver.TEXT_DISPLAYED)
        self.capture_screenshot("at the top of the page")
        return text