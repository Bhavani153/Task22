import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
print(driver.find_element(By.XPATH,'//span[@ title="173,266"]').text)
time.sleep(2)
print(driver.find_element(By.XPATH,'//span[@ class="_ac2a"]').text)
time.sleep(2)