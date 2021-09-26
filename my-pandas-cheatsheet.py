import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# --- БАЗОВЫЕ ОПЕРАЦИЕ ПО ВЫБОРКЕ ---
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

# Ну типа наоборот, но тут ещё и сумма получаецца
# Тоесть тут кол-во пассажиров Титаника возраст которых неизвестен
# print(df['Age'].isna().sum())

# Имена всех людей для которых известен возраст
# print(df.loc[df['Age'].notna(), 'Name'])

# --- СОРТИРОВКА ---

# Первые 10 записей отсортированные по возрасту
# print(df.sort_values('Age').head(10))

# Первые 10 записей отсортированные по убыванию возраста и по имени в алфавитном порядке
# print(df.sort_values(['Age', 'Name'], ascending=[False, True]).head(10))

# -- Копируем --
# df2 = df.copy(deep=True)

# Присобачиваем один датафрейм под низ другого датафрейма
# cdf1 = pd.concat([df, df2])

# --- АНАЛИТИЧЕСКИЕ ФУНКЦИИ ---

# Кол-во не пустых элементов по всем колонкам
# print(df.count())

# Кол-во элм-ов по колоночке
# print(df['Age'].count())

# -- СРЕДНЕЕ И МЕДИАНА --
# print(df['Age'].mean(), df['Age'].median())

# -- НЕМНОГО ГОТОВОЙ СТАТИСТИКИ (ура) (среднее/мин/макс значения, медиана, квантили) --
# print(df['Age'].describe())

# -- Группируем --
# in next releases (49.99$)