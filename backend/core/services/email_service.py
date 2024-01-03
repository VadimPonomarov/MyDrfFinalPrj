import os
from concurrent.futures import ThreadPoolExecutor

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse

from configs.celery import app
from core.my_dataclasses import UserDataClass
from core.services.email_extras.email_data_classes import SendEmailArgs
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:

    @staticmethod
    @app.task
    def send_email(from_email: str = '', to: str = '', subject: str = '', generated_content: str = ''):
        msg = EmailMultiAlternatives(
            from_email=from_email,
            to=to,
            subject=subject
        )
        msg.attach_alternative(
            content=generated_content,
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
            to=[os.getenv('EMAIL_HOST_USER'), user.email if user else None],
            context={'url': url},
            template=get_template('email_register.html'),
        )

        if os.environ.get('DOCKER'):
            cls.send_email.delay(**args())
        else:
            executor = ThreadPoolExecutor()
            executor.submit(cls.send_email, **args())
            executor.shutdown(wait=False)

    @classmethod
    def recovery_email(cls, user: UserDataClass):
        token = JWTService.create_token(user=user, token_class=RecoveryToken)
        url = os.getenv('BASE_URL').strip() + reverse(viewname='users_activate', kwargs={"token": token})
        args = SendEmailArgs(
            subject='Register',
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[os.getenv('EMAIL_HOST_USER'), user.email if user else None],
            context={'url': url},
            template=get_template('email_recovery.html'),
        )

        if os.environ.get('DOCKER'):
            cls.send_email.delay(**args())
        else:
            executor = ThreadPoolExecutor()
            executor.submit(cls.send_email, **args())
            executor.shutdown(wait=False)
