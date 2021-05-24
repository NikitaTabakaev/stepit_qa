from selenium import webdriver
import time
from math import log, sin

try:

    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_class_name("btn").click()

    browser.switch_to.alert.accept()
    time.sleep(1)
    numb = int(browser.find_element_by_xpath("//span[@id = 'input_value']").text)
    browser.find_element_by_xpath("//input[@id = 'answer']").send_keys(str(log(abs(12 * sin(numb)))))

    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()