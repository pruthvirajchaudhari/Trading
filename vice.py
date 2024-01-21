import requests
from bs4 import BeautifulSoup

def search_google(query):
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('h3', {'class': 't'})
        
        for i, result in enumerate(results, start=1):
            title = result.text
            print(f'{i}. {title}')
    else:
        print(f'Error: Unable to fetch results. Status Code: {response.status_code}')

# Example usage
query = 'web scraping with Python'
search_google(query)
