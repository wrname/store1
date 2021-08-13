from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一个HKR的测试报告",
    description="这是一个详细登陆的测试报告",
    verbosity=1,
    stream = open(file="登陆测试报告.html", mode="w+", encoding="utf-8")
)


runner.run(tests)


# 邮件发送代码
# 报告发送
# 截图当成附件发送过去

sender = '1209812066@qq.com'  # 发件人邮箱账号
my_pass = 'wpqkwbchhlocghhe'  # 发件人邮箱授权码
user = '1950722212@qq.com'  # 收件人邮箱账号

msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["",sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

# 发送附件
att = MIMEText(open('登陆测试报告.txt','rb').read(), 'base64', 'utf-8')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=test.html"  # filename为文件名字
msg.attach(att)


try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")












