def strategy(balance_trend, df, date_index, switch_threshold):
    for i in range(2,len(date_index)):
        nasdaq_prev_day_change = df['nasdaq_pctChange_adjClose'].iloc[i-1]
        
        commission = 0 
        if abs(nasdaq_prev_day_change) < switch_threshold:
            # With the trend
            if nasdaq_prev_day_change < 0:
                balance = balance_trend[i-1] + (balance_trend[i-1] * df['sqqq_intraday'].iloc[i])
                balance_trend.append(balance - commission)
            else:
                balance = balance_trend[i-1] + (balance_trend[i-1] * df['tqqq_intraday'].iloc[i])
                balance_trend.append(balance - commission)

        else:
            # Opposite the trend
            if nasdaq_prev_day_change < 0:
                balance = balance_trend[i-1] + (balance_trend[i-1] * df['tqqq_intraday'].iloc[i])
                balance_trend.append(balance - commission)
            else:
                balance = balance_trend[i-1] + (balance_trend[i-1] * df['sqqq_intraday'].iloc[i])
                balance_trend.append(balance - commission)
        
        
    return balance_trend