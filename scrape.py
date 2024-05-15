import requests
from bs4 import BeautifulSoup

def get_all_contents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            contents = []
            for element in soup.find_all(string=True):
                contents.append(element.get_text())
            return contents
        else:
            # print("Failed to retrieve the page:", response.status_code)
            return response.status_code
    except Exception as e:
        # print("Please provide the correct URL")
        return None

def get_all_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            hrefs = []
            for link in links:
                hrefs.append(link['href'])
            return hrefs
        else:
            # print("Failed to retrieve the page:", response.status_code)
            return response.status_code
    except Exception as e:
        return None

# URL of the webpage you want to scrape
url = input("Enter the URL of the webpage you want to scrape: ")

all_contents = get_all_contents(url)

all_links = get_all_links(url)

if all_contents is None or all_links is None:
    print("Please provide the correct URL")
elif isinstance(all_contents, int) or isinstance(all_links, int):
    print("Failed to retrieve the page:", all_contents)
else:
    with open('contents.txt', 'w', encoding='utf-8') as f:
        counter = 1
        for content in all_contents:
            if content.strip():
                f.write(f"{counter} {content}\n")
                counter += 1

    with open('links.txt', 'w') as f:
        counter = 1
        for link in all_links:
            if link:
                f.write(f"{counter} {link}\n")
                counter += 1

