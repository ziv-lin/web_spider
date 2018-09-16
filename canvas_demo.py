from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from http import cookiejar

def save_html(name, response):
    file_temp = open(name+".html", "w")
    file_temp.write(str(response.content.decode('utf-8')))
    file_temp.close()

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies_1.txt')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)
except:
    print("还没有cookie信息")

canvas_url = "https://canvas.ust.hk/login/cas"
login_url = "https://access.ust.hk/cas/login?service=https%3A%2F%2Fcanvas.ust.hk%2Flogin%2Fcas"
canvas_main_url="https://canvas.ust.hk/?login_success=1"
# header = {
#     "Host": "www.canvas.ust.hk/login/cas",
#     "Referer": "https://canvas.ust.hk/login/cas",
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
# }

headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'}

response = session.get(canvas_url, headers = headers)
save_html("canvas_url_0", response);

soup = BeautifulSoup(response.content, "html.parser")
execution = soup.find('input', attrs={"name": "execution"}).get("value")
print("exec = ", execution)
data = {
        'username': "jlinbe",
        'password': "Dji730470317",
        'execution': execution,
        '_eventId': "submit",
        'geolocation': ""}
response_login = session.post(login_url, data=data, headers = headers)
save_html("login", response_login);
response = session.post(canvas_main_url, headers = headers)
save_html("canvas_dash_0", response);
for i in session.cookies:
        print(i)
session.cookies.save()