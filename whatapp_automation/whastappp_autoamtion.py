
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import *

import time
from whatsapp_ui import *


  
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_1Ra05"]')
    

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")

# PLEASE scan qr code   for LOGGING IN.
print("Scan QR code ")
print("Logged in")
time.sleep(10)


def msg():
	user_name_list =[""]#enter user_name...
	msg = [""]
	count=int(input("enetr the message count:))

	for user_name in user_name_list:

        try:
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)
            print("0")
        finally:
            print("some error is there")
       
        search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_box.send_keys(user_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(8)

	for i in range(count):
		msg_box.send_keys(msg)
		msg_box.send_keys(Keys.ENTER)

msg()


def reps():
	print("Do you want o send anymore messages")
	askUser=input(press y for yes or n for no)
	if(askUser=='Y' or askUser=='y'):
		msg()
		reps()
	elif (askUser=='N' or askUser=='n'):
		print("Thank you! see you soon :\n")
	else:
		print("please enter a valid option :\n ")	
		reps()

reps()
        

driver.quit
