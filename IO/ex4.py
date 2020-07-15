import pandas as pd

url = '/home/jiyoon/다운로드/part/part2/sample.html'


tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print("tables{%s}" % i)
    print(tables[i])
    print('\n')

df = tables[1]

df.set_index(['name'], inplace=True)
print(df)