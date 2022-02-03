from django.http import HttpResponse

from .services.recipients import (
    get_all_recipients_from_bd,
    check_is_object_exists,
    get_recipients_from_group
)
from .services.mailing_list import start_mailing_list
from .models import EmailContent


def send_email_to_all_recipients(request, email_content_id: int):
    recipients = get_all_recipients_from_bd()

    # can't pass a query object as argument in celery task,
    # so we need to check
    # is EmailContent object exists before schedule task
    check_is_object_exists(EmailContent, email_content_id)

    start_mailing_list.delay(
        recipients=recipients, email_content_id=email_content_id
    )

    return HttpResponse("Start mailing list")


def send_email_to_group(request, email_content_id: int, group_id: int):
    check_is_object_exists(EmailContent, email_content_id)
    recipients = get_recipients_from_group(group_id)

    start_mailing_list.delay(
        recipients=recipients,
        email_content_id=email_content_id
    )

    return HttpResponse("Start group {} mailing list".format(group_id))