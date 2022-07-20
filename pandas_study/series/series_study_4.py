import pandas as pd
import matplotlib.pyplot as plt

date = pd.date_range('20220701', periods=4)
s = pd.Series([4, 7, -5, 3], index=date)
plt.plot(s.index, s.values, '-')
plt.title('my series chart')
plt.xlabel('date')
plt.ylabel('price')
plt.grid(True)
plt.show()
