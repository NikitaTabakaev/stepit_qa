import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test:

    links = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]
    message = ""

    @pytest.mark.parametrize('link', links)
    def test_find_hide_message(self, browser, link):

        browser.get(link)
        time.sleep(10)

        browser.find_element_by_xpath("//textarea").send_keys(str(math.log(int(time.time()))))
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
        ).click()

        t = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//pre[@class = 'smart-hints__hint']"))).text

        if t != "Correct!":
            self.message += t

        print(self.message)