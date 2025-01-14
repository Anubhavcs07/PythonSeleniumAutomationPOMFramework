from selenium.webdriver.common.by import By

class HoverOver:
    HOVER_ELEMENT_ID = (By.ID, "mousehover")
    TOP_LINK = (By.LINK_TEXT, "Top")
    RELOAD_LINK = (By.LINK_TEXT, "Reload")
    TEXT_DISPLAYED = (By.TAG_NAME, "h1")
    TEXT = "Practice Page"
