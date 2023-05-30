


import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title("Web Scraper Demo")

    # Make a GET request to the website
    url = "http://books.toscrape.com/"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the desired data from the HTML
    # Here, we're extracting all the links from the page
    links = soup.find_all("a")

    # Display the extracted links in Streamlit
    for link in links:
        st.write(link["href"])

if __name__ == '__main__':
    main()