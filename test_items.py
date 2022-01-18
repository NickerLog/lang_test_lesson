from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_lang_switch(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(15)  # time for look at browser window
    assert expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')), \
        'Cannot locate button on page'
