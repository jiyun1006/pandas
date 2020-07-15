import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B", "B+"],
        'c++': ["B+", "C", "C+"], }

data2 = {'c0': [1, 2, 3],
         'c1': [4, 5, 6],
         'c2': [7, 8, 9],
         'c3': [10, 11, 12],
         'c4': [13, 14, 15]}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)

# 여러 데이터 프레임 한 엑셀 파일로 저장하기.
writer = pd.ExcelWriter("./df_excelwriter.xlsx")

df.to_excel(writer, sheet_name="sheet1")

df2.to_excel(writer, sheet_name="sheet2")

writer.save()

# df.to_csv("./df_sample.csv")
# df.to_json("./df_sample.json")
# df.to_excel("./df_sample.xlsx")
