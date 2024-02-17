import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver. maximize_window()
Right_clk = driver.find_element(By.XPATH, "//*[text()='right click me']")

Action = ActionChains(driver)

Action.context_click(Right_clk).perform()

time.sleep(3)