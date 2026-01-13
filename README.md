# Web Scraper - Quotes

A simple Python web scraper that extracts quotes and their authors from [quotes.toscrape.com](http://quotes.toscrape.com).

## Features

- Scrapes quotes and author names from a popular quotes website
- Saves extracted data to a text file (`quotes.txt`)
- Uses `BeautifulSoup` for HTML parsing

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/danishsyed-dev/web-scraper-quotes.git
   cd web-scraper-quotes
   ```

2. Install dependencies:
   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

Run the script:
```sh
python quotes.py
```

The scraped quotes will be saved to `quotes.txt` in the same directory.

## Output Example

```
"The world as we have created it is a process of our thinking..." - Albert Einstein
"It is our choices, Harry, that show what we truly are..." - J.K. Rowling
...
```

## License

This project is open source and available under the [MIT License](LICENSE).
