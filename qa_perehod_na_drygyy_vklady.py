import time
from selenium import webdriver
from math import log, sin
try:
    browser = webdriver.Firefox()

    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_class_name("trollface").click()

    # переход на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # new_window = browser.window_handles[1] # вариант с переменной
    # browser.switch_to.window(new_window)

    time.sleep(2)
    numb = int(browser.find_element_by_xpath("//span[@id = 'input_value']").text)
    browser.find_element_by_xpath("//input[@id = 'answer']").send_keys(str(log(abs(12 * sin(numb)))))
    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()