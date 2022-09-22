import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import pandas as pd

#read data
data1 = pd.read_excel('iSharesS&P500.xlsx', sheet_name='Sheet1', usecols='B')

#make qqplot
qqplot(np.array(data1), line='s')
plt.show()
