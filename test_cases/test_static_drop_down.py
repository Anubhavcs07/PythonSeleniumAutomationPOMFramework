import allure
from Base.BaseClass import BaseClass
from PageObjects.StaticDropDownPageObject import StaticDropDownPageObject

class TestStaticDropDown(BaseClass):
    def test_static_drop_down(self):
        staticDropDownPageObject = StaticDropDownPageObject()
        web_elem = staticDropDownPageObject.get_drop_down_element()
        staticDropDownPageObject.choose_drop_down_value(web_elem)