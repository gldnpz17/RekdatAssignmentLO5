import pandas as pd
import seaborn as sns
import numpy as np
import re
import matplotlib.pyplot as plt

raw_data = pd.read_csv('menu.csv')
menu_data = raw_data[['Category', 'Serving Size', 'Calories']]

# Parse numerical data.
for index, row in menu_data.iterrows():
    weight = (re.search('\\((\\d+) g\\)', row['Serving Size']))
    if weight is None:
        menu_data.at[index, 'Serving Size'] = np.nan
    else:
        menu_data.at[index, 'Serving Size'] = float(weight.group(1))

menu_data.dropna(inplace=True)

print(menu_data)

# Calculate calorie density.
menu_data['Calorie Density'] = menu_data['Calories']/menu_data['Serving Size']

# Serving size boxplot.
axes = sns.boxplot(
    data=menu_data,
    x='Category',
    y='Serving Size',
).set(
    xlabel='Kategori',
    ylabel='Takaran sajian (gram)',
    title='Boxplot Takaran Sajian Makanan'
)
plt.show()

# Calorie boxplot.
axes = sns.boxplot(
    data=menu_data,
    x='Category',
    y='Calories',
).set(
    xlabel='Kategori',
    ylabel='Kalori (kalori)',
    title='Boxplot Kalori Makanan'
)
plt.show()

# Calorie density boxplot
axes = sns.boxplot(
    data=menu_data,
    x='Category',
    y='Calorie Density'
).set(
    xlabel='Kategori',
    ylabel='Densitas Kalori (kalori/gram)',
    title='Boxplot Densitas Kalori Makanan'
)
plt.show()

# Calorie density histogram.
grid = sns.FacetGrid(
    menu_data,
    col='Category',
    height=2,
    col_wrap=3
)
grid.map(sns.histplot, 'Calorie Density')
plt.show()

# Menu scatterplot combined.
sns.scatterplot(
    data=menu_data,
    x='Serving Size',
    y='Calories',
    hue='Category'
)
plt.show()

# Menu scatterplot separate.
grid = sns.FacetGrid(
    menu_data,
    col='Category',
    height=2,
    col_wrap=3
)
grid.map(sns.scatterplot, 'Serving Size', 'Calories')
plt.show()
