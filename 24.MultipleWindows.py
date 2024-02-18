import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
print(driver.title)

driver.find_element(By.XPATH, "//*[normalize-space()='Click Here']").click()
select_window = driver.window_handles


driver.switch_to.window(select_window[1])
print(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/h3[1]").text)


driver.switch_to.window(select_window[0])
print(driver.find_element(By.XPATH, "//*[normalize-space()='Opening a new window']").text)

driver.close()
