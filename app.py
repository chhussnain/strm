import streamlit as st
import requests
import re

def main():
    st.title("Movie Title Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://example.com/movies")

    # Make a GET request to the website
    response = requests.get(url)

    # Extract the movie titles using regular expressions
    movie_titles = re.findall(r'<h2>(.*?)</h2>', response.text)

    # Display the extracted movie titles in Streamlit
    for title in movie_titles:
        st.write(title)

if __name__ == '__main__':
    main()
