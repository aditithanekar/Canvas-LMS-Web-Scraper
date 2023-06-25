from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_eight_components():
    driver.get("https://learn.zybooks.com/zybook/UCRCS010CSpring2023")
    driver.implicitly_wait(1)