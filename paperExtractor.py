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
                # found_questions = re.findall(
                #     r"Q\.\d\s\(\w\).*?(?=\nQ\.\d|\nOR|\Z)", text, re.DOTALL
                # )
                # Use a regular expression to find the questions.
                for match in re.finditer(r"Q\.\d\s\(\w\).*?(?=\nQ\.\d|\nOR|\Z)", text, re.DOTALL):
                    # Add the question to the set.
                    questions.add(match.group(1))

                # Add the found questions to the set of questions
                questions.update(found_questions)

    # Write the unique questions to a text file
    # with open("questionsOfADA.txt", "w", encoding='utf-8') as file:
    #     for question in questions:
    #         file.write(question + "\n")
    # Create a new PDF for the questions.
    pdf = FPDF()

    # Add a page.
    pdf.add_page()

    # Set the font.
    pdf.set_font("Arial", size = 12)

    # Loop through the questions.
    for question in questions:
        # Write the question to the PDF.
        pdf.cell(200, 10, txt = question, ln = True)

    # Save the PDF.
    pdf.output("questions.pdf")

# List of PDF files to extract questions from
pdf_files = [
    "D:\python\paperExtractor\ADA-BE-SUMMER-2022.pdf",
    "D:\python\paperExtractor\ADA-BE-WINTER-2020.pdf",
    "D:\python\paperExtractor\ADA-BE-WINTER-2021.pdf",
    "D:\python\paperExtractor\ADA-BE-WINTER-2022.pdf",
]

# Extract questions from the PDF files
extract_questions_from_pdf(pdf_files)
