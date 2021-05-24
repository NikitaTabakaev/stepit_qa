import time
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:

    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")) # ожидание пока текст станет 100

    browser.find_element_by_id("book").click()

    numb = int(browser.find_element_by_xpath("//span[@id = 'input_value']").text)
    browser.find_element_by_xpath("//input[@id = 'answer']").send_keys(str(log(abs(12 * sin(numb)))))

    browser.find_element_by_id("solve").click()

    # делаю скролы на нужные элементы
    inp = browser.find_element_by_xpath("//input[@id = 'answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)

    button = browser.find_element_by_xpath("//button[@id = 'solve']")
    browser.execute_script("return arguments[1].scrollIntoView(true);", button)
    time.sleep(5)
finally:

    time.sleep(5)
    browser.quit()