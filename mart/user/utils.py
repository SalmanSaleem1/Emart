from flask_mail import Message
from mart import mail
from flask import render_template, flash
from mart.constant.appConstant import Constant


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset message', sender='noreply@gmail.com', recipients=[user.email])
    msg.html = render_template('include/SentEmail.html', token=token, _external=True)
    flash(f'{Constant.RESET_PASSWORD_EMAIL_SEND}', f'{Constant.INFO_FLASH_MESSAGE}')
    mail.send(msg)

    return "Send"
