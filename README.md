# Leveraged-ETF-Trading-Strategy
### Testing TQQQ and SQQQ Leveraged ETF Trading Strategy
_Note: No Commission fees were incorporated into the calculations (shoutout to WEALTHSIMPLE)_

### Report PDF: [Leveraged ETF Trading Strategy](https://github.com/Aryanpatel335/Leverged-ETF-Trading-Strategy/blob/main/Leveraged-ETF-Trading-Strategy.pdf)

After noting the rapid growth of the market over the past few years, the strategy was thought of to invest in the overall market index with 3x leveraged ETFS. Nasdaq 100 was noted to be the fastest-growing and most volatile index to perform the backtesting strategy. Using 3x leverage ETFs that track the Nasdaq 100 were chosen. TQQQ is a 3x leverage ETF based on the QQQ and SQQQ is a 3x inversed leveraged ETF that tracks the Nasdaq 100. Python and its various libraries were used to visualize the data after calculations were performed on the stock market data fetched from yFinance library. The outcome showed a “switch value” of 0.5 performed the best in the time frame chosen and it outperformed the growth of QQQ by 44.6%. At the end of the time frame using any other switch value using the strategy underperformed the growth of the initial investment of QQQ.

## Results:


![alt_text](https://github.com/Aryanpatel335/Leverged-ETF-Trading-Strategy/blob/main/results/result.png)
_Figure 1: Results of the various switch values and baseline trading strategies for comparison_

![alt_text](https://github.com/Aryanpatel335/Leverged-ETF-Trading-Strategy/blob/main/results/intraday_results.png)

_Figure 2: Raw output from dataframe_

