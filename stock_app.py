

import pandas as pd
res = connect.execute(f"select * from stock_history where symbol='{symbol}' and date > '2020-01-01' order by date")
data = pd.DataFrame(res)
data.columns = [f"{symbol}_"+item[0] if item[0]!="DATE" else "DATE" for item in res.description]

z.show(data)

symbol1 = "SPY"
res = connect.execute(f"select * from stock_history where symbol='{symbol1}' and date > '2020-01-01' order by date")
data1 = pd.DataFrame(res)
data1.columns = [f"{symbol1}_"+item[0] if item[0]!="DATE" else "DATE" for item in res.description]

joined_result = pd.merge(data, data1, on='DATE')
