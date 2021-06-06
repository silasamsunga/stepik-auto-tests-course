from selenium import webdriver
from time import sleep
import math

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/redirect_accept.html"

def calc(q):
  return str(math.log(abs(12*math.sin(int(q)))))

try:
    browser.get(link)
    browser.find_element_by_xpath("/html/body/form/div/div/button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    sleep(3)
    x = browser.find_element_by_xpath("//*[@id='input_value']")
    x1 = x.text
    browser.find_element_by_xpath("//*[@id='answer']").send_keys(calc(x1))
    browser.find_element_by_xpath("/html/body/form/div/div/button").click()

finally:
    sleep(10)
    browser.quit()