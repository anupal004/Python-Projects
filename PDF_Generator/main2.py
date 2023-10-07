from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, align="L", ln=1, txt=row["Topic"])

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(266)

    pdf.set_font(family="Times", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, align="R", ln=1, txt=row["Topic"])

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

        pdf.ln(278)

        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, align="R", ln=1, txt=row["Topic"])

pdf.output("Notes_Lined.pdf")