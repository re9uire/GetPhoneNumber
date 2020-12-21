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

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--headless')

DRIVER_PATH = 'chromedriverのパス' # ローカル

google_url = 'https://google.com/'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

while True:
    shopName = input("店舗名:")
    serach_word = shopName + ' 電話番号'
    driver.get(google_url)
    serach_form = driver.find_element_by_name('q')
    serach_form.send_keys(serach_word)
    serach_form.submit()
    try:
        phone_number = driver.find_element_by_class_name('mw31Ze').text
    except Exception:
        # phone_number = None
        phone_number = 'None'
    if shopName == 'exit':
        print("プログラムを終了します")
        break
    print("電話番号:"+phone_number)
    continue