import pandas as pd
import matplotlib
import quandl
import config

quandl.ApiConfig.api_key = config.quand_api_key

df = quandl.get('WIKI/GOOGL')

# df.plot(kind='as', legend=True)
# matplotlib.pyplot.show()

print(df)