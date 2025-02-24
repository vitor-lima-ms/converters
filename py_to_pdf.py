from fpdf import FPDF # type: ignore
from pathlib import Path
import os

#Funcao para converter (https://www.geeksforgeeks.org/convert-python-file-to-pdf/)
def convert_to_pdf_fpdf(input_file, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(family='Arial', size=12)

    with open(input_file, 'r') as python_file:
        content = python_file.read()
        pdf.multi_cell(0, 10, content)

    pdf.output(output_pdf)

BASE_DIR = Path(__file__).parent
SUB_DIR = BASE_DIR / 'recipes_app/tests'

for file in os.listdir(SUB_DIR):
    if '.py' in file:
        convert_to_pdf_fpdf(SUB_DIR / file, f'{SUB_DIR}/{file.replace('.py', '')}.pdf')