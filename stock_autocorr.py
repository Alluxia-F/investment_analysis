import pandas as pd
from pandas_datareader.data import DataReader
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

data_source='yahoo'
drop_col=['Open','High','Low','Close','Adj Close','Volume']

start_date=date(2010,1,1)
now=date.today()
difference=relativedelta(now,start_date)
years=difference.years

def stock_autocorr(ticker): 
    stock=DataReader(ticker,data_source,start_date)
    stock['mean']=(stock['Open']+stock['High']+stock['Low']+stock['Close'])/4
    stock_change=stock.drop(drop_col,axis=1)
    stock_change['pct_change']=stock_change.pct_change()
    stock_autocorr=stock_change['pct_change'].autocorr()
    print('Over the past {0} years, the auto-correlation of {1} daily point change is:{2}'.format(years,ticker,stock_autocorr))
    
    