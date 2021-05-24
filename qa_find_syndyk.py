from selenium import webdriver
import time
import math

try:
    browser = webdriver.Firefox()

    browser.get("http://suninjuly.github.io/get_attribute.html")

    numb = browser.find_element_by_id("treasure").get_attribute("valuex")
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(numb))))))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_xpath("//button[@class = 'btn btn-default']").click()

finally:
    time.sleep(7)
    browser.quit()