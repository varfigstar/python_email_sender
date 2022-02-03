from django.urls import path

from . import views


urlpatterns = [
    path(
        'start_mailing/<int:email_content_id>/',
        views.send_email_to_all_recipients, name="start_mailing_list"
    ),
    path(
        'start_mailing/<int:email_content_id>/<int:group_id>/',
        views.send_email_to_group,
        name="start_group_mailing_list"
    )
]