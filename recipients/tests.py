from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .models import EmailContent, EmailRecipient, EmailRecipientsGroup


class MailingListTests(TestCase):
    def test_start_mailing_list(self):
        recipient = EmailRecipient.objects.create(
            to_email=settings.EMAIL_HOST_USER
        )
        recipient.save()
        email_content = EmailContent.objects.create(
            from_email=settings.EMAIL_HOST_USER,
            crontab="* * * 1 * 0",
            mail_text="Hello there!",
            mail_subject="Very important message"
        )
        email_content.save()

        response = self.client.get(
            reverse(
                'start_mailing_list',
                kwargs={"email_content_id": email_content.pk}
            )
        )
        wrong_not_found_response = self.client.get(
            reverse(
                'start_mailing_list',
                kwargs={"email_content_id": 1000}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(wrong_not_found_response.status_code, 404)


class GroupMailingListTests(TestCase):
    def test_start_group_mailing_list(self):
        recipient = EmailRecipient.objects.create(
            to_email=settings.EMAIL_HOST_USER
        )
        recipient.save()
        email_content = EmailContent.objects.create(
            from_email=settings.EMAIL_HOST_USER,
            crontab="* * * 1 * 0",
            mail_text="Hello there!",
            mail_subject="Very important message"
        )
        email_content.save()
        recipients_group = EmailRecipientsGroup.objects.create(
            group_name="Test Group"
        )
        recipients_group.recipients.add(recipient)
        recipients_group.save()

        response = self.client.get(
            reverse(
                'start_group_mailing_list',
                kwargs={
                    "email_content_id": email_content.pk,
                    "group_id": recipients_group.pk
                }
            )
        )
        wrong_not_found_response_1 = self.client.get(
            reverse(
                'start_group_mailing_list',
                kwargs={
                    "email_content_id": 1000,
                    "group_id": recipients_group.pk
                }
            )
        )

        wrong_not_found_response_2 = self.client.get(
            reverse(
                'start_group_mailing_list',
                kwargs={
                    "email_content_id": email_content.pk,
                    "group_id": 1000,
                }
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(wrong_not_found_response_1.status_code, 404)
        self.assertEqual(wrong_not_found_response_2.status_code, 404)
