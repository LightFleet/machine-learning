import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# print(df.loc[[5, 10, 15], ['Name', 'Age']].tail(1))

# Нулевая и девятая колонка элементов с индексами 5, 10 и 15
# print(df.iloc[[5, 10, 15], [0, 9]])

# Первые три колонки элементов с индексом от 5 до 24
# print(df.iloc[5:24, :3])

# df['Age'] > 18 - объект типа Series (true/false проставил) который передали в df и получили выборку по маске!
# print(df[df['Age'] > 18])

