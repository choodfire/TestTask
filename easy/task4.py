import requests  # pip install requests


def get_my_public_ip_address():
    response = requests.get("https://ifconfig.me/")

    return response.text.strip()


if __name__ == "__main__":
    get_my_public_ip_address()
