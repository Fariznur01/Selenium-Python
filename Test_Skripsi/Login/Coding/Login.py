from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://127.0.0.1:8000/')
time.sleep(4)
driver.maximize_window()

time.sleep(5)
#Cek jika username dan password diisi dengan benar
search_box = driver.find_element(By.NAME, "username")
search_box2 = driver.find_element(By.NAME, "password")

search_box.send_keys('admin')
time.sleep(3)
search_box2.send_keys('1234')
search_box.submit()

"""""
#Cek jika username dan password diisi dengan salah
search_box = driver.find_element(By.NAME, "username")
search_box2 = driver.find_element(By.NAME, "password")

search_box.send_keys('####')
search_box2.send_keys('####')
search_box.submit()
"""

""""
#Cek jika username dan password kosong 
search_box = driver.find_element(By.NAME, "username")
search_box2 = driver.find_element(By.NAME, "password")

search_box.submit()
"""

"""
Cek jumlah tag input
search_box = driver.find_elements(By.TAG_NAME,  "input")
print(len(search_box))
"""

#driver.find_element_by_id("").send_keys("uno")  # dengan  css id
#driver.find_element_by_name("username").send_keys("uno") #dengan  css name

