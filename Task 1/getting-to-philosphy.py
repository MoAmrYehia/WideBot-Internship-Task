import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    content_div = soup.find(
        id="mw-content-text").find(class_="mw-parser-output")

    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):

        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin(
        'https://en.wikipedia.org/', article_link)

    return first_link


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("Target ('Philosphy') article reached!")
        return False
    elif len(search_history) > max_steps:
        print("Maximum (25) searches reached, search aborted.")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Arrived at an article already seen, search aborted.")
        return False
    else:
        return True


article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("Arrived at an article with no links, search aborted.")
        break

    article_chain.append(first_link)

    time.sleep(0.5)  # Slow things down so as to not overload Wikipedia's servers
