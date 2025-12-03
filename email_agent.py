# email_agent.py
import os
from typing import Dict
from dataclasses import dataclass

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To


def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body."""

    sg = sendgrid.SendGridAPIClient(
        api_key=os.environ.get("SENDGRID_API_KEY")
    )

    # === Your email info (sender & receiver) ===
    from_email = Email("maimohamedsaber737@gmail.com")   # verified sender
    to_email = To("maimohamedsaber737@gmail.com")        # send to yourself

    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()

    response = sg.client.mail.send.post(request_body=mail)
    print("Email response:", response.status_code)

    return {"status": "sent", "code": response.status_code}
    

@dataclass
class Agent:
    name: str
    instructions: str
    model: str
    tools: list = None
    output_type: object | None = None


INSTRUCTIONS = """
You send well-formatted HTML emails.

Given a detailed report, you will:
1) Create a clear subject line.
2) Convert the report into clean HTML.
3) Use the 'send_email' tool to send the email once.
"""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
