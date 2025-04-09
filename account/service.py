import threading

from django.core.mail import EmailMultiAlternatives
import random

from django.utils import timezone

from account.models import Code


def send_email_alternative(to, user):
    reset_link = 'http://127.0.0.1:8000/accounts/restore_password/'
    to = [f'{to}']
    subject = "Forgot Password"
    from_email = 'djamolovramazon90@gmail.com'
    code = random.randint(1000, 9999)
    time = timezone.now()
    obj = Code.objects.create(code=code, user=user)

    htm_c = f"""
    
    <h1>Salom, {user.email}!</h1>
        <h2> code {code} </h2>
        <p>Sizning hisobingiz uchun parolni tiklash so‘rovi qabul qilindi.</p>
        <p>Agar bu so‘rovni siz bajargan bo‘lsangiz, davom etish uchun quyidagi tugmani bosing.</p>
        <a href="{reset_link}" style="display: inline-block; padding: 10px 20px; margin-top: 10px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">Parolni Tiklash</a>
        <p>Agar bu so‘rov sizga tegishli bo‘lmasa, hech qanday harakat qilishingiz shart emas.</p>
        
        <h1>{time}<h1>

    """
    email = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
    email.attach_alternative(htm_c, "text/html")
    email.send()


def send_email_async(to, user):
    thread1 = threading.Thread(target=send_email_alternative, args=(to, user))
    thread1.start()
