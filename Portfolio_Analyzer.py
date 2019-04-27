import numpy as np
import pandas as pd
#import quandl as web
import pandas_datareader as web
import matplotlib.pyplot as plt


stocks = ['DBX','ESV','AMD','S','SUN','SYF']
starttime = '10/4/2017'
endtime = '4/19/2019'
quantity = [12,8,100,25,10,25,20,5,50,10,30]
price=[5.87,10.37,5.67,26.13]
holding_period=['not','13.66','','not']

portfolio_df = pd.DataFrame()

def stock_pull(stock,starttime,endtime):

    data = web.tiingo.TiingoDailyReader(stock,start = starttime,end=endtime,api_key='43580dea04ec443ded0a1ff9d2f556353e2ac14d').read()
    print(data)
    return data
stock_pull('DBX',starttime,endtime)
#print(stock_pull('DBX',starttime,endtime))

# all_dates = []

# for index,symbol in enumerate(stocks):
#     symbol_data = stock_pull(symbol,starttime,endtime)
#     symbol_data.reset_index(inplace=True)
#     portfolio_df = pd.concat([portfolio_df,symbol_data])
    
# all_dates = portfolio_df['date'].unique()

# print(all_dates)
# portfolio_df_1 = pd.DataFrame()
# all_symbols = portfolio_df['symbol'].unique()
# daily_data_df = pd.DataFrame()
# daily_data_df['date'] = all_dates

# for date in all_dates:
#     print(date)
#     portfolio_df.loc[portfolio_df['date'] == date]
    
#     for each_symbol in stocks:
    
#         daily_data = portfolio_df.loc[(portfolio_df['symbol'] == each_symbol) & (portfolio_df['date'] == date)]
#         try:
#             daily_data_df.loc[daily_data_df['date'] == date,each_symbol + ' close'] = float(daily_data['close'])
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' open'] = float(daily_data['open'])
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' high'] = float(daily_data['high'])
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' low'] = float(daily_data['low'])
#         except:
#             daily_data_df.loc[daily_data_df['date'] == date,each_symbol + ' close'] = 0
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' open'] = 0
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' high'] = 0
#             daily_data_df.loc[daily_data_df['date'] == date, each_symbol + ' low'] = 0


#     portfolio_df_1 = pd.concat([portfolio_df_1,])

# portfolio_df.reset_index(inplace=True)
# #df = stock_pull('ESV','1/1/2019','2/1/2019')
# tags = list(portfolio_df.columns.values)
# daily_data_df.sort_values(by=['date'],inplace=True)
# print(daily_data_df)
# #print(portfolio_df)
# portfolio_df.to_csv('historical_data.csv')
# daily_data_df.to_csv('formated_data.csv',index=False)


# daily_data_df = pd.read_csv('formated_data.csv')
# daily_data_df_date=daily_data_df['date']
# dbx = daily_data_df['DBX close']
# plt.plot(daily_data_df_date,dbx)
# plt.show()




