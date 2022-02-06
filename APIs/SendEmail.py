import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from HtmlCode import html_code


def send_email_to_patient(final_result_dict):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Report of Autism Screening Test"
    msg['From'] = "Audect Team"
    msg['To']  = final_result_dict['email']
    html = html_code.format(final_result_dict['prediction_percentage'][0:6], final_result_dict['name'], final_result_dict['age'], final_result_dict['sex'], final_result_dict['who_completed_the_test'], final_result_dict['email'], final_result_dict['ethinicity'])

    # Record the MIME types of both parts - text/plain and text/html.
    mim_text = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(mim_text)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.login('projectworks41@gmail.com','vatsa1441')
    try:
        s=smtp_server.send_message(msg)
        smtp_server.quit()
        print(s)
        return "Email Sent"

    except:
        print(2)
        return "Email Sending Failed"

