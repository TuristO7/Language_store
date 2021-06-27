from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link =' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_bucket_button(browser):
    browser.get(link)
    WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "No add to cart button on page")