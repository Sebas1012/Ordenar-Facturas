from openpyxl import load_workbook
import json
import os
import shutil

def move_invoices(book_path, sheet_name, json_path, invoices_path):
  # Excel file load
  book = load_workbook(str(book_path))
  
  if sheet_name == None:
    sheet = book.active
  else:
    sheet = book[str(sheet_name)]

  # JSON path file load
  with open(json_path) as data:
    data = json.load(data)

  # List Files
  files = os.listdir(invoices_path)

  for row in sheet.iter_rows(min_row=2, values_only=True):
    print(row)



move_invoices('./book/test.xlsx', None, './paths.json', './invoices')

