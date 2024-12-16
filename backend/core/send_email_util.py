#!/usr/bin/env python3
from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from .config import settings
from fastapi import HTTPException
from utils.logging_helper import logger
from utils.common_helpers import validate_email

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = settings.MAIL_API_KEY


def send_email_message(
        receiver: str,
        subject: str,
        message: str
        ):
    """
    Sends an email using Brevo's transactional email API

        Args:
        receiver (str): The recipient's email address
        subject (str): The email subject
        message (str): The message body of the email

        Returns:
            dict: Response from Brevo API on success
            None: on failure

        Raises:
            HTTPException: on failure
    """
    if not validate_email(receiver):
        logger.error("Invalid email format: %s", receiver)
        raise HTTPException(
            status_code=400, detail="Invalid email address provided"
            )
    if not subject or not message:
        logger.error("Subject or message empty")
        raise HTTPException(
            status_code=400, detail="Subject and message cant be empty"
            )

    sender = {
        "name": f"{settings.FROM_NAME}", "email": f"{settings.FROM_MAIL}"
        }
    html_content = f"""
        <html>
            <body>
                <h3>Hi there, from the Trainer Plug Team </h3>
                <p> {message} </p>
            </body>
        </html>
    """
    to = [{"email": f"{receiver}"}]
    subject = subject
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, html_content=html_content, sender=sender, subject=subject
        )

    try:
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
            )
        api_response = api_instance.send_transac_email(send_smtp_email)
        logger.info("email sent successfully to %s", receiver)
        return api_instance
    except ApiException as e:
        logger.error("Error while sending email: %s", e)
        raise HTTPException(status_code=500, detail="Failed to send email")
