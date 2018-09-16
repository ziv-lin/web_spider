import requests
import webbrowser

data = {"username": "jlinbe", "password": "Dji730470317"}

raw_net = "https://access.ust.hk/cas/login?service=https%3A%2F%2Fcanvas.ust.hk%2Flogin%2Fcas"

r = requests.post("https://access.ust.hk/cas/login?service=https%3A%2F%2Fcanvas.ust.hk%2Flogin%2Fcas", data=data)


r = requests.post("https://access.ust.hk/cas/login?service=https%3A%2F%2Fcanvas.ust.hk%2Flogin%2Fcas", data=data)
# print(r.text)
print(r.cookies.get_dict())
# r = requests.get("https://canvas.ust.hk/courses/20765/files", cookies=r.cookies)
# print(r.text)

