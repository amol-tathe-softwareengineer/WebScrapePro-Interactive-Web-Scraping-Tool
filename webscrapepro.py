import requests
from bs4 import BeautifulSoup

url = input("Enter Website URL: ")

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        print("\nPage Title:")
        print(soup.title.string)

        print("\nFirst 5 Headings:")
        headings = soup.find_all("h1")

        for heading in headings[:5]:
            print("-", heading.text.strip())

    else:
        print("Failed to retrieve website data.")

except Exception as error:
    print("An error occurred:", error)
