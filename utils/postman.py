# -*- coding:utf-8 -*-
"""
 @FileName  :postman.py
 @Time      :2022/9/7 10:49
 @Author: liuguanghong
 @software: PyCharm
 @pythonVersion: 3.9.0
"""
import smtplib
from email.mime.text import MIMEText


def send_email(mail_host, mail_user, mail_pass, receivers, title, content):
    # 第三方 SMTP 服务
    sender = mail_user  # 发件人邮箱
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False


if __name__ == '__main__':
    email_config = {
        "mail_host": "smtp.163.com",
        "mail_user": "lgh_981203@163.com",
        "mail_pass": "OUPFEFUQSEXBITGF",
        "receivers": ["992247234@qq.com"],
        "title": "测试",
        "content": "测试发送内容"
    }
    # send_email(mail_host="smtp.163.com", mail_user="lgh_981203@163.com", mail_pass="OUPFEFUQSEXBITGF",
    #            receivers=["992247234@qq.com"], title="测试", content="测试发送内容")
    res = send_email(**email_config)
    if res:
        print("发送成功")
