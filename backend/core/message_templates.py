"""Module that contains email message templates"""


def email_verification_msg(verification_link: str) -> str:
    """
    Defines an email template for the email verification

    Args:
        verification_link (str): the verification link

    Returns:
        str: message content
    """

    message = f"""
    Hi there, please complete your email verification by clicking on the link below:
    <br/>
    {verification_link}
    """
    return message
