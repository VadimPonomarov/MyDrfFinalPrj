import json
import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse

from core.services.email_extras.email_data_classes import SendEmailArgs
from core.services.jwt_services import ActivateToken, JWTService
from core.my_dataclasses import UserDataClass
from configs.celery import app

from concurrent.futures import ThreadPoolExecutor


class EmailService:

    @classmethod
    @app.task
    def send_email(cls, args: SendEmailArgs):
        msg = EmailMultiAlternatives(
            from_email=args.from_email,
            to=args.to,
            subject=args.subject
        )
        msg.attach_alternative(
            content=args.generated_content,
            mimetype='text/html'
        )
        msg.send()

    @classmethod
    def send_register_email(cls, user: UserDataClass):
        token = JWTService.create_token(user=user, token_class=ActivateToken)
        url = os.getenv('BASE_URL').strip() + reverse(viewname='users_activate', kwargs={"token": token})

        args = SendEmailArgs(
            subject='Register',
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[os.getenv('EMAIL_HOST_USER'), user.email],
            context={'url': url},
            template=get_template('email_register.html'),

        )

        with ThreadPoolExecutor() as executor:
            executor.submit(cls.send_email, args)

        spam.delay('My text')


@app.task
def spam(text='Spam !!!'):
    print(text)
