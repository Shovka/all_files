import requests
from bs4 import BeautifulSoup
import json

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"


# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
# }
# req = requests.get(url, headers=headers)

# src = req.text

# # print(src)

# with open("index.html", "w") as file:
#     src = file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

catarago = {}
hrefs_all = soup.find_all(class_="mzr-tc-group-item-href")
for i in hrefs_all:
    text = i.text
    href = "https://health-diet.ru" + i.get("href")

catarago[text] = href
with open("catarago.json", "w") as file:
    json.dump(catarago, file, indent=4, ensure_ascii=False)