import streamlit as st
import requests
import re

def main():
    st.title(" My Web Scraper")

    # Make a GET request to the website
    url = "https://quotes.toscrape.com/"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)

    # Extract the links using regular expressions
    links = re.findall(r'<a\s+href=[\'"]?([^\'" >]+)', response.text)

    # Display the extracted links in Streamlit
    for link in links:
        st.write(link)

if __name__ == '__main__':
    main()
