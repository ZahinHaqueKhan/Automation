import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to_emails, attachment_path, sender_email, sender_password):
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, "plain"))

    # Open the file to be sent
    with open(attachment_path, "rb") as attachment:
        # Instance of MIMEBase and named as p
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode into base64
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    # Attach the instance 'part' to instance 'msg'
    message.attach(part)

    # Convert the message to string
    text = message.as_string()

    # Log in to server using secure context and send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            for email in to_emails:
                message["To"] = email
                server.sendmail(sender_email, email, text)
            print("Emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Email details
    sender_email = "zahinhaquekhan@gmail.com"
    sender_password = "wwrq optb vgym evlp"
    subject = "Immatriculation Certificate"
    body = """
    Dear sir, 

    Please find my immatriculation certificate attached. Please feel free to write to me incase of queries.
    
    I wish you a wonderful day.

    Yours faithfully,
    Zahin Haque Khan
    """
    attachment_path = "Immatrikulationsbescheinigung.pdf"
    
    # List of recipient emails
    to_emails = ["khanzahinhaque@gmail.com"]

    # Send the email
    send_email(subject, body, to_emails, attachment_path, sender_email, sender_password)
