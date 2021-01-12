import requests

print(requests.__version__)
r = requests.get(http://www.google.com)
print(r.text)

raw = requests.get("https://raw.githubusercontent.com/Felix-Huang11/CMPUT404_lab1/main/script.py")
print(raw.text)
