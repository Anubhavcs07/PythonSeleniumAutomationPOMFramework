from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import allure


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Radio Button Click")
@allure.description("This test is to validate the Radio button check")
@allure.severity(allure.severity_level.CRITICAL)
def test_radio_btn_click(setup):
    # driver.find_element(By.XPATH, '//input[@value="radio1"]').click()
    driver = setup
    xpath_radio_btn = (By.XPATH, '//input[@value="radio1"]')
    radio_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(xpath_radio_btn))
    radio_btn.click()
    # screenshot = driver.get_screenshot_as_png()
    # allure.attach(screenshot, name="RadioButton", attachment_type=allure.attachment_type.PNG)
    with allure.step("Capturing radio button"):
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="RadioButton", attachment_type=allure.attachment_type.PNG)
    assert driver.find_element(By.XPATH, '//input[@value="radio1"]').is_selected() == True, "Radio button is clicked"
    if driver.find_element(By.XPATH, '//input[@value="radio1"]').is_selected():
        print("clicked")
    else:
        print("not selected")

def test_select_static_drop_down(setup):
    driver = setup
    id_drop_down = "dropdown-class-example"
    drop_down_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_drop_down)))
    # select = Select(driver.find_element(By.ID, id_drop_down))
    select = Select(drop_down_element)
    select.select_by_visible_text("Option1")
    selected_option = select.first_selected_option.text
    print("selected option", selected_option)
    assert selected_option == "Option1", "Option1 selected"

def test_checkbox_clicked(setup):
    driver = setup
    id_checkbox = "checkBoxOption1"
    chkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_checkbox)))
    time.sleep(3)
    chkbox.click()

    assert chkbox.is_selected()

def test_dynamic_dropdowns(setup):
    driver = setup
    id_drop_down = "#autocomplete.inputs"
    id_select = "ui-id-1"
    
    drp_down = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, id_drop_down)))
    drp_down.click()
    drp_down.send_keys("India")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_select)))
    time.sleep(4)

def test_alert_box(setup):
    driver = setup
    id_alert_input = "name"
    id_alert_btn = "alertbtn"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_alert_input))).send_keys("Anubhav")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_alert_btn))).click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    assert alert_text == "Hello Anubhav, share this practice page and share your knowledge"

def test_hide_show_box(setup):
    driver = setup
    id_hide_btn = "hide-textbox"
    id_show_btn = "show-textbox"
    id_input_box = "displayed-text"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_hide_btn))).click() #hides the input box
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_show_btn))).click() # shows the input box
    input_box = driver.find_element(By.ID, id_input_box)
    assert input_box.is_displayed(), "Input box is displayed"
    print("Input box is displayed")

def test_new_tab_handles(setup):
    driver = setup
    new_tab_btn = "opentab"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, new_tab_btn))).click()
    time.sleep(5)
    window_handles = driver.window_handles
    original_windows = driver.current_window_handle
    driver.switch_to.window(window_handles[-1])
    WebDriverWait(driver, 10).until(EC.title_contains("QAClick Academy - A Testing Academy to Learn, Earn and Shine"))
    driver.close()

def test_product_table(setup):
    driver = setup
    id_table = "product"
    xpath_table = '//table[@id="product"]//tr'
    table_data = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath_table)))
    for row in table_data:
        col = row.find_elements(By.XPATH, "./td")
        
        for c in col:
            print(c.text)

def test_open_new_window(setup):
    driver = setup
    id_new_win_btn = "openwindow"
    original_win = driver.current_window_handle
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id_new_win_btn))).click()
    win_handle = driver.window_handles
    driver.switch_to.window(win_handle[-1])
    driver.maximize_window()
    time.sleep(5)
    assert driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine"
    driver.close()
    driver.switch_to.window(original_win)

def test_handle_iframes(setup):
    driver = setup
    id_iframe = "courses-iframe"
    iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_iframe)))
    setup.driver.execute_script("arguments[0].scrollIntoView(true);", iframe_element)
    driver.switch_to.frame(iframe_element)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div.header-upper").click()

def test_mouse_hover(setup):
    driver = setup
    id_mouse_hover = "mousehover"
    select = 'Top'
    id_select = f"//div//a[text()='{select}']"
    hover_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_mouse_hover)))
    driver.execute_script("arguments[0].scrollIntoView(true);", hover_btn)
    hover_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_mouse_hover)))
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).click().perform()
    driver.find_element(By.XPATH, id_select).click()
