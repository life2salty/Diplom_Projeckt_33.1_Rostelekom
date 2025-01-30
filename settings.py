import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')

valid_password_email = os.getenv('valid_password_email')
valid_password_phone = os.getenv('valid_password_phone')

invalid_phone = os.getenv('invalid_phone')
invalid_email = os.getenv('invalid_email')
invalid_login = os.getenv('invalid_login')

invalid_password = os.getenv('invalid_password')
