import smtplib
import email.mime.multipart
import email.mime.text
import time
from email.mime.application import MIMEApplication
from email.utils import formataddr
import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport

def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    '''
    :param smtpHost: 域名
    :param sendAddr: 发送邮箱
    :param password: 邮箱密码
    :param recipientAddrs: 发送地址
    :param subject: 标题
    :param content: 内容
    :return: 无
    '''
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = formataddr(["tester yan",sendAddr]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['to'] = formataddr(["Yan Liu",recipientAddrs]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件地址
    part = MIMEApplication(open('./report/Test Report.html', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="Test Report.html")  # 发送文件名称
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(".",pattern="test*.py",top_level_dir=None)     # ."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(discover).report(filename="Test Report", description='Regression test', log_path='./report')    # log_path='.'把report放到当前目录下
    nowtime = time.strftime("%Y%m%d %H:%M:%S")

    try:
        subject = 'automation test report'
        content = f'{nowtime} This is the report file of MHR automation test'

        send_email('smtp.126.com', 'liuyan061@126.com', 'liuyan061', 'Palmer.Lu@mullenloweprofero.com', subject, content)
    except Exception as err:
        print(err)
