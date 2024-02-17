import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

loyalty = driver.find_element(By.XPATH, "//a[@aria-label='Menu LOYALTY']")
loyalty01 = driver.find_element(By.XPATH, "//a[@aria-label='Sub Menu of Loyalty, Irctc Sbi Card.']//span[@class='list_text'][normalize-space()='IRCTC SBI Credit Card']")
loyalty02 = driver.find_element(By.XPATH,
                                 "//li[@class='menu-list header-icon-menu ng-star-inserted']//ul[@class='box-shadow']//li//ul[@class='child-drop']//li//span[@class='list_text'][normalize-space()='About IRCTC SBI Credit Card']")
Action = ActionChains(driver)

Action.move_to_element(loyalty).move_to_element(loyalty01).move_to_element(loyalty02).click().perform()

time.sleep(2)

# driver = webdriver.Chrome()
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# LOYALTY = driver.find_element(By.XPATH, "//a[@aria-label='Menu LOYALTY']")
# LOYALTY1 = driver.find_element(By.XPATH,
#                     "//a[@aria-label='Sub Menu of Loyalty, Irctc Sbi Card.']//span[@class='list_text'][normalize-space()='IRCTC SBI Credit Card']")
# LOYALTY2 = driver.find_element(By.XPATH, "//li[@class='menu-list header-icon-menu ng-star-inserted']//ul[@class='box-shadow']//li//ul[@class='child-drop']//li//span[@class='list_text'][normalize-space()='About IRCTC SBI Credit Card']")
# Action =ActionChains(driver)
# Action.move_to_element(LOYALTY).move_to_element(LOYALTY1).move_to_element(LOYALTY2).click().perform()
# time.sleep(3)
# driver.close()