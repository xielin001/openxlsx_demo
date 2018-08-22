import pprint

import openpyxl
#新版本openpyxl已不再支持get_highest_row()、get_highest_column()方法，引入max_row,max_column属性替代。
wb = openpyxl.load_workbook('.\\data\\censuspopdata.xlsx')
sheet = wb.get_active_sheet()
# sheet = wb.get_sheet_by_name('Population by Census Tract')
print(sheet)
rownum = sheet.max_row+1
print("rownum:",rownum)
populationdict = {}
for i in range(2,rownum):
    print("循环",i)
    state = sheet['B'+str(i)].value
    county = sheet['C'+str(i)].value
    pop = sheet['D' + str(i)].value
    populationdict.setdefault(state,{})
    populationdict[state].setdefault(county,{'pop':0,'tracts':0})
    populationdict[state][county]['tracts'] +=1
    populationdict[state][county]['pop'] +=int(pop)
print(populationdict)
#将结果保存到文件
print("Writing into the file population.py.....")
with open('.\\data\\population.py','w') as f:
    f.write("alldata= "+ pprint.pformat(populationdict))
f.close()
print("Done.")
