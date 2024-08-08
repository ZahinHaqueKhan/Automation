#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pdfkit

def get_all_links(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = {link['href'] for link in links if link['href'].startswith(base_url)}
        return urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {base_url}: {e}")
        return set()

def convert_url_to_pdf(url, output_path):
    try:
        pdfkit.from_url(url, output_path)
        print(f"Successfully saved {url} to {output_path}")
    except Exception as e:
        print(f"Failed to convert {url} to PDF: {e}")

def main():
    base_url = 'https://versebyversequranstudycircle.wordpress.com/'  # Replace with your target website
    output_dir = '/home/yamato/Downloads/VerseByVerseQuran'  # Replace with your output directory

    urls = get_all_links(base_url)

    for i, url in enumerate(urls):
        output_path = f"{output_dir}/page_{i+1}.pdf"
        convert_url_to_pdf(url, output_path)

if __name__ == "__main__":
    main()
