import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailClient:
    """Класс для работы с почтой по протоколам SMTP и IMAP."""

    def __init__(self, login, password, smtp_host, imap_host):
        self.login = login
        self.password = password
        self.smtp_host = smtp_host
        self.imap_host = imap_host

    def send_message(self, subject, recipients, message):
        """Отправляет письмо заданным получателям."""
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_host, 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.login, self.password)
            server.sendmail(self.login, recipients, msg.as_string())

    def receive_last_message(self, header=None):
        """Возвращает последнее письмо из входящих.

        Если задан header, ищет письмо с соответствующим заголовком.
        """
        with imaplib.IMAP4_SSL(self.imap_host) as mail:
            mail.login(self.login, self.password)
            mail.select('inbox')
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            _, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
        return email.message_from_bytes(raw_email)


if __name__ == '__main__':
    client = EmailClient(
        login='login@gmail.com',
        password='qwerty',
        smtp_host='smtp.gmail.com',
        imap_host='imap.gmail.com',
    )
    client.send_message(
        subject='Subject',
        recipients=['vasya@email.com', 'petya@email.com'],
        message='Message',
    )
    last_message = client.receive_last_message()
