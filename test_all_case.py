import unittest
import HTMLTestRunner
import time
import sendmail

list_case = "E:/xy/test/pycharm/pycharmWorkspace/selenium_testcase/testcase"


def create_suite_list():
    test_unit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(list_case, pattern='test_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
            print(test_unit)
    return test_unit

if __name__ == "__main__":
    all_test_names = create_suite_list()
    now = time.strftime(' %Y-%m-%d-%H_%M_%S ', time.localtime(time.time()))
    filename = 'E:/xy/test/pycharm/pycharmWorkspace/selenium_testcase/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'官网自动化测试报告', description=u'用例执行情况：')
    # 执行测试用例
    runner.run(all_test_names)
    # 发送邮件
    sendmail.send_report()
