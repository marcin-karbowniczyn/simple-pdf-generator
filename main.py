from fpdf import FPDF
import pandas as pd

# Pandas is a data analysis package, wich can parse CSV data into data frames, to use them in Python

# Import CSV to be displayed into PDF File
df = pd.read_csv('files/topics.csv')

# Initiate the PDF file
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Generate pages in the PDF file. This loop will give us access to each row in DF
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    # x1 - starting point, y1 - wysokość od x1, x2 - ending point, y2 - wysokość od ending point
    pdf.line(10, 21, 200, 21)

    num_of_pages = int(row['Pages'])
    if num_of_pages > 1:
        for n in range(num_of_pages - 1):
            pdf.add_page()

pdf.output('output.pdf')
