from selenium import webdriver
import time

try:
    # Положить в одну папку geckodriver.exe с этим кодом и запустить.
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']").send_keys("123")
    browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']").send_keys("123")
    browser.find_element_by_xpath("//input[@placeholder = 'Input your email']").send_keys("123")

    browser.find_element_by_xpath("//button[text() = 'Submit']").click()
    time.sleep(5)

    assert "Congratulations! You have successfully registered!" == \
           browser.find_element_by_xpath("//h1[text() = 'Congratulations! You have successfully registered!']").text

finally:
    time.sleep(10)
    browser.quit()
