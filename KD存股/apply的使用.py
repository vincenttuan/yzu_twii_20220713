import pandas as pd

K = 0
def add(n):
    global K
    K = K + n + 3
    return K

df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df)
df['z'] = df['y'].apply(add)
print(df)
