
import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import os,time
# Declare browser
# s = Service('/Users/FTECH/OneDrive/Desktop/chromedriver.exe')
# # import chromedriver
# driver = webdriver.Chrome(service=s)

# # Open URL
# driver.get("https://www.lazada.vn/dien-thoai-di-dong/?page=1&spm=a2o4n.home.cate_1.1.1905e182tGDwoM")
# sleep(random.randint(5,10))

# # ================================ GET link/title
# elems = driver.find_elements(By.CSS_SELECTOR , ".RfADt [href]")
# title = [elem.text for elem in elems]
# links = [elem.get_attribute('href') for elem in elems]

# df = pd.DataFrame(links)
# print(df)

if __name__ == "__main__":
    url_file_driver = os.path.join('etc','chromedriver.exe')
    driver = webdriver.Chrome(executable_path=url_file_driver)
    driver.get('https://covid19.gov.vn/')
    target = driver.find_elements_by_xpath('')
    driver.switch_to.frame(1)
    time.sleep(4)  # dung web 4s
    driver.close()