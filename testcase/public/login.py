from selenium import webdriver
import selenium.webdriver.support.ui as ui


def login(self):
    driver = self.driver
    driver.get("http://www.secomid.com/secomid-e/page/index.php")

    # 最多等待10秒
    wait = ui.WebDriverWait(driver, 10)
    # 等待，直至页面显示用户名输入框
    wait.until(
        lambda dr: driver.find_element_by_xpath("/html/body/div[3]/div[2]").is_displayed())
    print("login success")
