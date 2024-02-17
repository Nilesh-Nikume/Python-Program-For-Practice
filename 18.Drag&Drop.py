import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
source_element = driver.find_element(By.XPATH,"//div[@id='draggable']")
destination_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

Action = ActionChains(driver)
Action.drag_and_drop(source_element,destination_element).perform()
time.sleep(3)