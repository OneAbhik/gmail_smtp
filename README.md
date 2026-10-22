# Gmail SMTP Email Sender

A simple Python project that sends emails using Gmail's SMTP server. It uses Gmail App Passwords and environment variables to keep credentials secure.

## Features

- Send emails through Gmail SMTP
- Use Gmail App Password authentication
- Store credentials securely in a `.env` file
- Use Python's built-in `smtplib` library
- Use TLS encryption for the SMTP connection

## Requirements

- Python 3.10 or newer
- A Gmail account
- 2-Step Verification enabled on the Gmail account
- A Gmail App Password

## Project Structure

```text
gmail_smtp/
├── .env.example
├── .gitignore
├── README.md
└── send_email.py
