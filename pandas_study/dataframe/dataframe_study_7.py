import pandas as pd
import io
str = 'name,john,mary'
data = str.split(',')
print(data)
str = ','.join(data)
print(str)
line = '\n'.join(data)
print(line)
df = pd.read_csv(io.StringIO(line))
print(df)
