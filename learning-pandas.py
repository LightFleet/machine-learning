import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


#print(df.loc[[5, 10, 15], ['Name', 'Age']].tail(1))

print(df.iloc[[5, 10, 15], [0, 9]])
