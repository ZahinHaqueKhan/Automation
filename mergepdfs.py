#!/usr/bin/python3
import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_directory, output_path):
    pdf_writer = PdfWriter()
    
    for root, _, files in os.walk(input_directory):
        for file in sorted(files):
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                pdf_reader = PdfReader(pdf_path)
                
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
    
    with open(output_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)
    
    print(f"Successfully merged PDFs into {output_path}")

def main():
    input_directory = input("Enter the directory: ")  # Replace with your directory path
    output_path = input_directory + "/merged.pdf"  # Replace with your desired output file path
    
    merge_pdfs(input_directory, output_path)

if __name__ == "__main__":
    main()
