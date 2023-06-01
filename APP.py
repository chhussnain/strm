import streamlit as st
import requests
import re

def main():
    st.title("My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://example.com")

    # Add a button to trigger scraping
    if st.button("Scrape Website"):
        # Make a GET request to the website
        response = requests.get(url)

        # Extract the button elements using regular expressions
        buttons = re.findall(r'<button[^>]*>(.*?)</button>', response.text, re.IGNORECASE)

        # Display the extracted buttons in Streamlit
        for button in buttons:
            st.write(button)

if __name__ == '__main__':
    main()
