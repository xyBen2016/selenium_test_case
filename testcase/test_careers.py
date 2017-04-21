import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from testcase.public import login


class CareersTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        login.login(self)
        self.driver.maximize_window()
        self.driver.get("http://www.secomid.com/secomid-e/page/compintro.php")

        # 最多等待10秒
        wait = ui.WebDriverWait(self.driver, 10)
        # 等待，直至页面显示用户名输入框
        wait.until(
            lambda dr: self.driver.find_element_by_xpath("/html/body/div[3]/div[2]").is_displayed())
        self.driver = self.driver

    def tearDown(self):
        self.driver.quit()

    def testCareers(self):
        """判断是否Careers页"""
        # try:
        div = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        # except:
        # self.driver.get_screenshot_as_file(
        #     "E:/xy/test/pycharm/pycharmWorkspace/selenium_testcase/report/errorCareers.png")

        if div.text.find("Join Us！") == -1:
            print("fail:testCareers Join Us！")
        else:
            print("success:testCareers Join Us！")

    def testCurrentUrl(self):
        """判断url是否正确"""
        if self.driver.current_url != "http://www.secomid.com/secomid-e/page/talrecruit.php":
            print("fail:testCareers currenturl")
        else:
            print("success:testCareers currenturl")

    def testCurrentjob(self):
        """判断The current job是否出现"""
        # try:
        span = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/span")
        # except:
        # self.driver.get_screenshot_as_file(
        #     "E:/xy/test/pycharm/pycharmWorkspace/selenium_testcase/report/errorCurrentjob.png")

        if span.text.find("The current job") == -1:
            print("fail:testCareers The current job")
        else:
            print("success:testCareers The current job")


if __name__ == "__main__":
    unittest.main()
