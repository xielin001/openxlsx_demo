import openpyxl
import openxlsx.data
wb = openpyxl.load_workbook('.\\data\\example.xlsx')
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
result = openxlsx.data.population['WY']
print(result)