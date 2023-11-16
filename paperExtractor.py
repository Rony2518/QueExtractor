import PyPDF2
import re
import os
from fpdf import FPDF

def extract_questions_from_pdf(pdf_files):
    # Initialize an empty set to store the questions
    questions = set()

    for pdf_file in pdf_files:
        # Open the PDF file
        with open(pdf_file, "rb") as file:
            # Create a PDF file reader object
            reader = PyPDF2.PdfReader(file)

            # Loop through each page in the PDF
            for page_num in range(len(reader.pages)):
                # Extract the text from the page
                text = reader.pages[page_num].extract_text()

                # Use a regular expression to find questions in the text
                # This assumes that all questions start with "Q." and end with a number
                # indicating the marks for the question
                found_questions = re.findall(
                    r"Q\.\d\s\(\w\).*?(?=\nQ\.\d|\nOR|\Z)", text, re.DOTALL
                )

                # Add the found questions to the set of questions
                questions.update(found_questions)
    # Write the unique questions to a text file
    with open("questionsOfADA.txt", "w", encoding='utf-8') as file:
        for question in questions:
            file.write(question + "\n")

# List of PDF files to extract questions from
pdf_files = [
    "\path\paper1.pdf",
    "\path\paper2.pdf",
    "\path\paper3.pdf",
    "\path\paper4.pdf",
]

# Extract questions from the PDF files
extract_questions_from_pdf(pdf_files)
