
from docx import Document
from docx.shared import Pt, RGBColor
import tempfile
import pandas as pd
import os

def export_to_docx(text: str) -> str:
    doc = Document()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)

    for paragraph in text.split('. '):
        doc.add_paragraph(paragraph.strip())

    path = tempfile.mktemp(suffix='.docx')
    doc.save(path)
    return path

def export_to_csv(segments: list) -> str:
    df = pd.DataFrame(segments)
    path = tempfile.mktemp(suffix='.csv')
    df.to_csv(path, index=False)
    return path
