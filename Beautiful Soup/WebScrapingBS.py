# This is a simple web scraping script using BeautifulSoup

#Importing the required libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#Hardcoded URL, you can change it to any URL you want to scrape
url = "https://www.reddit.com/r/cybersecurity/"


#Opening the URL using urlopen. Returns a file-like object
#The read() method reads the entire content of the file-like object and returns it as a byte string
# To convert the byte string to a regular string, we can decode it using UTF-8 encoding.
html = urlopen(url).read().decode('utf-8')

# To parse the HTML content, we can use BeautifulSoup.
soup = BeautifulSoup(html, 'html.parser')

if(os.path.exists('reddit.html')):
    os.remove('reddit.html')  # Remove the file if it exists
# Create a new HTML file to save the scraped content
with open('reddit.html', 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))  # Write the HTML content to a file

# Find all the links in the HTML content
links = []
for link in soup.find_all('a', attrs={'href': True}):
    links.append(link.get('href'))  # Append the link to the list
if(os.path.exists('reddit_links.html')):
    os.remove('reddit_links.html')  # Remove the file if it exists
with open('reddit_links.html', 'w', encoding='utf-8') as file:
    for item in links:
        file.write(item+"\n")  # Write the links to a file