from fpdf import FPDF
import pandas as pd

# Pandas is a data analysis package, wich can parse CSV data into data frames, to use them in Python

# Import CSV to be displayed into PDF File
df = pd.read_csv('files/topics.csv')

# Initiate the PDF file
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Generate pages in the PDF file. This loop will give us access to each row in DF
for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)  # Tutaj height nie jest w mm, ale w points
    # x1 - starting point, y1 - wysokość od x1, x2 - ending point, y2 - wysokość od ending point
    pdf.line(10, 21, 200, 21)

    # Set the footer
    pdf.ln(265)  # Add a breakline which has 265 mm
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for n in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)  # Add a breakline which has 277 mm
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output('output.pdf')
