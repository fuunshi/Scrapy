## Overview
This is a Python script that crawls staff pages on various government websites and extracts email addresses. The script uses the Scrapy library to crawl and scrape data from the following websites:
- https://sidingbamun.gov.np/staff
- https://mikwakholamun.gov.np/staff
- https://meringdenmun.gov.np/staff
- and more if you configure it well

The extracted email addresses are written to a text file named after the website's domain in a folder named `Data`. 

## Prerequisites
- Python 3.x
- Scrapy library

## Installation
1. Clone this repository to your local machine.
2. Navigate to the repository directory using the terminal or command prompt.
3. Install Scrapy if you haven't already:
   ```bash
   pip install scrapy
   ```

## Usage
1. Open a terminal or command prompt and navigate to the cloned repository directory.
2. Run the Python script:
   ```bash
   scrapy crawl govsite
   ```

This will start the crawling process. The script will visit each of the URLs specified in the `start_urls` list and extract email addresses from the staff pages. The extracted email addresses will be saved in the `Data` folder in text files named after the website's domain.

## File Structure
- `README.md`: This file.
- `govsite`: The main Python script that crawls the government websites and extracts email addresses.
- `scrapy.cfg`: A Scrapy configuration file.
- `Data/`: A folder containing the text files with extracted email addresses.

## Notes
- The script assumes that the email addresses are present in `<td>` tags on the staff pages. If the structure of the staff pages changes, the script may need to be updated.
- The script may take some time to run, depending on the number of URLs and the size of the staff pages.
- The script saves the extracted email addresses as plain text files. You can modify the script to save the data in a different format if needed.
- Make sure to respect the terms of use of the websites you're scraping.

