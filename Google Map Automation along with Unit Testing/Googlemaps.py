from selenium import webdriver
from time import sleep
import sys

driver = webdriver.Chrome()

driver.get("https://www.google.com/maps/@19.2467222,73.0051052,15z")
sleep(2)


def searchplace():
    place = driver.find_element_by_class_name("tactile-searchbox-input")
    place.send_keys(sys.argv[1])
    submit = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()


searchplace()


def directions():
    sleep(10)
    direction = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
    direction.click()


directions()


def find():
    sleep(6)
    dest = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    dest.send_keys(sys.argv[2])
    sleep(2)
    search = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()


find()


def kilometers():
    sleep(5)
    totalkilometers = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("Total Kilometers:", totalkilometers.text)
    sleep(5)
    bus = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
    print("Bus Travel:", bus.text)
    sleep(7)
    train = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[2]/div[1]/div")
    print("Train Travel:", train.text)
    sleep(7)


kilometers()
