import os, sys, time, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pprint

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--headless')

DRIVER_PATH = 'chromedriverのパス' # ローカル

google_url = 'https://google.com/'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.implicitly_wait(1) # 秒
i = 0

with open('./out.txt', mode='w') as a:
    while True:
        f = open('./input.txt', 'r')
        datalist = f.readlines()
        serach_word = datalist[i] + ' 電話番号'
        driver.get(google_url)
        serach_form = driver.find_element_by_name('q')
        serach_form.send_keys(serach_word,Keys.ENTER)
        # serach_form.submit()
        try:
            phone_number = driver.find_element_by_class_name('mw31Ze').text
        except Exception:
            # phone_number = None
            phone_number = 'None'
        a.write(phone_number+'\n')
        print(phone_number)
        i += 1
        continue

f.close()
driver.close()