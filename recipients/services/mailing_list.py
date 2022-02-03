from celery import shared_task
from django.shortcuts import get_object_or_404
from django.core.mail import send_mass_mail
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings
from email_sender import celery_app

from ..models import EmailContent


@celery_app.task(bind=True)
def start_mailing_list(*args, recipients: list, email_content_id: int):
    email_content = get_object_or_404(EmailContent, pk=email_content_id)

    messages = [
        (
            email_content.mail_subject,
            email_content.mail_text,
            email_content.from_email,
            [r]
        )
        for r in recipients
    ]

    return send_mass_mail(
        messages
    )
