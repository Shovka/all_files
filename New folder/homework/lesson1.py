from bs4 import BeautifulSoup
with open("./index.html") as file:
    src = file.read()
print(src)
soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find() , .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)
# page_h1 = soup.find_all("h1")
# print(page_h1)

# for item in page_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("h5").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)


# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[1].text)

# find_a = soup.find(class_="links").find("ul").find_all("a")
# find_a = soup.find_all(class_="finda")

# for i in find_a:
#     texts = i.text
#     links = i.get("href")
#     print(f'{texts}: {links}')

# post_div = soup.find(class_="links").find_parent()
# print(post_div)