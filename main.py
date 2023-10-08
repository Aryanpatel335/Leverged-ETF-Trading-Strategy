from strategy import strategy
from qqq_strategy import qqq_strategy
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Define the tickers for TQQQ, SQQQ, and the NASDAQ index
tickers = ['TQQQ', 'SQQQ', '^IXIC', 'QQQ']

# Set the date range for historical data
start_date = '2018-01-01'
end_date = '2023-10-01'

# Fetch historical data
tqqq_data = yf.download(tickers[0], start=start_date, end=end_date)
sqqq_data = yf.download(tickers[1], start=start_date, end=end_date)
nasdaq_data = yf.download(tickers[2], start=start_date, end=end_date)
qqq_data = yf.download(tickers[3],start=start_date, end=end_date)

df_tqqq = pd.DataFrame(tqqq_data)
df_sqqq = pd.DataFrame(sqqq_data)
df_nasdaq = pd.DataFrame(nasdaq_data)
df_qqq = pd.DataFrame(qqq_data)

def calculate_intraday_change(df):
    open_price = list(df['Open'])
    close_price = list(df['Close'])
    intraday_pctChange = []
    for i in range(len(open_price)):
        intraday_pct = ((close_price[i] - open_price[i]) / open_price[i])
        intraday_pctChange.append(intraday_pct)
    return intraday_pctChange

tqqq_intraday = calculate_intraday_change(df_tqqq)
sqqq_intraday = calculate_intraday_change(df_sqqq)
nasdaq_intraday = calculate_intraday_change(df_nasdaq)
qqq_intraday = calculate_intraday_change(df_qqq)

nasdaq_pctChange_adjClose = list(df_nasdaq['Adj Close'].pct_change()*100)

date_index = df_nasdaq.index.tolist()
df_intraday_vals = pd.DataFrame()
df_intraday_vals['date'] = date_index
df_intraday_vals['nasdaq_pctChange_adjClose'] = nasdaq_pctChange_adjClose
df_intraday_vals['tqqq_intraday'] = tqqq_intraday
df_intraday_vals['sqqq_intraday'] = sqqq_intraday
df_intraday_vals['qqq_intraday'] = qqq_intraday

# here 1.5 is SWITCH VALUE
# if adj close gain from PREVIOUS DAY is between 0 - 1.5% or -1.5-0 we wiill buy in that direction for next day, if the pct change is greater than 1.5 in any direction we will buy in opposite direction for next day 

# starting at index ---> see previous was -3.03683 we buy tqqq and multiply our previous val at index 1 which is 10000 by percent change ie 0.0765 so 10000 * 1.0765

switch_threshold = [x/2 for x in range(1,6)]


balance_trend_qqq = [10000, 10000]
qqq_strategy_trend = qqq_strategy(balance_trend_qqq, df_intraday_vals, date_index)

# qqq invest it and forget it strategy 
# invest 10000 and let the stock grow over the years
initial_investment = 10000
qqq_data['Daily_Return'] = qqq_data['Adj Close'].pct_change()
qqq_data['Investment_Value'] = initial_investment * (1 + qqq_data['Daily_Return']).cumprod()

plt.figure(figsize=(18,9))

df_strategy_output = pd.DataFrame()
df_strategy_output['date'] = date_index

# Graphing Strategy with Different Switch Values
column_name = []
for i in range(len(switch_threshold)):
    label = 'Switch Value : ' + str(switch_threshold[i])
    column_name.append(label)

for i,j in enumerate(column_name):
    balance_trend = [10000, 10000]
    df_strategy_output[j] = strategy(balance_trend, df_intraday_vals , date_index, switch_threshold[i] )

for i in column_name:
    plt.plot(df_intraday_vals['date'], df_strategy_output[i], label=i)

print(df_intraday_vals)
print(df_strategy_output)

# intraday_vals_csv = 'intraday_data.csv'
# strategy_output_csv = 'strategy_output_data.csv'

# df_intraday_vals.to_csv(intraday_vals_csv, index=False)
# df_strategy_output.to_csv(strategy_output_csv, index=False)

plt.plot(df_intraday_vals['date'], qqq_strategy_trend, linestyle='--', label="QQQ Intra Strategy")
plt.plot(qqq_data.index, qqq_data['Investment_Value'], label='QQQ Investment')
plt.axhline(y=10000, color='red', linestyle='--', label='Initial Investment')
plt.title('TQQQ, SQQQ Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Account Balance in Dollars')
plt.legend()
plt.grid(True)

plt.show()