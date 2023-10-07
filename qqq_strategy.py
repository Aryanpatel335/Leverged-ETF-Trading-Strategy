def qqq_strategy(balance_trend, df, date_index):
    for i in range(2,len(date_index)):
        balance =  balance_trend[i-1] + (balance_trend[i-1] * df['qqq_intraday'].iloc[i])
        
        commission = 0 

        balance_trend.append(balance - commission)
        
    return balance_trend