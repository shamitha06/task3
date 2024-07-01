import requests
from bs4 import BeautifulSoup

# URL of th web page to scrape
url = 'https://realpython.com/python-web-scraping-practical-introduction/' # Replace with the url of the web page you want to scrape

# send a GET request to the web page
reponse = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
   # parse the HTML content fo the page
   soup = Beautifulsoup(response.text, 'html.parser')

   # Extract all the text from the page
   page_text = soup.get_text()

   # Extract all the links from the page
   links = [a['href'] for a in soup.find_all('a', href=True)]

   # Extract all the images from the page
   images = [img['src'] for img in soup.find_all('img', src=True)]

   # print the extracted data
   print("page Text:")
   print(page_text)

   print("\nLinks:")
   for links in links:
      print(link)

      print("\nImages:")
   for image in images:
      print(image)
else:
   print(f"Failed to retrieve the web page. status code: {response.status_code}")       