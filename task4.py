# pip install requests
import requests

def get_my_public_ip_address():
    response = requests.get("https://ifconfig.me/")

    return response.text.strip()
