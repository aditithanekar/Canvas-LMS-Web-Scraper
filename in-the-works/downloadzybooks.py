from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#the commented works! 
driver.get("https://www.zybooks.com/")
driver.implicitly_wait(10)

driver.find_element(By.ID, 'username').send_keys('athan014')
driver.find_element(By.ID, 'password').send_keys('4Mallets!')

sign_in_button = driver.find_element(By.TAG_NAME, "button")
sign_in_button.click()


for i in driver.find_elements(By.TAG_NAME,"option"):
    print(i.get_attribute("value"))
    print("hi")
#driver.find_element(By.NAME, 'device').click()

#driver.find_element(By.TAG_NAME, 'select').click()
# driver.find_element()

#select_element = driver.find_element(By.CLASS_NAME, "device-select-wrapper")
#select_element.click()

# options = driver.find_elements(By.TAG_NAME,"option")

# # Click on the second option
# options[1].click()

#driver.find_element(By.CSS_SELECTOR, "#login-form fieldset div select").click()
#driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/form/fieldset/div/select/option[2]").click()

