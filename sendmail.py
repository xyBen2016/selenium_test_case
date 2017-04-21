import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import os
import datetime


# 定义发送邮件
def sent_mail(file_new):
    # 发信邮箱
    mail_from = 'xingyi_90@126.com'
    # 收信邮箱
    mail_to = 'xingyi_90@126.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['Subject'] = u"自动化测试报告"
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.126.com')
    # 用户名密码
    smtp.login('xingyi_90@126.com', 'xingyi251')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')


# 查找测试报告，调用发邮件功能
def send_report():
    result_dir = 'E:\\xy\\test\\pycharm\\pycharmWorkspace\\selenium_testcase\\report'

    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
    os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    # 调用发邮件模块
    sent_mail(file_new)

if __name__ == "__main__":
    # 执行发邮件
    send_report()
