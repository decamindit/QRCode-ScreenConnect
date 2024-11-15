import subprocess
import sys
import os
import secrets
import string


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def random_pass(length=10):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password


def generate_login(issuer,user_name):
    random_string = pyotp.random_base32()
    img = qrcode.make(f'otpauth://totp/{user_name}?secret={random_string}&issuer={issuer}')
    img.save(f'qrcode.png')
    print(f'QRCode generated \n Username: {user_name} \n Password: {random_pass(12)}\n Secret: goog:{random_string}')
    print('\nScan the QRCode to setup the OTP')


if __name__ == "__main__":

    try:
        import qrcode
        import pyotp
    except ImportError:
        install('pyotp')
        install('qrcode')
        install('qrcode[pil]')

    import qrcode
    import pyotp

    issuer = input("Enter Issuer: ")
    user_name = input("Enter Username: ")
    generate_login(issuer,user_name)
    os._exit(0)