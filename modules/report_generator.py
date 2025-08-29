from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd

def export_pdf(df: pd.DataFrame, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, "MLFF Tolling SAT Test Report")
    y = 750
    for _, row in df.iterrows():
        line = f"{row['ID']} - {row['Title']} : {row['Status']}"
        c.drawString(50, y, line)
        y -= 20
    c.save()

