import threading
import random

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives


def send_email_single(to):
    code = random.randint(100000, 999999)
    send_mail(
        subject="Reset password",
        message=f"your reset password {code} ",
        from_email='djamolovramazon90@gmail.com',
        recipient_list=[f'{to}'],
        fail_silently=False,
    )


def send_otp_code_email(to):
    thread1 = threading.Thread(target=send_email_single, args=(to,))
    thread1.start()
