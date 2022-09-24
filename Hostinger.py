from argparse import Action
from gettext import find
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import os
import pandas as pd
from pathlib import Path
import requests
import shutil
import math
import csv
import re
import datetime
import sys

#creatying a function to get our profile
def get_profile_path(profile):
    FF_PROFILE_PATH = os.path.join(os.environ['APPDATA'],'Mozilla', 'Firefox', 'Profiles')

    try:
        profiles = os.listdir(FF_PROFILE_PATH)
    except WindowsError:
        print("Could not find profiles directory.")
        sys.exit(1)
    try:
        for folder in profiles:
            print(folder)
            if folder.endswith(profile):
                loc = folder
    except StopIteration:
        print("Firefox profile not found.")
        sys.exit(1)
    return os.path.join(FF_PROFILE_PATH, loc)


#hostinger url
url2=""
download_path_root = os.path.join(os.environ['USERPROFILE'],r'OneDrive\Reporting\E1')

#Folder name
file_path="ShopfiyExport"


#profiles which helps us to download the file 
mime_types = "text/csv,text/html"
profile = webdriver.FirefoxProfile(get_profile_path('njc5g4gd.ShopifyNew'))
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.path.join(download_path_root, file_path))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)

#importing options
options = Options()
#firefox  exe path
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#gecko paths
Gecko_path = r"C:\Users\junai\OneDrive\Reporting\E1\gecko\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=profile ,executable_path= Gecko_path, options=options)
#browser get the url
driver.get(url2)
#maximizing our current browsers
driver.maximize_window()
wait = WebDriverWait(driver, 10)
time.sleep(5)

#your email
Email = "Enter Email"
#your password
password = "Enter here "

#this line of code will get enter your email
driver.find_element(By.CSS_SELECTOR,"#rcmloginuser").send_keys(Email)
time.sleep(4)
#this line of code will get enter your password
driver.find_element(By.CSS_SELECTOR,"#rcmloginpwd").send_keys(password)
#clicking login button
driver.find_element(By.ID,"rcmloginsubmit").click()
#Setting mail duration
mail_duration = 10
time.sleep(mail_duration*60)
#This line of code will select the newest the mail from your mail box
new = driver.find_elements(By.CSS_SELECTOR,"#messagelist tbody tr")[0]
#double clicking your 1st mail
act = ActionChains(driver)
act.double_click(new)
act.perform()

time.sleep(5)
#clicking the msg 
driver.find_element(By.CSS_SELECTOR,"table.v1mail-section:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
time.sleep(5)
driver.quit()
