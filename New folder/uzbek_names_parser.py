import requests
import sqlite3
import time
from bs4 import BeautifulSoup

con = sqlite3.connect("names.db", check_same_thread=False)
cur = con.cursor()

# cur.execute("""CREATE TABLE names(
#     id INTEGER PRIMARY KEY AUTOINCREMENT ,
#     name TEXT,
#     descripition TEXT);""")


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}


for i in range(1,29):
    url = f"https://ismlar.com/category/O%E2%80%98zbekcha?gender=1&page={i}"
    page = requests.get(url=url, headers=HEADERS)
    # print(page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")

    all_names = soup.find_all("li",class_="p-4 rounded-2xl space-y-4 bg-cyan-100")
    for name in all_names:
        try:
            sql = f"""
            INSERT INTO names(name,descripition)
            VALUES('{name.h1.text.strip()}','{name.div.p.text.strip()}')
            """
        except sqlite3.DatabaseError as err:
            print(err)
        else:
            con.commit()
    else:
        time.sleep(1)
        print("OK")
