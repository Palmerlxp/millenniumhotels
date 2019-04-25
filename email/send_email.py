import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr

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
    part = MIMEApplication(open('../report/Test Report.html', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="Test Report.html")  # 发送文件名称
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()

try:
    subject = 'Python 测试邮件'
    content = '这是一封来自 Python 编写的测试邮件。'
    send_email('smtp.qq.com', '1477602712@qq.com', 'qruxtvirmvguggbc', '605049232@qq.com', subject, content)
except Exception as err:
    print(err)

