# This is a simple web scraping script using BeautifulSoup

#Importing the required libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Hardcoded URL, you can change it to any URL you want to scrape
url = "https://www.reddit.com/r/cybersecurity/"

#Opening the URL using urlopen. Returns a file-like object
#The read() method reads the entire content of the file-like object and returns it as a byte string
# To convert the byte string to a regular string, we can decode it using UTF-8 encoding.
html = urlopen(url).read().decode('utf-8')

# To parse the HTML content, we can use BeautifulSoup.
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())  # This will format the HTML content for better readability

images = soup.find_all('img')  # Find all image tags. List of Tag objects
for image in images:
    print(image)  # Print the image tag
    print(image['src'])  # Print the value of the 'src' attribute
    print(image.get('alt'))  # Get the value of the 'alt' attribute
    print(image.get('title'))  # Get the value of the 'title' attribute
    print()