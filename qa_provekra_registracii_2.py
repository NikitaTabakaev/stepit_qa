from selenium import webdriver
import time
import unittest


class TestReg(unittest.TestCase):

    def test_reg(self):

        browser = webdriver.Firefox()

        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']").send_keys("123")
        browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']").send_keys("123")
        browser.find_element_by_xpath("//input[@placeholder = 'Input your email']").send_keys("123")

        browser.find_element_by_xpath("//button[text() = 'Submit']").click()
        time.sleep(5)

        reg_text = browser.find_element_by_xpath("//h1[text() = 'Congratulations! You have successfully registered!']").text

        assert "Congratulations! You have successfully registered!" == reg_text

    def test_reg_2(self):

        browser = webdriver.Firefox()

        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']").send_keys("123")
        browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']").send_keys("123")
        browser.find_element_by_xpath("//input[@placeholder = 'Input your email']").send_keys("123")

        browser.find_element_by_xpath("//button[text() = 'Submit']").click()
        time.sleep(5)

        reg_text = browser.find_element_by_xpath("//h1[text() = 'Congratulations! You have successfully registered!']").text

        assert "Congratulations! You have successfully registered!" == reg_text


if __name__ == "__main__":
    unittest.main()
