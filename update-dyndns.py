from requests import get
import os
from dotenv import load_dotenv

load_dotenv()

current_wan_ip = get("https://v4.ident.me/")
ip_adress = current_wan_ip.text

user = os.getenv("user")
key = os.getenv("key")
hostname = os.getenv("hostname")

res = get(f"https://{user}:{key}@members.dyndns.org/v3/update?hostname={hostname}&myip={ip_adress}")
