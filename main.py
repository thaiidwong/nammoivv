import base64
import hashlib
import socket
import random
import os
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

# Danh sách các màu đậm
COLORS = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.GREEN,
    Style.BRIGHT + Fore.YELLOW,
    Style.BRIGHT + Fore.BLUE,
    Style.BRIGHT + Fore.MAGENTA,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.WHITE,
]

def get_random_color():
    """Trả về một màu ngẫu nhiên (đậm)."""
    return random.choice(COLORS)

def create_key_from_ip(ip_address):
    """
    Tạo key từ địa chỉ IP bằng cách băm SHA-256 và mã hóa Base64.
    """
    try:
        sha256_hash = hashlib.sha256(ip_address.encode()).digest()
        base64_key = base64.b64encode(sha256_hash).decode()
        return base64_key
    except Exception as e:
        return f"Error: {e}"

def validate_key(input_key, expected_key):
    """
    Xác thực key người dùng nhập với key đã mã hóa.
    """
    return input_key == expected_key

def main():
    # Lấy địa chỉ IP hiện tại
    ip_address = socket.gethostbyname(socket.gethostname())

    # Tạo key từ IP mạng
    generated_key = create_key_from_ip(ip_address)

    # Hiển thị thông tin với màu sắc ngẫu nhiên (đậm)
    print(get_random_color() + f"Ip Của Bạn Là: {ip_address}")
    print(get_random_color() + "Zalo: 0943040079")
    print(get_random_color() + "Liên hệ chủ code để lấy key")
    print(get_random_color() + "Key sử dụng vv chắc thế")
    print(get_random_color() + "Key thay đổi theo IP mạng và đã được mã hóa")
    print(get_random_color() + "Nếu không thấy IP thì lên web tìm")

    key_file = "key_free_by_dwongthai.txt"

    # Kiểm tra sự tồn tại của file lưu key
    if os.path.exists(key_file):
        with open(key_file, "r") as file:
            saved_key = file.read().strip()
        if validate_key(saved_key, generated_key):
            print(get_random_color() + "Key hợp lệ!")
            return
        else:
            print(get_random_color() + "Key Sai")

    # Yêu cầu người dùng nhập key nếu không có hoặc không hợp lệ
    while True:
        inp = input(get_random_color() + "Nhập Key: ").strip()
        if validate_key(inp, generated_key):
            print(get_random_color() + "Key Đúng Rùi")
            with open(key_file, "w") as file:
                file.write(inp)
            break
        else:
            print(get_random_color() + "key Sai")

if __name__ == "__main__":
    main()
#Phần Code Tiếp Theo Ở Đây

from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
from time import sleep,strftime
from datetime import datetime
import re,requests,os,sys
import socket
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")

import os, sys, requests
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;32m╔═══════════════════════════════════════════════════════════════════════════════════════╗
\033[1;32m║   \033[1;31mChúc bạn năm 2025 đầy may mắn\033[1;33m, an khang thịnh vượng!                                ║
\033[1;32m║═══════════════════════════════════════════════════════════════════════════════════════║
\033[1;32m║   \033[1;31mBạn đã sẵn sàng nói lời tạm biệt \033[1;33mvới năm 2024 chưa??                                ║
\033[1;32m║═══════════════════════════════════════════════════════════════════════════════════════║
\033[1;32m║   \033[1;31mHãy sẵn sàng \033[1;33mchào đón năm 2025!                                                     ║
\033[1;32m╚═══════════════════════════════════════════════════════════════════════════════════════╝
\033[1;31m nếu không vào được code
\033[1;33m ib để hỗ trợ   
  \033[1;34m  
  \033[1;34m        2025   2025   2025  
  \033[1;33m     2025 2025 2025 2025 2025 
  \033[1;32m  2025  2025   2025    2025  2025
  \033[1;35m2025                           2025
  \033[1;35m2025      happy new year       2025    
  \033[1;34m2025                           2025    
  \033[1;33m2025                           2025   
  \033[1;32m  2025                        2025
  \033[1;35m    2025                    2025 
  \033[1;36m      2025                2025   
  \033[1;34m        2025            2025     
  \033[1;33m          2025        2025     
  \033[1;32m            2025    2025
  \033[1;35m              20252025
  \033[1;36m                2025
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.001)
while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP 2025 để đi tiếp hoặc nhập thoat để thoát\033[1;37m =>: \033[1;33m'
)
    if chon == "thoat":
       break
    if chon == "2025":
        exec(requests.get('https://raw.githubusercontent.com/kococc/nammoivv/refs/heads/main/nammoivv.py').text)
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")
   
