from django.shortcuts import get_object_or_404

from ..models import EmailRecipient, EmailRecipientsGroup


def check_is_object_exists(object_cls, object_id: int):
    return get_object_or_404(object_cls, pk=object_id)


def get_all_recipients_from_bd():
    return [r.to_email for r in EmailRecipient.objects.all()]


def get_recipients_from_group(group_id: int):
    group = get_object_or_404(EmailRecipientsGroup, pk=group_id)
    recipients = [r.to_email for r in group.recipients.all()]

    return recipients


