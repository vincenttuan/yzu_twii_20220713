import pandas as pd
import io
str = 'name,age,sex\njohn,18,M\nmary,19,F'
df = pd.read_csv(io.StringIO(str))
print(df)


