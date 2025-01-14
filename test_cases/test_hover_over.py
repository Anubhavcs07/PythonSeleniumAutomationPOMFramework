from Base.BaseClass import BaseClass
from PageObjects.HoverOverPageObject import HoverOverPageObject
import allure

class TestHoverOver(BaseClass):
    @allure.title("Testing hover")
    @allure.description("this is test to check the hover element")
    @allure.severity("CRITICAL")
    def test_hover_over(self):
        hoverPageObject = HoverOverPageObject(self.driver)
        hoverPageObject.perform_click_on_top()
        text = hoverPageObject.check_text_is_displayed()
        assert text == "Practice Page"