import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from testcase.public import login


class AboutTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        login.login(self)
        self.driver.get("http://www.secomid.com/secomid-e/page/compintro.php")
        # 最多等待10秒
        wait = ui.WebDriverWait(self.driver, 10)
        # 等待，直至页面显示用户名输入框
        wait.until(
            lambda dr: self.driver.find_element_by_xpath("/html/body/div[3]/div[2]").is_displayed())

    def tearDown(self):
        self.driver.quit()

    def testAbout(self):
        """判断是否about页"""
        div = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]")
        if div.text.find("ABOUT") == -1:
            print("fail:testAbout ABOUT")
        else:
            print("success:testAbout ABOUT")

    def testCurrentUrl(self):
        """判断url是否正确"""
        if self.driver.current_url != "http://www.secomid.com/secomid-e/page/compintro.php":
            print("fail:testAbout currenturl")
        else:
            print("success:testAbout currenturl")

    def testCulture(self):
        """判断CULTURE是否出现"""
        span = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/span[2]")
        if span.text.find("CULTURE") == -1:
            print("fail:testAbout CULTURE")
        else:
            print("success:testAbout CULTURE")

if __name__ == "__main__":
    unittest.main()
