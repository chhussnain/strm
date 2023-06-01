import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title("My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://example.com")

    # Add a button to trigger scraping
    if st.button("Scrape Website"):
        # Make a GET request to the website
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the input fields in the HTML
        input_fields = soup.find_all("input")

        # Display the extracted value attributes in Streamlit
        for input_field in input_fields:
            value = input_field.get("value")
            if value:
                st.write("value:", value)

if __name__ == '__main__':
    main()
