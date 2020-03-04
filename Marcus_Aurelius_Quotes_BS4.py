from bs4 import BeautifulSoup
import requests
import csv

# Scrape all Marcus Aurelius Quotes from this page
url = 'https://wisdomquotes.com/marcus-aurelius-quotes/'

# Tell website that is user not robot trying to access it.
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(url, headers=headers)
htmlData = response.content


soup = BeautifulSoup(htmlData, 'lxml')

#  Make CSV file = Marcus_Aurelius_Quotes.csv
csv_file = open('Marcus_Aurelius_Quotes.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Quote'])

# Loop all blockquote and print paragraphs text
quotes = soup.findAll('blockquote')
for x in quotes:
    paragraph = x.find('p').text
    print(paragraph)
    print()

    #  Author Name = "Marcus Aurelius"
    csv_writer.writerow(["Marcus Aurelius", paragraph])

csv_file.close()
