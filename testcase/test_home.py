import unittest
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from testcase.public import login


class HomeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        login.login(self)
        self.driver.get("http://www.secomid.com/secomid-e/page/index.php")
        # 最多等待10秒
        wait = ui.WebDriverWait(self.driver, 10)
        # 等待，直至页面显示用户名输入框
        wait.until(lambda dr: self.driver.find_element_by_xpath("/html/body/div[3]/div[2]").is_displayed())

    def tearDown(self):
        self.driver.quit()

    def testHome(self):
        """判断公司信息是否正确"""
        div = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]")
        if div.text.find("粤ICP备16084902号") == -1:
            print("fail:testHome 粤ICP备16084902号")
        else:
            print("success:testHome 粤ICP备16084902号")

    def testCurrentUrl(self):
        """判断url是否正确"""
        if self.driver.current_url != "http://www.secomid.com/secomid-e/page/index.php":
            print("fail:testHome currenturl")
        else:
            print("success:testHome currenturl")

if __name__ == "__main__":
    unittest.main()
