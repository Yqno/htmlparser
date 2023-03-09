import requests 
from bs4 import BeautifulSoup


url = input("your URL:") # Your URL Here 
response = requests.get(url)

if response.status_code == 200:

    doc = BeautifulSoup(response.text, "html.parser")    
    
    # Extract Images
    images = doc.find_all("img")
    for img in images:
        print("Image URL:", img.attrs["src"])

    # Extract Headers
    headers = doc.find_all("h1")
    for header in headers:
        print("Header:", header.text)

    # Extract Paragraphs
    paragraphs = doc.find_all("p")
    for paragraph in paragraphs:
        print("Paragraph:", paragraph.text)
        
    # Extract Links
    links = doc.find_all("a")
    for link in links:
        print("Link:", link.attrs["href"])
