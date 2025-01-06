import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome import service


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()