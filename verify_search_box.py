# This script finds the search products field

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('http://bootcamp.store.supersqa.com/my-account/')

# Find element and save it
# search_prod_elem = driver.find_elements(By.ID, 'woocommerce-product-search-field-0')
search_prod_elem = driver.find_elements(By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
placeholder = search_prod_elem[0].get_attribute('placeholder')
# print(placeholder)
if placeholder == 'Search products…':
    print(f"The correct text for the search box is => {placeholder}")
else:
    print("There was no matching text")

# breakpoint()
