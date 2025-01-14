from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Step 2: Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail's SMTP server
app.config['MAIL_PORT'] = 587  # Port for Gmail's SMTP server
app.config['MAIL_USE_TLS'] = True  # Use TLS (Transport Layer Security)
app.config['MAIL_USERNAME'] = 'evans.kabiru@student.moringaschool.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'ezxg scdc kcww yaps'  # Your email password (use an app password if using Gmail)

mail = Mail(app)

# Define a route to send email
@app.route('/')
def send_email():
    try:
        msg = Message(
            subject='Hello from the other side!',
            sender=app.config['MAIL_USERNAME'],  # Explicit sender
            recipients=['egatangi537@gmail.com']  # Recipient email
        )
        msg.body = "Hey Evans, sending you this email from my Flask app. Let me know if it works!"
        mail.send(msg)
        return "Message sent successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run("127.0.0.1", 5006, debug=True)