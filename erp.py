import pandas as pd
import matplotlib
from sqlalchemy import create_engine


engine = create_engine('postgresql://mogo_erp:UiyiLahyook2iewucotaesh3@localhost:5434/mogo_erp_ug_dev')

df = pd.read_sql_query('select * from public.commissions',con=engine)

df['rate'].plot(kind='hist', legend=True)

matplotlib.pyplot.show()