import pyupbit
import numpy
import pandas as pd
import time

#거래량 상위 10개 티커 추출
tickerlist = pyupbit.get_tickers(fiat = "KRW")
top20 = []

for i in range(0,len(tickerlist)):
    data = pyupbit.get_ohlcv(tickerlist[i], count = 1)
    value = float(str(data['value'])[23:-28])
    if (i < 12):
        top10.append(value)
    else:
        if (min(top10) < value):
            tindex = top10.index(min(top20))
            top10[tindex] = value
            tickerlist[tindex] = tickerlist[i]
    time.sleep(0.2)
del tickerlist[0:2]
del tickerlist[9:-1]
del top10[0:2]

acckey = '4lLO0AEaSxEgRUUehxl84NnMW7J1auDxXIaODxnn'
seckey = 'APcOEHpbxgsawLBRcVNgXYROdcL1Eld3EtQBdXoA'
upbit = pyupbit.Upbit(acckey, seckey)

while(1):
    #60분 rsi 계산함수
    data60 = pyupbit.get_ohlcv("KRW-BTC", interval = "minute60", count = 15)
    data30 = pyupbit.get_ohlcv("KRW-BTC", interval = "minute30", count = 15)

    def rsi_calc(ohlc: pd.DataFrame, period: int = 14):
        delta = ohlc["close"].diff()
        ups, downs = delta.copy(), delta.copy()
        ups[ups < 0] = 0
        downs[downs > 0] = 0
        au = ups.ewm(com = period-1, min_periods = period).mean()
        ad = downs.abs().ewm(com = period-1, min_periods = period).mean()
        rs = au/ad
        return pd.Series(100-(100/(1+rs)), name = "RSI")

    rsi60 = rsi_calc(data60, 14).iloc[-1]
    rsi30 = rsi_calc(data30, 14).iloc[-1]

    #매매코드
    seed = int(upbit.get_balance("KRW"))

    if(rsi60 <= 36 && rsi30 <= 32 && seed > 0):
        for i in range(10):
            upbit.buy_market_order(tickerlist[i], (seed/10))
    
    for i in range(10):
        upbit.get_balance(tickerlist[i])['balance']
        upbit.sell_market_order(tickerlist[i], upbit.get_balance(tickerlist[i])['balance'])

    if(len(upbit.get_balance()) == 1):
        print("매도 완료")
        break
