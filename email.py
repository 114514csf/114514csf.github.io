from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 你的邮箱配置（以QQ邮箱为例）
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
EMAIL_USER = "your_email@qq.com"
EMAIL_PASS = "your_email_password_or_auth_code"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单内容
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # 组装邮件内容
        mail_content = f"姓名: {name}\n邮箱: {email}\n内容:\n{message}"
        msg = MIMEText(mail_content, "plain", "utf-8")
        msg["Subject"] = "表单信息"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER

        # 发送邮件
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
            return "邮件发送成功！"
        except Exception as e:
            return f"邮件发送失败: {e}"

    # 简单的HTML表单
    form_html = '''
    <form method="post">
      姓名: <input type="text" name="name"><br>
      邮箱: <input type="email" name="email"><br>
      内容: <textarea name="message"></textarea><br>
      <input type="submit" value="提交">
    </form>
    '''
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True)
