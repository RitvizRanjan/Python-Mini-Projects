# whatsapp automation using selenium webdriver for multiple user (those who already exixt in your chat box recently)
# install selenium in your device by giving cmd ->"pip3 install selenium -U--(pip3 for python 3)
# please check your webdriver version in chrome by settings->help->about google chrome-->("version")
# downlaod the same version 0f web driver from "https://chromedriver.chromium.org/downloads"
from selenium import webdriver
# PLEASE download this module by giving command "pip install webdriver-manager"
# this modules manages your works like pressing enter and opening whatsapp.
from webdriver_manager.chrome import ChromeDriverManager
# this module will help you to use keys like ENTER ,RETURN ,e.t.c..
from selenium.webdriver.common.keys import Keys
# we are using try-except-finally so for except we need this ....
from selenium.common.exceptions import *
# we are importing time beacuse we need time to selct the and open the msg box
import time
from whatsapp_ui import *


# we are defining function so that we can call it whenever we need
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_1Ra05"]')
    
# we have to give the path of your web driver where you have stored in local server (laptop)
driver = webdriver.Chrome(ChromeDriverManager().install())
# to open whatsapp in chrome browser
driver.get("http://web.whatsapp.com")
# PLEASE scan qr code   for LOGGING IN.
print("Scan QR code ")
print("Logged in")
time.sleep(10)
# your chat box will open after 10 sec (whatever u had selected 'user_name')
# select your username_list(multiple user by making it list)
user_name_list =[""]#enter user_name...
# inspect your whatsapp serach bar to get your user_name <span> andpaste the xpath of search so it can search user_name .
msg = [""]
# for multiple use whom we didnt texted for long time or new user to seach in search bar
for user_name in user_name_list:
        try:
            # Select for the title having user name
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)
            print("0")
        finally:
            print("some error is there")
        # searches user_name
        search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        # no need to enter code will do the work.
        search_box.send_keys(user_name)
        # inspect an copy the xpath of message box of your user.
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        # open the message box of user.
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        # type the message and send it.
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(8)
        # your tab will get close after 8 seconds.

        driver.quit
