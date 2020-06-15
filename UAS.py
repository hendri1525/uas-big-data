import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# input array menggunakan numpy
x = np.array([393, 410, 464, 474, 478, 478, 488, 537, 562, 590, 594, 636, 652])
y = np.array([393, 410, 464, 474, 478, 478, 488, 537, 562, 590, 594, 636, 652])


# convert ke panda dataframe
data = {'x': x, 'y': y}
df = pd.DataFrame(data)

# plot menggunakan barplot
sns.barplot(x='x', y='y', data=df)

plt.ylabel('Total_Kasus ')
plt.xlabel('Di Wilayah Nusa Tenggara Barat (393 = 20 May) > (652 = 1 Juni)')
plt.title('Total Kasus Covid-19 20 May sampai 1 Juni Tahun 2020')
plt.show()
