from Base.BaseClass import BaseClass
from PageObjects.OpenNewTabPageObject import OpenNewTabPageObject

class TestNewTab(BaseClass):
    def test_new_tab(self):
        openNewTab = OpenNewTabPageObject(self.driver)
        title = openNewTab.click_on_button()
        assert title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine", "title is matching"