import smtplib
from email.mime.text import MIMEText
from email.header import Header

# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '154822916@qq.com'
password = 'xckhtdvgytqzcaig'

# 收信方邮箱
to_addr = '154822916@qq.com'

# 发信服务器
smtp_server ='smtp.qq.com'
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header('大BOSS')
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(host='smtp.qq.com')
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()
