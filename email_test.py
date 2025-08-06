import smtplib
from email.message import EmailMessage

# Replace with your email and app password (generate from Google Account security settings)
email_id = "barunk622@gmail.com"
app_pass = "osnc gugi arhl ihrn"
  # App password

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_id
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_id, app_pass)
            smtp.send_message(msg)
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Send account creation acknowledgment
def send_openacn_ack(uemail, uname, uacn, upass):
    sub = "Congrats 😊, Account Opened Successfully"
    body = f"""Hello {uname},

Welcome to ABC Bank!

Your Account Number is: {uacn}
Your Password is: {upass}

⚠️ Kindly change your password when you login for the first time.

Thanks,
ABC Bank
Noida"""
    send_email(sub, body, uemail)

# Send OTP for fund transfer
def send_otp(uemail, otp, amt):
    sub = "OTP for Fund Transfer"
    body = f"""Your OTP is {otp} to transfer amount ₹{amt}.

⚠️ Please do not share this OTP with anyone.

Thanks,
ABC Bank
Noida"""
    send_email(sub, body, uemail)

# Send OTP for password recovery
def send_otp_4_pass(uemail, otp):
    sub = "OTP for Password Recovery"
    body = f"""Your OTP to recover your password is: {otp}

⚠️ Do not share this with anyone.

Thanks,
ABC Bank
Noida"""
    send_email(sub, body, uemail)

