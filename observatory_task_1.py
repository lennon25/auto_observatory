# -*-coding:utf-8-*-
from appium import webdriver
import unittest
import time

class ObservatoryAutoTest(unittest.TestCase):

    def setUp(self):

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '12',
            'deviceName': 'afd67e94',
            'appPackage': 'hko.MyObservatory_v1_0',
            'appActivity': 'hko.homepage.Homepage2Activity',
            "noReset": True,
            "autoGrantPermissions": True,

        }
        # home activity: 
        # Agreement activity: hko.MyObservatory_v1_0.AgreementPage

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_9day_forecast(self):
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("Navigate up").click()
        self.driver.moveTo(173,1280)
        self.driver.find_element_by_name("9-Day Forecast").click()
        self.assertIsNotNone(self.driver.find_element_by_name("Weather Forecast"))

    def tearDown(self):
        self.driver.quit()


if __name__== '__main__':
    unittest.main()