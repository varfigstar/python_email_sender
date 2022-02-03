from django.db import models


class EmailRecipient(models.Model):
    to_email = models.CharField(max_length=250)

    def __str__(self):
        return self.to_email


class EmailContent(models.Model):
    from_email = models.CharField(max_length=250)
    crontab = models.CharField(max_length=70)
    mail_text = models.TextField()
    mail_subject = models.CharField(max_length=250)


class EmailRecipientsGroup(models.Model):
    group_name = models.CharField(max_length=200)
    recipients = models.ManyToManyField(EmailRecipient)