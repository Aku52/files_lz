import docx
f = open('lion.docx','r')    
doc = docx.Document(f)
for paragraph in doc.paragraphs:
    for run in paragraph.runs:



'''import csv
from docx import Document
from docx.shared import RGBColor
from openpyxl import load_workbook
from openpyxl.styles import Font
import json
import pandas as pd
'''
