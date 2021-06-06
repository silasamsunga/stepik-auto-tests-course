from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(q):
  return str(math.log(abs(12*math.sin(int(q)))))


try:
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_xpath("//*[@id='input_value']")
    x1 = x.text
    browser.find_element_by_id("answer").send_keys(calc(x1))
    button1 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

    #browser.find_element_by_id("solve").clicl


finally:
    sleep(15)
    browser.quit()