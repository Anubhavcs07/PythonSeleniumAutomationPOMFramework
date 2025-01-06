from Base.BaseClass import BaseClass
from Locators.StaticDropDown import StaticDropDownLocators

class StaticDropDownPageObject(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.staticDropDownLocators = StaticDropDownLocators()

    def get_drop_down_element(self):
        web_elem = self.find_element_function(self.staticDropDownLocators.ID_DROP_DOWN)
        return web_elem

    def choose_drop_down_value(self, web_elem):
        # web_elem = self.get_drop_down_element()
        select = self.select_drop_down(web_elem)
        self.choose_value(select, self.staticDropDownLocators.OPTION_SELECTED)

    