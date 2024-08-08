#!/usr/bin/python3
import os
from PyPDF2 import PdfReader
from ebooklib import epub

def pdf_to_text(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text() + "\n"
    return text

def create_epub(text, output_path, title="Title", author="Author"):
    book = epub.EpubBook()

    book.set_identifier('id123456')
    book.set_title(title)
    book.set_language('en')
    book.add_author(author)

    # Create a chapter
    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml', lang='en')
    chapter.content = '<h1>Chapter 1</h1><p>' + text.replace('\n', '<br/>') + '</p>'

    # Add chapter
    book.add_item(chapter)

    # Define Table Of Contents
    book.toc = (epub.Link('chap_01.xhtml', 'Chapter 1', 'chap_01'),)

    # Add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Basic spine
    book.spine = ['nav', chapter]

    # Write to the file
    epub.write_epub(output_path, book, {})

    print(f"Successfully created EPUB: {output_path}")

def main():
    pdf_path = input('Path to the pdf file: ')  # Replace with your PDF file path
    output_path = input("Name of the output file (without extension): ") + ".epub" # Replace with your desired EPUB file path

    text = pdf_to_text(pdf_path)
    create_epub(text, output_path, title="Sample Title", author="Sample Author")

if __name__ == "__main__":
    main()
