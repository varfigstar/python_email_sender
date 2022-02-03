from django.contrib import admin
from django.contrib.admin import register

from .models import EmailRecipient, EmailContent, EmailRecipientsGroup


@register(EmailRecipient)
class EmailRecipientAdminModel(admin.ModelAdmin):
    list_display = ('to_email',)


@register(EmailRecipientsGroup)
class EmailRecipientsGroupAdminModel(admin.ModelAdmin):
    list_display = ('group_name',)


@register(EmailContent)
class EmailContentAdmin(admin.ModelAdmin):
    list_display = ('mail_subject',)