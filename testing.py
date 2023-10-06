import pandas as pd
from mlu import test

a = [1,2,3,4,5]
b = [6, 7, 8, 9, 10]
df = pd.DataFrame([a, b])

print(test(df))