import pandas as pd
import numpy as np

student1 = pd.Series({'국어': np.nan, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})

print(student1, '\n')
print(student2, '\n')

add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2

print(type(div), '\n')

result = pd.DataFrame([add, sub, mul, div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result2 = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index=['덧셈', '뺼셈', '곱셈', '나눗셈'])
print(result2)


