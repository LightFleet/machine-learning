import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# print(df.loc[[5, 10, 15], ['Name', 'Age']].tail(1))

# Нулевая и девятая колонка элементов с индексами 5, 10 и 15
# print(df.iloc[[5, 10, 15], [0, 9]])

# Первые три колонки элементов с индексом от 5 до 24
# print(df.iloc[5:24, :3])

# df['Age'] > 18 - объект типа Series (true/false проставил) который передали в df и получили выборку по маске!
# print(df[df['Age'] > 18])

# Все пассажиры 5-10-15 лет
# print(df[df['Age'].isin([5, 10, 15])])

# Возвращает маску (карту) где проверяет есть ли элемент на этом месте
# print(df['Age'].notna())

# Ну типа наоборот, но тут ещё и пропуск
# Тоесть тут кол-во пассажиров Титаника возраст которых неизвестен
# print(df['Age'].isna().sum())

# Имена всех людей для которых известен возраст
# print(df.loc[df['Age'].notna(), 'Name'])

### СОРТИРОВКА

# Первые 10 записей отсортированные по возрасту
print(df.sort_values('Age').head(10))


