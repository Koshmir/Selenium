import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\Admin\\PycharmProjects\\python_selenium\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print("Enter Cart")

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1 GOOD")

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product 1 Good")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Checout")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Igor")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Koshman")
print("Input Last Name")

ZIP = driver.find_element(By.XPATH, "//input[@id='postal-code']")
ZIP.send_keys("Boston,Lenina street,23")
print("Input ZIP")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish Product 1"""

finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Cart Product 1 GOOD")

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Finish Price Product 1 GOOD")

summery_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summery_price = summery_price.text
print(value_summery_price)

item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summery_price == item_total
print("Total summary price Good")




time.sleep(6)
driver.close()
