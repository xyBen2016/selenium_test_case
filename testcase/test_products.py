# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class ProductsTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.secomid.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_products_test_case(self):
        """判断是否products页"""
        driver = self.driver
        driver.get(self.base_url + "/secomid-e/page/productline.php")
        driver.find_element_by_css_selector("span.LTE > strong").click()
        driver.find_element_by_link_text("More").click()
        driver.find_element_by_css_selector("span.flatTitle.select > strong").click()
        driver.find_element_by_css_selector("span.smartTitle.select > strong").click()
        driver.find_element_by_css_selector("div.W68.second").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
