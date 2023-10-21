import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract specific elements or data from the page
    # For example, let's extract all the links (anchor tags) on the page
    links = soup.find_all('a')

    # Print the links
    for link in links:
        print(link.get('href'))

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

