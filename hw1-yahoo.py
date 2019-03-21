
from pandas_datareader import data as web
import datetime as dt
import fix_yahoo_finance as yf
yf.pdr_override()
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2018, 12, 31)
df = web.get_data_yahoo(['VNQ'],start, end)
df.to_csv(r'VNQ.csv')

from pandas_datareader import data as web
import datetime as dt
import fix_yahoo_finance as yf
yf.pdr_override()
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2018, 12, 31)
df = web.get_data_yahoo(['VNQI'],start, end)
df.to_csv(r'VNQI.csv')


from pandas_datareader import data as web
import datetime as dt
import fix_yahoo_finance as yf
yf.pdr_override()
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2018, 12, 31)
df = web.get_data_yahoo(['SCHH'],start, end)
df.to_csv(r'SCHH.csv')

from pandas_datareader import data as web
import datetime as dt
import fix_yahoo_finance as yf
yf.pdr_override()
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2018, 12, 31)
df = web.get_data_yahoo(['IYR'],start, end)
df.to_csv(r'IYR.csv')


realestate= ['VNQ','VNQI','SCHH','IYR','XLRE','RWR','RWX','RWO','ICF','REET','REM','USRT','FREL']

for i in realestate:
    j = i + ".TW"


for k in realestate:
    try :
        df = web.get_data_yahoo([k],start, end)
        if df.empty == False:
            df.to_csv(k + '.csv')
        else :
            pass
    except :
        pass