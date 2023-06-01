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

        # Extract the class attributes using regular expressions
        classes = re.findall(r'class=["\']([^"\']*)', response.text)

        # Display the extracted classes in Streamlit
        for class_name in classes:
            st.write(class_name)

if __name__ == '__main__':
    main()
