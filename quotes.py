# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
URL = "http://quotes.toscrape.com"
response = requests.get(URL)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quotes on the page
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

# Step 4: Open a file to save the quotes
with open("quotes.txt", "w") as file:
    for quote, author in zip(quotes, authors):
        file.write(f"{quote.text} - {author.text}\n")

print("Quotes have been saved to quotes.txt")
