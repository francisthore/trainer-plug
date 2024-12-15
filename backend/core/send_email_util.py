#!/usr/bin/env python3
from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from config import settings

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = settings.MAIL_API_KEY

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "from the Python SDK!"
sender = {"name":"Trainer Plug","email":"no-reply@linfordscarwash.co.za"}
replyTo = {"name":"Trainer Plug","email":"info@mambatechsol.com"}
html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
to = [{"email":"thorefrancis@gmail.com","name":"Francis Thre"}]
params = {"parameter":"My param value","subject":"New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=replyTo, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
