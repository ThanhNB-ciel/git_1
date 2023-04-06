import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

d = {'count': [1,1,1,2,2,3,3,3,4], 
     'name': ['bob','bob','bob','shelby','shelby','jordan','jordan','jordan','jeff'],
     'type': ['type1','type2','type4','type1','type6','type5','type8','type2',None],
     'salary':[1000,2000,3000,10000,15000,30000,100000,50000,25000]}
df = pd.DataFrame(data=d)

# group data and aggregate
df_plot = df.groupby(['name','type'])[['salary','count']].sum().reset_index()
df_plot.sort_values(by=['name','type'],inplace=True)

avg_salary = df_plot['salary'].sum()/df_plot['count'].sum()

# plot treemap
fig = px.treemap(df_plot,
                 values='count',
                 color='salary',
                 color_continuous_scale='balance',
                 color_continuous_midpoint=avg_salary,
                 path=['type','name'])
# fig.data[0].textinfo = 'label+value+percent parent'
percents = (100*df.salary / sum(df.salary)).tolist()
salaries = df.salary.tolist()

## store multiple lists of data in customdata
fig.data[0].customdata = np.column_stack([salaries, percents])
fig.data[0].texttemplate = "%{label}<br>%{value}<br>Salary:$%{customdata[0]}<br>Percent of total:%{customdata[1]:.2f}%"
fig.show()
