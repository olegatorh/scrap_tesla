import requests
from bs4 import BeautifulSoup


def data_from_lxml_using_bs4():
    url = "https://www.tesmanian.com/blogs/tesmanian-blog"
    data = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    title_and_link = soup.select('h2 a')
    print(f"bs\n: {title_and_link}")
    for i in title_and_link:
        data.append(f"https://www.tesmanian.com{i.attrs['href']}")
    return data


