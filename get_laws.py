import requests
from bs4 import BeautifulSoup


CODUL_PENAL_LINK = "https://legislatie.just.ro/Public/DetaliiDocument/109855"


def main():
    page = requests.get(CODUL_PENAL_LINK)

    # Save content to file
    with open('CODUL_PENAL.html', 'wb+') as f:
        f.write(page.content)
    
    with open('CODUL_PENAL.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(content, 'lxml')
    
    # Extract all S_ART tags
    articles = soup.find_all('span', attrs={'class': 'S_ART'})

    # Dictionary to store extracted texts
    article_texts = {}
    law_texts = [article.text for article in articles]
    law_dict = {article.contents[1].text: article.contents[3].text for article in articles}


if __name__ == '__main__':
    main()