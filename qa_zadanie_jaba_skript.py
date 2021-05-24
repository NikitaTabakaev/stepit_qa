from selenium import webdriver
import time
from math import log, sin

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/execute_script.html")

    numb = int(browser.find_element_by_xpath("//span[@id = 'input_value']").text)

    button = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("answer").send_keys(str(log(abs(12 * sin(numb)))))

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    button_2 = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    button_2.click()

finally:
    time.sleep(5)
    browser.quit()