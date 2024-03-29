# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

class TestPrediksiDTC():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_prediksiDTC(self):
    # Test name: Prediksi DTC
    # Step # | name | target | value
    # 1 | open | http://127.0.0.1:8000/ | 
    self.driver.get("http://127.0.0.1:8000/")
    # 2 | setWindowSize | 1296x688 | 
    self.driver.set_window_size(1296, 688)
    # 3 | click | name=username |
    time.sleep(5)
    self.driver.find_element(By.NAME, "username").click()
    # 4 | type | name=username | admin
    self.driver.find_element(By.NAME, "username").send_keys("admin")
    # 5 | click | id=myInput | 
    self.driver.find_element(By.ID, "myInput").click()
    # 6 | type | id=myInput | 
    self.driver.find_element(By.ID, "myInput").send_keys("#####")
    # 7 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 8 | click | css=#dtc > .bx | 
    self.driver.find_element(By.CSS_SELECTOR, "#dtc > .bx").click()
    # 9 | click | linkText=Tambah Testing Simpan | 
    self.driver.find_element(By.LINK_TEXT, "Tambah Testing Simpan").click()
    # 10 | click | id=id_name | 
    self.driver.find_element(By.ID, "id_name").click()
    # 11 | type | id=id_name | Test01
    #self.driver.find_element(By.ID, "id_name").send_keys("Test01")
    # 12 | type | id=id_name | Test10
    self.driver.find_element(By.ID, "id_name").send_keys("Test10")
    # 13 | click | id=id_Radius_mean | 
    self.driver.find_element(By.ID, "id_Radius_mean").click()
    # 14 | type | id=id_Radius_mean | 20.57
    self.driver.find_element(By.ID, "id_Radius_mean").send_keys("20.57")
    # 15 | click | id=id_Texture_mean | 
    self.driver.find_element(By.ID, "id_Texture_mean").click()
    # 16 | type | id=id_Texture_mean | 17.77
    self.driver.find_element(By.ID, "id_Texture_mean").send_keys("17.77")
    # 17 | click | id=id_Perimeter_mean | 
    self.driver.find_element(By.ID, "id_Perimeter_mean").click()
    # 18 | type | id=id_Perimeter_mean | 87.46
    self.driver.find_element(By.ID, "id_Perimeter_mean").send_keys("87.46")
    # 19 | click | id=id_Area_mean | 
    self.driver.find_element(By.ID, "id_Area_mean").click()
    # 20 | type | id=id_Area_mean | 1326
    self.driver.find_element(By.ID, "id_Area_mean").send_keys("1326")
    # 21 | click | id=id_Smoothness_mean | 
    self.driver.find_element(By.ID, "id_Smoothness_mean").click()
    # 22 | type | id=id_Smoothness_mean | 0.08474
    self.driver.find_element(By.ID, "id_Smoothness_mean").send_keys("0.08474")
    # 23 | click | id=id_Compactness_mean | 
    self.driver.find_element(By.ID, "id_Compactness_mean").click()
    # 24 | type | id=id_Compactness_mean | 0.07864
    self.driver.find_element(By.ID, "id_Compactness_mean").send_keys("0.07864")
    # 25 | click | id=id_Concavity_mean | 
    self.driver.find_element(By.ID, "id_Concavity_mean").click()
    # 26 | type | id=id_Concavity_mean | 0.0869
    self.driver.find_element(By.ID, "id_Concavity_mean").send_keys("0.0869")
    # 27 | click | id=id_Concave_points_mean | 
    self.driver.find_element(By.ID, "id_Concave_points_mean").click()
    # 28 | type | id=id_Concave_points_mean | 1.471
    self.driver.find_element(By.ID, "id_Concave_points_mean").send_keys("1.471")
    # 29 | click | id=id_Symmetry_mean | 
    self.driver.find_element(By.ID, "id_Symmetry_mean").click()
    # 30 | type | id=id_Symmetry_mean | 0.1812
    self.driver.find_element(By.ID, "id_Symmetry_mean").send_keys("0.1812")
    # 31 | click | id=id_Fractal_dimension_mean | 
    self.driver.find_element(By.ID, "id_Fractal_dimension_mean").click()
    # 32 | type | id=id_Fractal_dimension_mean | 5.766
    self.driver.find_element(By.ID, "id_Fractal_dimension_mean").send_keys("5.766")
    # 33 | click | id=id_Radius_se | 
    self.driver.find_element(By.ID, "id_Radius_se").click()
    # 34 | type | id=id_Radius_se | 0.5435
    self.driver.find_element(By.ID, "id_Radius_se").send_keys("0.5435")
    # 35 | click | css=form | 
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    # 36 | click | id=id_Texture_se | 
    self.driver.find_element(By.ID, "id_Texture_se").click()
    # 37 | type | id=id_Texture_se | 7.886
    self.driver.find_element(By.ID, "id_Texture_se").send_keys("7.886")
    # 38 | click | id=id_Perimeter_se | 
    self.driver.find_element(By.ID, "id_Perimeter_se").click()
    # 39 | type | id=id_Perimeter_se | 3.398
    self.driver.find_element(By.ID, "id_Perimeter_se").send_keys("3.398")
    # 40 | click | id=id_Area_se | 
    self.driver.find_element(By.ID, "id_Area_se").click()
    # 41 | type | id=id_Area_se | 23.13
    self.driver.find_element(By.ID, "id_Area_se").send_keys("23.13")
    # 42 | click | id=id_Smoothness_se | 
    self.driver.find_element(By.ID, "id_Smoothness_se").click()
    # 43 | type | id=id_Smoothness_se | -0
    self.driver.find_element(By.ID, "id_Smoothness_se").send_keys("-0")
    # 44 | click | id=id_Compactness_se | 
    self.driver.find_element(By.ID, "id_Compactness_se").click()
    # 45 | type | id=id_Compactness_se | 0.01308
    self.driver.find_element(By.ID, "id_Compactness_se").send_keys("0.01308")
    # 46 | click | id=id_Concavity_se | 
    self.driver.find_element(By.ID, "id_Concavity_se").click()
    # 47 | type | id=id_Concavity_se | 0.0186
    self.driver.find_element(By.ID, "id_Concavity_se").send_keys("0.0186")
    # 48 | click | id=id_Concave_points_se | 
    self.driver.find_element(By.ID, "id_Concave_points_se").click()
    # 49 | type | id=id_Concave_points_se | 1.587
    self.driver.find_element(By.ID, "id_Concave_points_se").send_keys("1.587")
    # 50 | click | id=id_Symmetry_se | 
    self.driver.find_element(By.ID, "id_Symmetry_se").click()
    # 51 | type | id=id_Symmetry_se | 0.01389
    self.driver.find_element(By.ID, "id_Symmetry_se").send_keys("0.01389")
    # 52 | click | id=id_Fractal_dimension_se | 
    self.driver.find_element(By.ID, "id_Fractal_dimension_se").click()
    # 53 | type | id=id_Fractal_dimension_se | 6.193
    self.driver.find_element(By.ID, "id_Fractal_dimension_se").send_keys("6.193")
    # 54 | click | id=id_Radius_worst | 
    self.driver.find_element(By.ID, "id_Radius_worst").click()
    # 55 | type | id=id_Radius_worst | 14.11
    self.driver.find_element(By.ID, "id_Radius_worst").send_keys("14.11")
    # 56 | click | css=#div_id_Texture_worst > .requiredField | 
    self.driver.find_element(By.CSS_SELECTOR, "#div_id_Texture_worst > .requiredField").click()
    # 57 | click | id=id_Texture_worst | 
    self.driver.find_element(By.ID, "id_Texture_worst").click()
    # 58 | type | id=id_Texture_worst | 23.41
    self.driver.find_element(By.ID, "id_Texture_worst").send_keys("23.41")
    # 59 | click | id=id_Perimeter_worst | 
    self.driver.find_element(By.ID, "id_Perimeter_worst").click()
    # 60 | type | id=id_Perimeter_worst | 99.7
    self.driver.find_element(By.ID, "id_Perimeter_worst").send_keys("99.7")
    # 61 | click | id=id_Area_worst | 
    self.driver.find_element(By.ID, "id_Area_worst").click()
    # 62 | type | id=id_Area_worst | 1956
    self.driver.find_element(By.ID, "id_Area_worst").send_keys("1956")
    # 63 | click | id=id_Smoothness_worst | 
    self.driver.find_element(By.ID, "id_Smoothness_worst").click()
    # 64 | type | id=id_Smoothness_worst | 1.037
    self.driver.find_element(By.ID, "id_Smoothness_worst").send_keys("1.037")
    # 65 | click | id=id_Compactness_worst | 
    self.driver.find_element(By.ID, "id_Compactness_worst").click()
    # 66 | type | id=id_Compactness_worst | 0.1866
    self.driver.find_element(By.ID, "id_Compactness_worst").send_keys("0.1866")
    # 67 | click | id=id_Concavity_worst | 
    self.driver.find_element(By.ID, "id_Concavity_worst").click()
    # 68 | type | id=id_Concavity_worst | 0.2416
    self.driver.find_element(By.ID, "id_Concavity_worst").send_keys("0.2416")
    # 69 | click | id=id_Concave_points_worst | 
    self.driver.find_element(By.ID, "id_Concave_points_worst").click()
    # 70 | type | id=id_Concave_points_worst | 0.186
    self.driver.find_element(By.ID, "id_Concave_points_worst").send_keys("0.186")
    # 71 | click | id=id_Symmetry_worst | 
    self.driver.find_element(By.ID, "id_Symmetry_worst").click()
    # 72 | type | id=id_Symmetry_worst | 3.613
    self.driver.find_element(By.ID, "id_Symmetry_worst").send_keys("3.613")
    # 73 | click | id=id_Fractal_dimension_worst | 
    self.driver.find_element(By.ID, "id_Fractal_dimension_worst").click()
    # 74 | type | id=id_Fractal_dimension_worst | 8.368
    self.driver.find_element(By.ID, "id_Fractal_dimension_worst").send_keys("8.368")
    # 75 | click | css=.btn-info | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
    # 76 | click | css=.alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    # 77 | assertText | css=.alert | Data Berhasil di Prediksi
    time.sleep(5)
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "Data Berhasil di Prediksi"
  
