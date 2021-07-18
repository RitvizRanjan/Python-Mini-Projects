import unittest
from selenium import webdriver

class TestGoogleMap(unittest.TestCase):
        def test_Bing(self ):
            self.driver = webdriver.Chrome()
            self.driver.get("https://www.boogle.com")
            print("Title of page is :" + self.driver.title)
            self.driver.close()

if __name__ == '__main__':
       unittest.main()
