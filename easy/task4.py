import requests  # pip install requests


def get_my_public_ip_address() -> str:
    response = requests.get("https://ifconfig.me/")

    return response.text.strip()


if __name__ == "__main__":
    get_my_public_ip_address()
