import smtplib
from email.mime.text import MIMEText

# 设置邮件服务器 服务器host和端口

conn = smtplib.SMTP_SSL('mail.weimob.com', 465)

# 登录邮箱
conn.login(user='weijie.shi@weimob.com', password='SSwwjj9!7')

sender = 'weijie.shi@weimob.com'

receiver = 'weijie.shi@weimob.com'

message = MIMEText('内容内容内容内容内容内容内容内容', 'plain', 'utf-8')

message['Subject'] = '这是测试发送邮件'

message['from'] = sender

message['to'] = receiver

# 发送邮件
try:
    conn.sendmail(sender, receiver, message.as_string())
    print("发送成功")
except Exception as e:
    print("发送邮件失败")