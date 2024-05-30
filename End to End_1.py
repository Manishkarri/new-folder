import pandas as pd
import altair as alt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv( "C:\Users\chand\Downloads\sales_data_sample.csv", encoding='latin1')

# Convert `ORDERDATE` to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Aggregate data at daily level
df_daily_agg = df.groupby(df['ORDERDATE'].dt.date)[['SALES', 'QUANTITYORDERED']].sum().reset_index()

# Aggregate data at monthly level
df_monthly_agg = df.groupby(pd.Grouper(key='ORDERDATE', freq='M'))[['SALES', 'QUANTITYORDERED']].sum().reset_index()

# Aggregate data at yearly level
df_yearly_agg = df.groupby(pd.Grouper(key='ORDERDATE', freq='Y'))[['SALES', 'QUANTITYORDERED']].sum().reset_index()

# Aggregate data at product level
df_product_agg = df.groupby('PRODUCTLINE')[['SALES', 'QUANTITYORDERED']].sum().reset_index()
df_product_agg['AVG_PRICE'] = df.groupby('PRODUCTLINE')['PRICEEACH'].mean().reset_index()['PRICEEACH']
df_product_agg['DISTINCT_ORDERS'] = df.groupby('PRODUCTLINE')['ORDERNUMBER'].nunique().reset_index()['ORDERNUMBER']

# Aggregate data at customer level
df_customer_agg = df.groupby('CUSTOMERNAME')[['SALES', 'QUANTITYORDERED']].sum().reset_index()
df_customer_agg['AVG_PRICE'] = df.groupby('CUSTOMERNAME')['PRICEEACH'].mean().reset_index()['PRICEEACH']
df_customer_agg['DISTINCT_ORDERS'] = df.groupby('CUSTOMERNAME')['ORDERNUMBER'].nunique().reset_index()['ORDERNUMBER']

# Aggregate data at country level
df_country_agg = df.groupby('COUNTRY')[['SALES', 'QUANTITYORDERED']].sum().reset_index()

# Aggregate data at dealsize level
df_dealsize_agg = df.groupby('DEALSIZE')[['SALES', 'QUANTITYORDERED']].sum().reset_index()

# Convert `ORDERDATE` to string in all aggregated dataframes
df_daily_agg['ORDERDATE'] = df_daily_agg['ORDERDATE'].astype(str)
df_monthly_agg['ORDERDATE'] = df_monthly_agg['ORDERDATE'].astype(str)
df_yearly_agg['ORDERDATE'] = df_yearly_agg['ORDERDATE'].astype(str)

# Plot a line chart of total `SALES` and `QUANTITYORDERED` over time using `df_daily_agg`
chart1 = alt.Chart(df_daily_agg, title='Daily Sales and Quantity Ordered Over Time').mark_line(point=True).encode(
    x='ORDERDATE:T',
    y=alt.Y('SALES:Q', axis=alt.Axis(title='Sales', titleColor='blue')),
    color=alt.value('blue'),
    tooltip=['ORDERDATE', 'SALES']
).encode(
    y=alt.Y('QUANTITYORDERED:Q', axis=alt.Axis(title='Quantity Ordered', titleColor='red')),
    color=alt.value('red'),
    tooltip=['ORDERDATE', 'QUANTITYORDERED']
).interactive()

chart1.save('daily_sales_and_quantity_ordered_over_time_line_chart.json')

# Plot a line chart of total `SALES` and `QUANTITYORDERED` over time using `df_monthly_agg`
chart2 = alt.Chart(df_monthly_agg, title='Monthly Sales and Quantity Ordered Over Time').mark_line(point=True).encode(
    x='ORDERDATE:T',
    y=alt.Y('SALES:Q', axis=alt.Axis(title='Sales', titleColor='blue')),
    color=alt.value('blue'),
    tooltip=['ORDERDATE', 'SALES']
).encode(
    y=alt.Y('QUANTITYORDERED:Q', axis=alt.Axis(title='Quantity Ordered', titleColor='red')),
    color=alt.value('red'),
    tooltip=['ORDERDATE', 'QUANTITYORDERED']
).interactive()

chart2.save('monthly_sales_and_quantity_ordered_over_time_line_chart.json')

# Plot a line chart of total `SALES` and `QUANTITYORDERED` over time using `df_yearly_agg`
chart3 = alt.Chart(df_yearly_agg, title='Yearly Sales and Quantity Ordered Over Time').mark_line(point=True).encode(
    x='ORDERDATE:T',
    y=alt.Y('SALES:Q', axis=alt.Axis(title='Sales', titleColor='blue')),
    color=alt.value('blue'),
    tooltip=['ORDERDATE', 'SALES']
).encode(
    y=alt.Y('QUANTITYORDERED:Q', axis=alt.Axis(title='Quantity Ordered', titleColor='red')),
    color=alt.value('red'),
    tooltip=['ORDERDATE', 'QUANTITYORDERED']
).interactive()

chart3.save('yearly_sales_and_quantity_ordered_over_time_line_chart.json')

# Plot a bar chart of total `SALES` by `PRODUCTLINE`
chart4 = alt.Chart(df_product_agg, title='Total Sales by Product Line').mark_bar().encode(
    x='PRODUCTLINE:N',
    y='SALES:Q',
    color='PRODUCTLINE:N',
    tooltip=['PRODUCTLINE', 'SALES']
).interactive()

chart4.save('total_sales_by_product_line_bar_chart.json')

# Plot a bar chart of total `SALES` by top 10 `CUSTOMERNAME`
top_10_customers = df_customer_agg.nlargest(10, 'SALES')
chart5 = alt.Chart(top_10_customers, title='Total Sales by Top 10 Customers').mark_bar().encode(
    x=alt.X('CUSTOMERNAME:N', sort='-y'),
    y='SALES:Q',
    color='CUSTOMERNAME:N',
    tooltip=['CUSTOMERNAME', 'SALES']
).interactive()

chart5.save('total_sales_by_top_10_customers_bar_chart.json')

# Plot a bar chart of total `SALES` by top 10 `COUNTRY`
top_10_countries = df_country_agg.nlargest(10, 'SALES')
chart6 = alt.Chart(top_10_countries, title='Total Sales by Top 10 Countries').mark_bar().encode(
    x=alt.X('COUNTRY:N', sort='-y'),
    y='SALES:Q',
    color='COUNTRY:N',
    tooltip=['COUNTRY', 'SALES']
).interactive()

chart6.save('total_sales_by_top_10_countries_bar_chart.json')

# Plot a bar chart of total `SALES` by `DEALSIZE`
chart7 = alt.Chart(df_dealsize_agg, title='Total Sales by Deal Size').mark_bar().encode(
    x='DEALSIZE:N',
    y='SALES:Q',
    color='DEALSIZE:N',
    tooltip=['DEALSIZE', 'SALES']
).interactive()

chart7.save('total_sales_by_deal_size_bar_chart.json')
