import time 
import requests
from bs4 import BeautifulSoup as bs

url = f"https://ismlar.com/category/Boshqalar"

def connect_to_site(url,index):
    res = requests.get(url+f"?page={index}")
    if res.status_code == 200:
        return res
    else:
        return False
    

def write_data(data):
    with open("names.txt", "a", encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}, ")


def parser(index):
    obj_parse =  connect_to_site(url,index)
    print(obj_parse)
    if obj_parse:
        page = bs(obj_parse.text, "html.parser")
        h1 = page.findAll("h1" , class_="font-bold text-2xl text-cyan-500")
        names = [x.text.strip() for x in h1]
        print(names)
        write_data(names)
    else:
        time.sleep(1)
        print("Error")
    return True

for i in range(1,190):
    done = parser(index=i)
    print(done)
    if done:
        print(i)