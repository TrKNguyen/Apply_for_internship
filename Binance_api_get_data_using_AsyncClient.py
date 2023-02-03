apikey = ""
secret = ""
import asyncio
from binance import AsyncClient, BinanceSocketManager
import sqlalchemy
import pandas as pd 
import time
def createFrame(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns= ['symbol','Time','Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df

async def main():
    coin = 'BTCUSDT'
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')
    ts = bm.trade_socket(coin)
    pre = int(time.time())
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            frame=createFrame(res)
            frame.to_sql('BTCUSDT',engine,if_exists='append',index=False)      
            print(frame)

    await client.close_connection()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    