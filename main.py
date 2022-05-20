from openpyxl import load_workbook
import json
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

  for row in sheet.iter_rows(min_row=2, values_only=True):
    try:
      if row[1] == 'Excluido':
        shutil.move(invoices_path+'FE'+str(row[0])+'.pdf', data['Excluido'])
      elif row[1] == 'Exentas':
        shutil.move(invoices_path+'FE'+str(row[0])+'.pdf', data['Exentas'])
      elif row[1] == 'Reintegros':
        shutil.move(invoices_path+'FE'+str(row[0])+'.pdf', data['Reintegros'])
    except:
      print('Error')



move_invoices('./book/detalle.xlsx', None, './paths.json', 'C:/Users/auxiliar.tics/Desktop/Facturas/')

