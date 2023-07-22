from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('http://bootcamp.store.supersqa.com/my-account/')


# find the username field
# find element and save it
username_elem = driver.find_element(By.ID, 'reg_email')
# assert username_elem.is_enabled(), "The username field is not displayed"
if not username_elem.is_displayed():
    raise Exception("Username field is not displayed")

# input email address into the field
username_elem.send_keys('embelle@supersqa.com')


# find the password field
passwd_field = driver.find_element(By.XPATH, '//*[@id="reg_password"]')
# input the password into the field

passwd_field.send_keys('boogabooga1@@')
# click on the Registration button

register_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
reg_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
reg_btn.click()
breakpoint()
